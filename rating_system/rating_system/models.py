from sqlalchemy import Column, String, Integer

from rating_system.db import Base


class Rating(Base):
    __tablename__ = 'rating'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(80), nullable=False)
    stars = Column(Integer, nullable=False)
