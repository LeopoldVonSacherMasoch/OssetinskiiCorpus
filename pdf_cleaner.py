import os
from pdfminer.high_level import extract_text

# Путь к исходной папке с PDF-файлами
source_folder = "C:/Users/Administrator/Desktop/praktika/pdf_files"

# Путь к папке, в которую будут сохранены новые txt-файлы
output_folder = "new_pdf_files"

# Создание папки output_folder (если она не существует)
os.makedirs(output_folder, exist_ok=True)

# Обход папки с PDF-файлами
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if file.endswith(".pdf"):
            # Получение полного пути к текущему PDF-файлу
            pdf_path = os.path.join(root, file)
            
            try:
                # Извлечение текста из PDF-файла
                text = extract_text(pdf_path)
                
                # Формирование пути и имени нового txt-файла
                txt_filename = file.replace(".pdf", ".txt")
                output_path = os.path.join(output_folder, txt_filename)
                
                # Сохранение текста в новом txt-файле
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)
                
                print(f"Извлечен текст из файла: {pdf_path}")
                print(f"Создан новый txt-файл: {output_path}\n")
            
            except Exception as e:
                print(f"Ошибка при обработке файла {pdf_path}:", str(e))