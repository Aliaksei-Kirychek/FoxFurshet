from sqlalchemy import (
    Column, Integer, String, Text, DECIMAL, TIMESTAMP, Enum
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database import Base
import enum


class OrderStatusEnum(enum.Enum):
    new = "new"
    processing = "processing"
    delivered = "delivered"
    canceled = "canceled"


class OrdersORM(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_name = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=True)
    address = Column(Text, nullable=False)
    status = Column(Enum(OrderStatusEnum), default=OrderStatusEnum.new, nullable=False)
    delivery_date = Column(TIMESTAMP, nullable=False)
    total_price = Column(DECIMAL(10,2), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    order_items = relationship("OrderItem", back_populates="order")
