def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        line_count = len(lines)
        return line_count

file_path = 'model.txt'  # Укажите путь к вашему файлу
line_count = count_lines_in_file(file_path)
print(f"Количество строк в файле: {line_count}")