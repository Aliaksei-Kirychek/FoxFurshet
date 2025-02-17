from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from backend.database import Base


class OrderItemsORM(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    snack_id = Column(Integer, ForeignKey("snacks.id", ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    subtotal = Column(DECIMAL(10,2), nullable=False)

    order = relationship("Order", back_populates="order_items")
    snack = relationship("Snack")
