from datetime import datetime

from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    published_date: datetime

    class Config:
        from_attributes = True


class PostListSchema(BaseModel):
    posts: list[PostSchema]


class PostCreateSchema(BaseModel):
    title: str
    content: str