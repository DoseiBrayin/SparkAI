from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from db.models.paymentModel import Payment
from db.models.personalityModel import Personality
from db.models.genderModel import Gender

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    age_range = Column(String(10), nullable=False)
    fk_gender = Column(String(1), ForeignKey(Gender.id), nullable=False)
    fk_payment = Column(String(36), ForeignKey(Payment.id))
    fk_personality = Column(String(36), ForeignKey(Personality.id))

    gender = relationship(Gender, back_populates='users')
    payment = relationship(Payment, back_populates='users')
    personality = relationship(Personality, back_populates='users')

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "age_range": self.age_range,
            "fk_gender": self.gender.to_dict(),
            "fk_payment": self.payment.to_dict(),
            "fk_personality": self.personality.to_dict()
        }


    