#--- Telegram Бот погоды Cloudy ---#

Бот на aiogram, который выводит погоду исходя из введенного города, присылает погоду по установленному времени

# Технологии
1. Python 3.11+
2. aiogram 3
3. APScheduler
4. SQLite
5. OpenWeatherMap API

# Возможности:
1. Команды /start, /time
2. Вывод погоды по введенному городу
3. Автоопредление города и вывод погоды по геолокации
4. Установка уведомлений
5. Возможность установить до 3 параметров времен, когда будут приходить уведомления

# Установка через GitHub

1. git clone https://github.com/CJArthur/Cloudy_Bot.git
2. cd Cloudy_Bot
3. pip install -r requirements.txt

# Быстрый запуск с помощью Docker
1. Установите Docker(https://www.docker.com/)
2. Создайте файл .env на основе example.env и добавте туда свои ключи
3. Запустите контейнер: docker run -d --env-file .env kab0chinator0385/cloudy_bot:latest