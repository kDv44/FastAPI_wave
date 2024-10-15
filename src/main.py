from fastapi import FastAPI
from blog.routers import get_router, post_router


app = FastAPI()

app.include_router(get_router.router)
app.include_router(post_router.router)


@app.get("/")
def read_root():
    return "hi \(*^^*)/"
