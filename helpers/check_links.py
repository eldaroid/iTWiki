#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import unicodedata
from urllib.parse import unquote
from pathlib import Path

# Убедимся, что stdout использует UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Цвета
RED = '\033[0;31m'
GREEN = '\033[0;32m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

def simple_progress_bar(current, total, bar_length=40):
    """Простой прогресс-бар с процентами и счётчиком"""
    percent = current / total
    arrow = '=' * int(round(percent * bar_length))
    spaces = ' ' * (bar_length - len(arrow))
    
    # Формируем строку прогресс-бара
    bar = f"[{arrow}{spaces}] {percent:.1%} ({current}/{total})"
    
    # Возвращаем строку для перезаписи
    return bar

def normalize_path(path):
    """Нормализует путь для правильной работы с эмодзи на macOS"""
    return {
        'nfc': unicodedata.normalize('NFC', path),
        'nfd': unicodedata.normalize('NFD', path),
    }

def path_exists_normalized(path):
    """Проверяет, существует ли путь с учетом различных форм Unicode"""
    if os.path.exists(path):
        return True
    normalized = normalize_path(path)
    for variant in ['nfc', 'nfd']:
        if os.path.exists(normalized[variant]):
            return True
    return False

def extract_markdown_links(text):
    """Извлекает все markdown ссылки [text](url) включая вложенные скобки."""
    links = []
    i = 0
    while i < len(text):
        start = text.find('[', i)
        if start == -1:
            break
        close_bracket = text.find(']', start)
        if close_bracket == -1:
            i = start + 1
            continue
        if close_bracket + 1 >= len(text) or text[close_bracket + 1] != '(':
            i = close_bracket + 1
            continue
        paren_start = close_bracket + 2
        paren_count = 1
        j = paren_start
        while j < len(text) and paren_count > 0:
            if text[j] == '(':
                paren_count += 1
            elif text[j] == ')':
                paren_count -= 1
            j += 1
        if paren_count != 0:
            i = close_bracket + 1
            continue
        link_text = text[start + 1:close_bracket]
        link_url = text[paren_start:j - 1]
        links.append((link_text, link_url))
        i = j
    return links

def check_file(filepath):
    """Проверяет все ссылки в одном markdown файле."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (IOError, UnicodeDecodeError):
        return None

    matches = extract_markdown_links(content)
    broken_links = []
    working_links = 0
    total_links = 0
    external_links = 0
    file_dir = os.path.dirname(filepath)

    for text, url in matches:
        total_links += 1
        
        # Отделяем query параметры (?) и якоря (#)
        path_part = url
        
        # Обрабатываем query параметры
        if '?' in path_part:
            path_part, query_part = path_part.split('?', 1)
        
        # Обрабатываем якорь
        if '#' in path_part:
            path_part, anchor_part = path_part.split('#', 1)
        
        if not path_part:
            continue
            
        if path_part.startswith('http'):
            external_links += 1
            continue
            
        try:
            decoded_url = unquote(path_part, encoding='utf-8', errors='replace')
        except Exception:
            decoded_url = path_part
            
        check_path = decoded_url.rstrip('/')
        
        if check_path.startswith('/'):
            full_path = check_path.lstrip('/')
        else:
            full_path = os.path.normpath(os.path.join(file_dir, check_path))
            
        if path_exists_normalized(full_path):
            working_links += 1
        else:
            broken_links.append((url, decoded_url, full_path))

    return {
        'total': total_links,
        'working': working_links,
        'broken': broken_links,
        'external': external_links
    }

# Собираем все markdown файлы
md_files = list(Path('.').rglob('*.md'))
md_files.sort()
total_files = len(md_files)

print(f"{YELLOW}Проверка всех markdown файлов в проекте...{NC}")
print("=" * 70)

# Сбор результатов с прогресс-баром
results = []
files_with_broken = []

# Прогресс-бар
print()  # Отступ для красоты
for i, md_file in enumerate(md_files, 1):
    # Показываем прогресс-бар
    progress = simple_progress_bar(i, total_files)
    sys.stdout.write(f"\r{YELLOW}{progress}{NC}")
    sys.stdout.flush()
    
    # Обрабатываем файл
    result = check_file(str(md_file))
    if result is None or result['total'] == 0:
        continue
        
    results.append((str(md_file), result))
    if result['broken']:
        files_with_broken.append((str(md_file), result['broken']))

# Очищаем строку с прогресс-баром
sys.stdout.write("\r" + " " * 60 + "\r")
sys.stdout.flush()

# Подсчёт итогов
total_working = sum(r['working'] for _, r in results)
total_broken = sum(len(r['broken']) for _, r in results)
total_external = sum(r['external'] for _, r in results)

print("\n" + "=" * 70)

# Вывод результатов для каждого файла
for filepath, result in results:
    if result['broken']:
        print(f"{RED}✗{NC} {filepath}")
        for url, decoded, full_path in result['broken']:
            print(f"   {RED}• {decoded}{NC}")
    else:
        print(f"{GREEN}✓{NC} {filepath} ({result['working']} ссылок)")

print("")
print("=" * 70)
print(f"Всего markdown файлов проверено: {len(md_files)}")
print(f"{GREEN}Рабочие внутренние ссылки:{NC} {total_working}")
print(f"{YELLOW}Внешние ссылки:{NC} {total_external}")
print(f"{RED}Сломанные ссылки:{NC} {total_broken}")

if total_broken > 0:
    print(f"\n{RED}Файлы со сломанными ссылками ({len(files_with_broken)}):{NC}")
    for filepath, broken in files_with_broken:
        print(f"  • {filepath}")
    sys.exit(1)
else:
    print(f"\n{GREEN}✓ Все ссылки во всех файлах работают!{NC}")
    sys.exit(0)
