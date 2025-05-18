from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from aiogram import Bot
from database.db import get_all_user_times_and_cities
from utils.weather import get_weather_data_by_city
from utils.weather import get_weather_data_by_city

scheduler = AsyncIOScheduler()

async def send_weather_report(bot: Bot, user_id: int, city: str):
    try:
        weather = await get_weather_data_by_city(city)

        # Формируем сообщение
        message = (f"{weather['greeting']}!\n"
                   f"Погода в городе {weather['city']}\n\n"
                    "📋 Текущие данные\n"
                   f"🕒 Местное время: {weather['time']}\n"
                   f"🌡 Температура: {weather['temp']}°C\n"
                   f"🌡 Ощущается как: {weather['feels_like']}°C\n"
                   f"💧 Влажность: {weather['humidity']}%\n"
                   f"💨 Ветер: {weather['wind']} м/с")

        await bot.send_message(user_id, message)

    except Exception as e:
        print(f"[!] Ошибка при отправке отчета пользователю {user_id}: {e}")

def schedule_weather_jobs(bot: Bot):
    data = get_all_user_times_and_cities() 

    if not data:
        print("[!] Нет данных о времени и городах в базе.")
        return

    for user_id, city, time_str in data:
        try:
            hour, minute = map(int, time_str.split(":"))
            trigger = CronTrigger(hour=hour, minute=minute)

            job_id = f"{user_id}_{city}_{time_str}"

            scheduler.add_job(
                send_weather_report,
                trigger=trigger,
                args=[bot, user_id, city],
                id=job_id,
                replace_existing=True
            )

            print(f"[+] Задача добавлена: {job_id}")
        except Exception as e:
            print(f"[!] Ошибка при добавлении задачи {user_id=} {city=} {time_str=}: {e}")
