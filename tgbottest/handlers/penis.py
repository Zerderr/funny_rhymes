from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

sogl = "ы, а, о, э, у, и, я, ё, е, ю"
sogl = sogl.split(", ")
sogl_cool = ["и", "я", "ё", "е", "ю", "и", "я", "ё", "е", "ю"]
# Хэндлер на команду /start

# @router.message(Command(
#     commands=["start"],
# ))
# async def cmd_start(message: Message):
#     await message.answer("Привет! Этот бот делает очень смешные рифмы к словам, введи одно слово и проверь сам!")

def fuuny_rhyme(message: Message) -> str:
    a = message.text
    i = 0
    while (a[i] not in sogl):
        i+=1
        if (i == len(a)):
            return "Долбаеб где гласные"
    if (a[i] in sogl_cool):
        a = "ху" + a[i:]
    else:
        a = "ху" + sogl_cool[sogl.index(a[i])] + a[i+1:]
    return a


@router.message()
async def echo(message: Message):
    await message.answer(fuuny_rhyme(message))
    print(message.text)
    

