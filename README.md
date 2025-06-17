# Django Menu

Проект реализует древовидное выпадающее меню, которое можно редактировать через Django Admin.  
Меню поддерживает неограниченную вложенность и отображается с помощью кастомного тега `draw_menu`.

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/EnoticKreker/MenuProjectDjango.git
   cd MenuProjectDjango
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Примените миграции:
   ```bash
   python manage.py migrate
   ```
5. Создайте суперпользователя для доступа к админке:
   ```bash
   python manage.py createsuperuser
   ```
6. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
7. Откройте в браузере:
  - Сайт: http://127.0.0.1:8000
  - Админка: http://127.0.0.1:8000/admin

## Шаблоны
Меню рендерится через кастомный тег:
   ```bash
   {% load menu_tags %}
   {% draw_menu 'Главное меню' %}
   ```

