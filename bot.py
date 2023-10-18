from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram import executor
import extractor
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(msg: types.Message):
    await msg.answer("Hello! \n" +
               "I will export audio from a YouTube video you send! \n" +
               "Just type @vid and your search request, \n" +
               "then choose video you like.")

@dp.message_handler(Text(startswith="http"))
async def send_audio(msg: types.Message):
    await msg.answer("Please, wait while bot processes your request...")
    audio_extractor = extractor.Extractor(msg.text)
    audio_extractor.extract_audio()
    await bot.send_voice(voice=open("extracted//audio.mp3", "rb"), chat_id=msg.chat.id)

def start_bot():
    executor.start_polling(dp)

