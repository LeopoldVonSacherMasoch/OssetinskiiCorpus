import os

# Путь к папке с файлами
folder_path = 'C:/Users/Administrator/Desktop/praktika/2txt_files'

# Получаем список файлов в папке
file_list = os.listdir(folder_path)

# Проходимся по каждому файлу
for file_name in file_list:
    
    # Формируем полный путь к файлу
    file_path = os.path.join(folder_path, file_name)

    # Открываем файл для чтения и записи
    with open(file_path, 'r+', encoding='utf-8') as file:
        # Считываем все строки из файла
        lines = file.readlines()

        # Переходим в начало файла
        file.seek(0)

        # Записываем все строки, кроме первой, обратно в файл
        file.writelines(lines[1:])

        # Обрезаем файл до новой длины
        file.truncate()
        