# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    charaster_id = Column(Integer, ForeignKey("charaster.id"))


class Ally(Base):
    __tablename__ = "allies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    charaster_id = Column(Integer, ForeignKey("charaster.id"))


class Enemy(Base):
    __tablename__ = "enemies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    charaster_id = Column(Integer, ForeignKey("charaster.id"))


class Charaster(Base):
    __tablename__ = "charaster"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    image = Column(String, default="images/charaster/no_image.png")
    quote = Column(String, default=None)
    description = Column(String, default=None)
    status = Column(String, default="unknown")
    role = Column(String, default="unknown")
    kills = Column(Integer, default=0)

    category = relationship("Category", backref="charaster")
    allies = relationship("Ally", backref="charaster")
    enemies = relationship("Enemy", backref="charaster")

    def __repr__(self):
        return f"<Charaster(name='{self.name}')>"


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, default=None)

    image = Column(String, default="images/location/no_image.png")


class Weapons(Base):
    __tablename__ = "weapons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, default=None)

    image = Column(String, default="images/weapons/no_image.png")
