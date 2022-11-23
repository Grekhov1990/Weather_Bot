from aiogram import Bot, Dispatcher, executor, types
import python_weather

bot = Bot(token='5829622337:AAHeOMfMJ4NYdsbNCwuJ52JUCJBKmRVQ4NY')
dp = Dispatcher(bot)
client = python_weather.Client(format=python_weather.IMPERIAL)



@dp.message_handler()
async def echo ( message: types. Message):
    weather = await client.get(message.text)
    celsius = round((weather.current.temperature - 32) / 1.8)
    resp_msg = message.text + "\n"
    resp_msg += f"Текущая температура: {celsius}\n"
    resp_msg += f"Состояние погоды: {weather.current.type}\n"
    if celsius < 10:
        resp_msg += "На улице ад... сиди дома, ты что псих совсем?"
    elif celsius < 20:
        resp_msg += "На улице холодно-одевайся как танк!"
    else:
        resp_msg += "Температура кайф, го на тусу,че сидишь как дуб?!"
    await message.answer(resp_msg)



if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=True)
