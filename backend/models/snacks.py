from sqlalchemy import Column, Integer, String, Text, ForeignKey, DECIMAL, Boolean
from sqlalchemy.orm import relationship
from backend.database import Base


class SnacksORM(Base):
    __tablename__ = "snacks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    price = Column(DECIMAL(10,2), nullable=False)
    image = Column(Text)
    is_visible = Column(Boolean, default=True)

    category = relationship("Category", back_populates="snacks")
