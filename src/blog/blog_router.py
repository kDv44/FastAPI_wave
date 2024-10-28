from fastapi import APIRouter, status, Query, Body
from typing import Optional, List
from enum import Enum

from .models import BlogModel


router = APIRouter(prefix="/blog", tags=["blog"])


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


# ===================================================================
# get
# ===================================================================
@router.get(
    "/all",
    summary="Retrieve all blogs",
)
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@router.get("/type/{blog_type}")
def get_blog_type(blog_type: BlogType):
    return {"message": f"Blog type: {blog_type}"}


@router.get(
    "/{blog_id}",
    status_code=status.HTTP_200_OK,
)
def get_blog(blog_id: str):
    return {"message": f"Blog with id - {blog_id}"}


@router.get("/{blog_id}/comments/{comment_id}", tags=["comment"])
def get_comment(
    blog_id: str, comment_id: str, valid: bool = True, username: Optional[str] = None
):
    return {
        "message": f"blog_id: {blog_id}, comment_id: {comment_id}, valid: {valid}, username: {username}"
    }


# ===================================================================
# post
# ===================================================================
@router.post("/new/{blog_id}")
def create_blog(blog: BlogModel, blog_id: int, version: int = 1):
    return {"blog_id": blog_id, "data": blog, "version": version}


@router.post("/new/{blog_id}/comment/{comment_id}")
def create_comment(
    blog: BlogModel,
    blog_id: int,
    comment_title: int = Query(
        None, title="Title of the comment", alias="commentId", deprecated=True
    ),
    content: str = Body(..., max_length=95),
    v: Optional[List[str]] = Query(
        [
            "1.0",
            "1.1",
            "1,2",
        ]
    ),
):
    return {
        "blog": blog,
        "title": comment_title,
        "blog_id": blog_id,
        "version": v,
        "content": content,
    }
