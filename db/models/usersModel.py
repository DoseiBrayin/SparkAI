from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.models.paymentModel import Payment
from db.models.personalityModel import Personality
from db.models.genderModel import Gender

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    # ... tus otras columnas ...

    fk_gender = Column(String(1), ForeignKey('gender.id'), nullable=False)
    fk_payment = Column(String(36), ForeignKey('payment.id'))
    fk_personality = Column(String(36), ForeignKey('personality.id'))

    gender = relationship('Gender', back_populates='users')
    payment = relationship('Payment', back_populates='users')
    personality = relationship('Personality', back_populates='users')



    