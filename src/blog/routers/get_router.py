from fastapi import APIRouter, status, Response

from typing import Optional
from enum import Enum


router = APIRouter(prefix="/blog", tags=["blog"])


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


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
def get_blog(blog_id: str, response: Response):
    return {"message": f"Blog with id - {blog_id}"}


@router.get("/{blog_id}/comments/{comment_id}", tags=["comment"])
def get_comment(
    blog_id: str, comment_id: str, valid: bool = True, username: Optional[str] = None
):
    return {
        "message": f"blog_id: {blog_id}, comment_id: {comment_id}, valid: {valid}, username: {username}"
    }
