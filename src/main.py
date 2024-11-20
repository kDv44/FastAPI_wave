from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse

from src.user.routers import article_router, user_router
from src.product.routers import product_routers

from src.database.db_config import engine
from src.exeptions import StoryException
from src.user import models
from src.blog import blog_router


app = FastAPI()

app.include_router(blog_router.router)
app.include_router(user_router.router)
app.include_router(article_router.router)
app.include_router(product_routers.router)


models.Base.metadata.create_all(engine)


@app.get("/")
def read_root():
    return "hi \(*^^*)/"


@app.exception_handler(StoryException)
def story_exception_header(request: Request, exc: StoryException):
    return JSONResponse(status_code=418, content={"detail": exc.name})


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)
