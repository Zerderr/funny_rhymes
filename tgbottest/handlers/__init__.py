from aiogram import Router

from .penis import router as p_router

router = Router()

router.include_router(p_router)