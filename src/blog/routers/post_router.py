from fastapi import APIRouter, Query, Body

from ..models import BlogModel


router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/new/{blog_id}")
def create_blog(blog: BlogModel, blog_id: int, version: int = 1):
    return {"blog_id": blog_id, "data": blog, "version": version}


@router.post("/new/{blog_id}/comment")
def create_comment(
    blog: BlogModel,
    blog_id: int,
    comment_id: int = Query(
        None, title="id of the comment", alias="commentId", deprecated=True
    ),
    content: str = Body(..., max_length=95),
):
    return {
        "blog": blog,
        "blog_id": blog_id,
        "comment_id": comment_id,
        "content": content,
    }
