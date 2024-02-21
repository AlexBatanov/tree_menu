# Тестовое задание Django Tree Menu

Это приложение Django позволяет создавать иерархические древовидные меню в админ-панели и отображать их на любой странице с помощью пользовательского тега шаблона.


<img src="https://github.com/AlexBatanov/tree_menu/blob/main/git_media/Запись%20экрана%20от%202024-02-21%2015-39-27.gif" width="250" height="300">

## Особенности
- Иерархическая структура древовидного меню
- Элементы меню хранятся в базе данных
- Редактирование меню в админ-панели Django
- Выделение активного элемента меню на основе текущего URL страницы
- Возможность размещения нескольких меню на одной странице с различными именами
- Переход на указанные URL или именованные URL при нажатии на элемент меню
- Для отрисовки каждого меню требуется всего 1 запрос к базе данных

## Установка
1. Клонируйте репозиторий:
   ```
   git clone git@github.com:AlexBatanov/tree_menu.git
   ```
2. Установите необходимые пакеты:
   ```
   pip install django
   ```
3. Примените миграции:
   ```
   python manage.py migrate
   ```
