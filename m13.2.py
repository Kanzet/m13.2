from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.utils import executor

api = '7758783583:AAFpoCKCoMlcaleYanfXydelGCAvsRtdW8'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот для общения.Задай любой вопрос и я на него отвечу в течение 10 секунд!')
@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)