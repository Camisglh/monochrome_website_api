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


class EnemyCreateSchema(BaseModel):
    name: str


class EnemySchema(EnemyCreateSchema):
    id: int

    class Config:
        orm_mode = True


class CharasterCreateSchema(BaseModel):
    name: str
    quote: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    role: Optional[str] = None
    kills: Optional[int] = None
    category: Optional[List[str]] = []
    allies: Optional[List[str]] = []
    enemies: Optional[List[str]] = []


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


class LocationCreateSchema(BaseModel):
    name: str
    description: Optional[str] = None


class LocalSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    image: Optional[str] = None

    class Config:
        orm_mode = True


class WeaponsCreateSchema(BaseModel):
    name: str
    description: Optional[str] = None


class WeaponsSchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    image: Optional[str] = None

    class Config:
        orm_mode = True
