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

def normalize_path(path):
    """Нормализует путь для правильной работы с эмодзи на macOS"""
    # macOS использует NFD, Python предпочитает NFC
    # Проверим оба варианта
    return {
        'nfc': unicodedata.normalize('NFC', path),
        'nfd': unicodedata.normalize('NFD', path),
    }

def path_exists_normalized(path):
    """Проверяет, существует ли путь с учетом различных форм Unicode"""
    if os.path.exists(path):
        return True
    
    # Пытаемся оба варианта нормализации
    normalized = normalize_path(path)
    for variant in ['nfc', 'nfd']:
        if os.path.exists(normalized[variant]):
            return True
    
    return False

def extract_markdown_links(text):
    """
    Извлекает все markdown ссылки [text](url) включая те, что содержат скобки в url.
    Правильно обрабатывает сбалансированные скобки в URL.
    """
    links = []
    i = 0
    while i < len(text):
        # Ищем открывающую квадратную скобку
        start = text.find('[', i)
        if start == -1:
            break
        
        # Ищем закрывающую квадратную скобку
        close_bracket = text.find(']', start)
        if close_bracket == -1:
            i = start + 1
            continue
        
        # Проверяем, есть ли открывающая круглая скобка сразу после
        if close_bracket + 1 >= len(text) or text[close_bracket + 1] != '(':
            i = close_bracket + 1
            continue
        
        # Теперь нам нужно найти закрывающую круглую скобку
        # Учитываем сбалансированность скобок
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
        
        # Извлекаем текст и URL
        link_text = text[start + 1:close_bracket]
        link_url = text[paren_start:j - 1]
        links.append((link_text, link_url))
        
        i = j
    
    return links

def check_file(filepath):
    """Проверяет все ссылки в одном markdown файле"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return None
    
    # Извлекаем все ссылки, правильно обрабатывая скобки
    matches = extract_markdown_links(content)
    
    broken_links = []
    working_links = 0
    total_links = 0
    external_links = 0
    
    # Директория, где находится текущий файл
    file_dir = os.path.dirname(filepath)
    
    for text, url in matches:
        total_links += 1
        
        # Разделяем URL на путь и якорь
        # Якоря могут быть вида #anchor или #:~:text=...
        if '#' in url:
            path_part, anchor_part = url.split('#', 1)
        else:
            path_part = url
            anchor_part = None
        
        # Если это чистый якорь (только якорь без пути), пропускаем
        if not path_part:
            continue
        
        # Внешние ссылки
        if path_part.startswith('http'):
            external_links += 1
            continue
        
        # Внутренние ссылки
        # Декодируем URL-кодированные символы (включая эмодзи)
        try:
            # unquote с явным указанием кодировки UTF-8
            decoded_url = unquote(path_part, encoding='utf-8', errors='replace')
        except Exception as e:
            decoded_url = path_part
        
        # Удаляем конечный слэш для проверки (для директорий)
        # но сохраняем оригинальный путь для вывода
        check_path = decoded_url.rstrip('/')
        
        # Получаем полный путь относительно файла
        if check_path.startswith('/'):
            # Абсолютный путь от корня проекта
            full_path = check_path.lstrip('/')
        else:
            # Относительный путь от директории файла
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

# Ищем все markdown файлы рекурсивно
md_files = list(Path('.').rglob('*.md'))
md_files.sort()

total_working = 0
total_broken = 0
total_external = 0
total_anchors = 0
files_with_broken = []

print(f"{YELLOW}Проверка всех markdown файлов в проекте...{NC}")
print("=" * 70)

for md_file in md_files:
    result = check_file(str(md_file))
    if result is None:
        continue
    
    if result['total'] == 0:
        continue
    
    total_working += result['working']
    total_external += result['external']
    total_broken += len(result['broken'])
    
    # Выводим информацию о файле, если есть проблемы
    if result['broken']:
        files_with_broken.append((str(md_file), result['broken']))
        print(f"{RED}✗{NC} {md_file}")
        for url, decoded, full_path in result['broken']:
            print(f"   {RED}• {decoded}{NC}")
    else:
        print(f"{GREEN}✓{NC} {md_file} ({result['working']} ссылок)")

print("")
print("=" * 70)
print(f"Всего markdown файлов проверено: {len(md_files)}")
print(f"{GREEN}Рабочие внутренние ссылки:{NC} {total_working}")
print(f"{YELLOW}Внешние ссылки:{NC} {total_external}")
print(f"{RED}Сломанные ссылки:{NC} {total_broken}")

if total_broken > 0:
    print(f"\n{RED}Файлы со сломанными ссылками ({len(files_with_broken)}):${NC}")
    for filepath, broken in files_with_broken:
        print(f"  • {filepath}")
    sys.exit(1)
else:
    print(f"\n{GREEN}✓ Все ссылки во всех файлах работают!{NC}")
    sys.exit(0)
