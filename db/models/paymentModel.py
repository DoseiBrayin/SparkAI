from sqlalchemy import Column, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint

Base = declarative_base()

class Payment(Base):
    __tablename__ = 'payment'

    id = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    card_number = Column(String, nullable=False, unique=True)
    cvv = Column(String(3), nullable=False)
    expiration_date = Column(String(6), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "card_number": self.card_number,
            "cvv": self.cvv,
            "expiration_date": self.expiration_date
        }