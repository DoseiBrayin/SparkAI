from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Gender(Base):
    __tablename__ = 'gender'

    id = Column(String(1), primary_key=True)
    name = Column(String, nullable=False)

    users = relationship('User', back_populates='gender')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
class Payment(Base):
    __tablename__ = 'payment'

    id = Column(String(36), primary_key=True)
    name = Column(String(100), nullable=False)
    card_number = Column(String, nullable=False, unique=True)
    cvv = Column(String(3), nullable=False)
    expiration_date = Column(String(6), nullable=False)
    
    users = relationship('User', back_populates='payment')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "card_number": self.card_number,
            "cvv": self.cvv,
            "expiration_date": self.expiration_date
        }
    
class Personality(Base):
    __tablename__ = 'personality'

    id = Column(String(36), primary_key=True)
    type = Column(String(100), nullable=False)

    users = relationship('User', back_populates='personality')

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type
        }

class User(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    age_range = Column(String(10), nullable=False)
    fk_gender = Column(String(1), ForeignKey('gender.id'), nullable=False)
    fk_payment = Column(String(36), ForeignKey('payment.id'))
    fk_personality = Column(String(36), ForeignKey('personality.id'))

    gender = relationship('Gender', back_populates='users')
    payment = relationship('Payment', back_populates='users')
    personality = relationship('Personality', back_populates='users')

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "age_range": self.age_range,
            "gender": self.gender.to_dict() if self.gender else None,
            "payment": self.payment.to_dict() if self.payment else None,
            "personality": self.personality.to_dict() if self.personality else None
        }
    


    