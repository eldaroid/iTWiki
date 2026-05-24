#!/bin/bash

# Функция для кодирования URL (для относительных ссылок)
url_encode() {
    local url="$1"
    local length="${#url}"
    for (( i = 0; i < length; i++ )); do
        local c="${url:i:1}"
        case "$c" in
            [a-zA-Z0-9._-]) printf "$c" ;;
            ' ') printf '%%20' ;;
            *) printf '%%%02X' "'$c" ;;
        esac
    done
}

# Функция для рекурсивного обхода директорий и создания Markdown-дерева
generate_tree() {
    local current_dir="$1"
    local indent="$2"
    local prefix="$3"

    # Проходим по каждому элементу в директории
    for file in "$current_dir"/*; do
        # Проверяем, существует ли файл или директория
        [ -e "$file" ] || continue

        # Получаем относительный путь для ссылки
        relative_path="${file#$root_dir/}"
        # Кодируем относительный путь для URL
        encoded_path=$(url_encode "$relative_path")

        # Получаем имя файла или директории
        basename_file=$(basename "$file")

        # Проверяем, является ли элемент директорией
        if [ -d "$file" ]; then
            case "$basename_file" in
                *.xcodeproj|*.xcassets|pictures)
                    # Пропускаем директории с указанными расширениями
                    continue
                    ;;
                *)
                    # Выводим ссылку на директорию и рекурсивно обходим её содержимое
                    echo "${indent}* [${prefix}${basename_file} Folder](${encoded_path}/)"
                    generate_tree "$file" "$indent  " "$prefix"
                    ;;
            esac
        elif [ -f "$file" ]; then
            case "$basename_file" in
                *.entitlements)
                    # Пропускаем файлы с расширением .entitlements
                    continue
                    ;;
                *)
                    # Выводим ссылку на файл
                    echo "${indent}* [${prefix}${basename_file}](${encoded_path})"
                    ;;
            esac
        fi
    done
}

# Устанавливаем начальную директорию
root_dir=$(pwd)

# Начинаем с заголовка
echo "# Project tree"
echo

# Запускаем генерацию дерева с начальной директории
generate_tree "$root_dir" "" ""

