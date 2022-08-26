from sqlalchemy import BigInteger, Column, String

from app.models import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(BigInteger, primary_key=True)
    text = Column(String, nullable=True)
