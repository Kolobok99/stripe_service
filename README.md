Stripe Service
---
Техническое задание
---
<a href='https://docs.google.com/document/d/1RqJhk-pRDuAk4pH1uqbY9-8uwAqEXB9eRQWLSMM_9sI/edit?usp=sharing'>ссылка на тз</a>

Описание
---
Stripe Service - REST API тестового задания для создания сессии оплаты заказов

Функционал
---
- добавления/обновление/удаление продуктов
- добавления/обновление/удаление скидок
- добавления/обновление/удаление налоговых ставок
- генерирование сессии оплаты продукта
- генерирование сессии оплаты заказа


Дополнительные задания:
---
- 1. запуск в Docker контейнерах
- 2. использование переменных окружения
- 3. просмотр моделей в Django Admin панели
- 4. запуск приложения на удаленном сервере, доступном для тестирования
- 5. реализовать модель Order
- 6. реализовать модель Discount, Tax
- 7. добавить поле currency в модель Item

Системные требования
---
- Windows / Linux / MacOS
- Docker
- Docker-compose

Стек 
---
- Python
- Django
- PostgreSQL
- Nginx
- gunicorn
- Docker, docker-compose

Зависимости
---
- Django==4.1.3
- djangorestframework==3.14.0  
- psycopg2=2.9.5
- stripe==5.0.0
- gunicorn==20.1.0


Запуск проекта
---
1.  Клонировать проект и перейти в его корень:

		git clone https://github.com/ . . .
		cd stripe_service

2. Создать директорию с .env.prod. файлами
		
	    cd backend
		mkdir .env.prod
		cd .env.prod

3. Инициализировать .env.prod/.env.settings со следующими переменными:

	    DEBUG=0
		SECRET_KEY={your_secret_key}
		DJANGO_ALLOWED_HOSTS={your_host_ip}

        POSTGRES_NAME=stripe_db
	    POSTGRES_USER=manager
	    POSTGRES_PASSWORD={your_sql_password}
	    POSTGRES_HOST=db
	    POSTGRES_PORT={your_sql_port}
		
        API_HOST={your_host_ip_with_port}
		STRIPE_PUBLISH_API_KEY={your_stripe_publish_api_key}
		STRIPE_SECRET_API_KEY={your_stripe_secret_api_key}
        
		DATABASE=postgres

4. Инициализировать .env.prod.db со следующими переменными:

		POSTGRES_DB=stripe_db
		POSTGRES_USER=manager
		POSTGRES_PORT={your_sql_port}
		POSTGRES_PASSWORD={your_sql_password}

5. Собрать проект

		cd ../docker-composes
		docker compose -f docker-compose.prod.yml build

6. Запустить проект

		docker compose -f docker-compose.ci.yml up


Документация API:
---
    - GET  api/v1/item/ - получить список всех продуктов
    - POST api/v1/item/ - добавить новый продуктов
    - GET  api/v1/item/{id}/ получить продукт по его id
    - PATCH api/v1/item/{id}/ изменить данные продукта по его id
    - DELETE api/v1/item/{id}/ удалить продукта по его id

	- GET  api/v1/order/ - получить список всех заказов
    - POST api/v1/order/ - добавить новый заказ
    - GET  api/v1/order/{id}/ получить заказ по его id
    - PATCH api/v1/order/{id}/ изменить данные заказ по его id
    - DELETE api/v1/order/{id}/ удалить заказ по его id

	- GET  api/v1/discount/ - получить все скидки
	- POST api/v1/discount/ - добавить новую скидку
	- GET  api/v1/discount/{id}/ получить скидку по еe id
	- DELETE api/v1/discount/{id}/ удалить скидку по его id

	- GET  api/v1/tax/ - получить все налоговые ставки
	- POST api/v1/tax/ - добавить новую налоговую ставку
	- GET  api/v1/tax/{id}/ получить налоговые ставку по еe id
	- PATCH api/v1/tax/{id}/ изменить налоговую ставку по ее id
	- DELETE api/v1/tax/{id}/ удалить налоговую ставку по ее id
	
	- GET api/v1/buy/item/{id}/ получить session оплаты продукта по его id
    - GET api/v1/buy/order/{id}/ получить session оплаты заказа по его id

	- GET item/<id>/ получить страницу продукта по его id
    - GET order/<id>/ получить страницу заказа по его id

