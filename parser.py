import requests
from bs4 import BeautifulSoup
import urllib.parse
from urllib.parse import urljoin
import os


# # Функция для загрузки pdf-файлов (газет)
# def download_file(url, directory):
#     response = requests.get(url)
#     file_name = url.split("/")[-1]
#     save_path = os.path.join(directory, file_name)

#     with open(save_path, "wb") as file:
#         file.write(response.content)

# # Парсим все pdf-газеты:

# # URL страниц сайта, с которого нужно спарсить PDF-документы
# for i in range (2, 14):
#   base_url = "https://gazeta-digora.ru/arhiv/page/"+str(i)+"/" #парсим с каждой страницы

#   response = requests.get(base_url)

#   if response.status_code == 200:
#       soup = BeautifulSoup(response.content, "html.parser")
#       links = soup.find_all("a")

#       for link in links:
#           href = link.get("href")

#           # Проверяем, является ли ссылка на PDF-файл
#           if href and href.endswith(".pdf"):
#               absolute_url = urllib.parse.urljoin(base_url, href)

#               # Создаем директорию для сохранения файлов, если она не существует
#               save_directory = "pdf_files"
#               if not os.path.exists(save_directory):
#                   os.makedirs(save_directory)

#               # Загружаем файл
#               download_file(absolute_url, save_directory)

#               print(f"Скачан файл: {absolute_url}")
#   else:
#       print(f"Ошибка при обращении к URL: {base_url}")






# #Парсим тексты
#Так как на сайте присутствуют ajax запросы, придется использовать Selenium, чтобы виртуально нажимать на кнопку "показать еще".
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://gazeta-digora.ru/'

# Создаем драйвер хрома
driver = webdriver.Chrome()

# открываем сайт
driver.get(url)

# Находим кнопку "показать еще"
button = driver.find_element(By.ID, 'true_loadmore')


import time
# Функция для парсинга текстов с сайта
def parse_website(url):
    for _ in range(50):
        time.sleep(3)
        button.click()
    
    page_source = driver.page_source

    # Создаем директорию txt_files, если она не существует
    if not os.path.exists('2txt_files'):
        os.makedirs('2txt_files')

    # Отправляем GET-запрос к указанному URL
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Используем BeautifulSoup для парсинга HTML-кода
        soup = BeautifulSoup(page_source, 'html.parser')

        # Находим все элементы <div> с классами "content", "news_block" и "text-center"
        divs = soup.find_all('div', class_=['content', 'news_block', 'text-center'])

        # Перебираем каждый найденный div
        for i, div in enumerate(divs):
            # Находим все ссылки внутри div
            links = div.find_all('a')

            # Перебираем каждую ссылку
            for link in links:
                # Получаем URL ссылки
                link_url = link.get('href')

                # Отправляем GET-запрос к ссылке
                link_response = requests.get(link_url)

                # Проверяем успешность запроса
                if link_response.status_code == 200:
                    # Используем BeautifulSoup для парсинга HTML-кода ссылки
                    link_soup = BeautifulSoup(link_response.content, 'html.parser')

                    # Находим элемент <div> с классом "post_content"
                    post_div = link_soup.find('div', class_='post_content')

                    # Проверяем, что найденный элемент существует
                    if post_div:
                        # Получаем текст из div
                        text = post_div.get_text()

                        # Генерируем имя файла на основе индекса и URL ссылки
                        filename = f'2txt_files/{link_url.replace("/", "_").replace("https:__gazeta-digora.ru_stati_", "")}.txt'

                        # Сохраняем текст в файл
                        with open(filename, 'w', encoding='utf-8') as file:
                            file.write(text)

                        print(f'Файл {filename} успешно сохранен.')
                    else:
                        print(f'Не удалось найти элемент с классом "post_content" на странице: {link_url}')
                else:
                    print(f'Не удалось получить доступ к ссылке: {link_url}')
    else:
        print('Не удалось получить доступ к указанному URL.')
    
# def parse_website(url):
#     for _ in range(20):
#         time.sleep(3)
#         button.click()
        
#     page_source = driver.page_source

#     # Создаем директорию txt_files, если она не существует
#     if not os.path.exists('txt_files'):
#         os.makedirs('txt_files')

#     # Отправляем GET-запрос к указанному URL
#     response = requests.get(url)

#     # Проверяем успешность запроса
#     if response.status_code == 200:
#         # Используем BeautifulSoup для парсинга HTML-кода
#         soup = BeautifulSoup(page_source, 'html.parser')

#         # Находим все элементы <div> с классами "content", "news_block" и "text-center"
#         divs = soup.find_all('div', class_=['content', 'news_block', 'text-center'])

#         # Перебираем каждый найденный div
#         for i, div in enumerate(divs):
#             # Находим все ссылки внутри div
#             links = div.find_all('a')

#             # Перебираем каждую ссылку
#             for link in links:
#                 # Получаем URL ссылки
#                 link_url = link.get('href')

#                 # Отправляем GET-запрос к ссылке
#                 link_response = requests.get(link_url)

#                 # Проверяем успешность запроса
#                 if link_response.status_code == 200:
#                     # Используем BeautifulSoup для парсинга HTML-кода ссылки
#                     post_div = BeautifulSoup(link_response.content, 'html.parser')

#                     # Находим элемент <h3 class="page-post_title">
#                     title_element = post_div.find('h3', class_='page-post_title')
#                     # Получаем текст из <h3 class="page-post_title">
#                     title_text = title_element.get_text()

#                     # Находим элемент <div class="post_text">
#                     text_element = post_div.find('div', class_='post_text')
#                     # Получаем текст из <div class="post_text">
#                     text = text_element.get_text()

#                     # Объединяем текст из обоих элементов
#                     combined_text = title_text + ' ' + text

#                     # Генерируем имя файла на основе индекса и URL ссылки
#                     filename = f'txt_files/{link_url.replace("/", "_").replace("https:__gazeta-digora.ru_stati_", "")}.txt'

#                     # Сохраняем текст в файл
#                     with open(filename, 'w', encoding='utf-8') as file:
#                         file.write(text)

#                     print(f'Файл {filename} успешно сохранен.')
#                 else:
#                     print(f'Не удалось найти элемент с классом "post_content" на странице: {link_url}')
#             else:
#                 print(f'Не удалось получить доступ к ссылке: {link_url}')
#     else:
#         print('Не удалось получить доступ к указанному URL.')
        
parse_website(url)


driver.close()





