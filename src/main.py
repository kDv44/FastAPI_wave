from fastapi import FastAPI

from src.database.db_config import engine
from src.user import models, user_router, article_router
from src.blog import blog_router


app = FastAPI()

app.include_router(blog_router.router)
app.include_router(user_router.router)
app.include_router(article_router.router)


models.Base.metadata.create_all(engine)


@app.get("/")
def read_root():
    return "hi \(*^^*)/"
