from typing import Optional, List, Union, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class CategoryCreateSchema(BaseModel):
    name: str


class CategorySchema(CategoryCreateSchema):
    id: int

    class Config:
        orm_mode = True


class AllyCreateSchema(BaseModel):
    name: str


class AllySchema(AllyCreateSchema):
    id: int

    class Config:
        orm_mode = True


class EnemySchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CharasterSchema(BaseModel):
    id: int
    name: str
    image: Optional[str] = None
    quote: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    role: Optional[str] = None
    kills: Optional[int] = None
    category: Optional[str] = None
    allies: Optional[List[str]] = []
    enemies: Optional[List[str]] = []

    class Config:
        orm_mode = True


class LocalSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    image: Optional[str] = None

    class Config:
        orm_mode = True


class WeaponsSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    image: Optional[str] = None

    class Config:
        orm_mode = True
