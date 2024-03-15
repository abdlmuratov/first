from aiogram import Bot, Dispatcher, types
from replyboard import kb
from replyboard import kbr
API_TOKEN = '6592990582:AAERb8J9I2-PbX8wDAEGSoOGYZqlpYqnXEE'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_sticker(chat_id=message.chat.id,sticker="CAACAgIAAxkBAAMWZcJEZoKSThY2pPs65ovqBGj0O80AAsMYAAL0EDBLwY6GsNYEYZY0BA", reply_markup=kb)

@dp.message_handler(commands=['photo'])
async def send_photo(message: types.Message):
    with open('photo_2024-02-07_10-19-52.jpg', 'rb') as file:
        await bot.send_photo(chat_id=message.chat.id, photo=file)
        await message.answer("Нуриддин Шамуратов")


@dp.message_handler(content_types=['photo'])
async def photo(message: types.message):
    await message.answer(message.sticker.file_id, reply_markup=kb)
    
@dp.message_handler(text="Биография Нуриддина")
async def bio(message: types.message):
    await message.answer("я Шамуратов Нуриддин родился в 2007 году мне нравится кс го")

@dp.message_handler(text="Инстаграм аккаунт")
async def insta(message: types.message):
    await message.answer("insta",reply_markup=kbr)

@dp.message_handler(text="Номер телефон")
async def number(message: types.message):
    await message.answer('+998907232799')

@dp.message_handler(text="Телеграм аккаунт")
async def telegram(message: types.message):
    await message.answer("https://t.me/Nuriddinsha")

@dp.message_handler(text="Фразы Нуриддина")
async def fraz(message: types.message):
    await message.answer("Коронная фраза: Пош")

@dp.message_handler(content_types=['contact'])
async def contact(message: types.message):
    name = message.from_user.first_name
    phone_number= message.contact.phone_number
    txt=f"{phone_number},{name}"
    await bot.send_message(chat_id="-4149337673", text=txt)

@dp.message_handler(content_types=['location'])
async def contact(message: types.message):
    name = message.from_user.first_name
    long = message.location.longitude
    lat = message.location.latitude
    static_map_url = f"https://static-maps.yandex.ru/1.x/?lang=ru_RU&ll={long},{lat}&z=15&l=map&pt={long},{lat},pm2rdm"
    await bot.send_photo(chat_id=-4149337673, photo=static_map_url)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)