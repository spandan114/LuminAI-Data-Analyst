from fastapi import APIRouter, Request, Depends
from app.api.controllers import chat_controller
from app.api.validators.chat_validator import AskQuestion, InitiateCinversaction
from app.dependencies.database import get_db
from app.config.db_config import DB

# Instance of APIRouter
chat_router = APIRouter()


@chat_router.post("/ask-question")
async def ask_question(request: Request, body: AskQuestion, db: DB = Depends(get_db)):
    user_id = request.state.user_id
    return await chat_controller.ask_question(user_id, body, db)


@chat_router.post("/initiate-conversations")
async def initiate_convesactions(request: Request, body: InitiateCinversaction, db: DB = Depends(get_db)):
    user_id = request.state.user_id
    return chat_controller.initiate_convesactions(user_id, body, db)


@chat_router.post("/get-conversations")
async def get_conversactions():
    return chat_controller.get_convesactions()


@chat_router.post("/get-conversations-history")
async def get_conversaction_history():
    return chat_controller.get_conversaction_history()
