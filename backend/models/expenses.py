from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class ExpensesORM(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    snack_id = Column(Integer, ForeignKey("snacks.id", ondelete="CASCADE"), nullable=False)
    ingredient = Column(String(255), unique=True, nullable=False)
    quantity = Column(Integer, nullable=False)

    snack = relationship("Snack")
