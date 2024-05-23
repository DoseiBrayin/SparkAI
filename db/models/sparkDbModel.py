from sqlalchemy import Column, String, ForeignKey, Boolean, Date
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
    token = Column(String(100), nullable=False)
    state = Column(Boolean, nullable=False)
    date = Column(Date, nullable=False)
    
    users = relationship('User', back_populates='payment')

    def to_dict(self):
        return {
            "id": self.id,
            "token": self.token,
            "state": self.state,
            "expiration_date": self.date
        }
    
class Personality(Base):
    """
    Represents a personality in the database.
    """

    __tablename__ = 'personality'

    id = Column(String(36), primary_key=True)
    type = Column(String(100), nullable=False)

    users = relationship('User', back_populates='personality')

    def to_dict(self):
        """
        Converts the Personality object to a dictionary.

        Returns:
            dict: A dictionary representation of the Personality object.
        """
        return {
            "id": self.id,
            "type": self.type
        }

class User(Base):
    """
    Represents a user in the system.

    Attributes:
        id (str): The unique identifier of the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        age_range (str): The age range of the user.
        fk_gender (str): The foreign key referencing the gender of the user.
        fk_payment (str): The foreign key referencing the payment information of the user.
        fk_personality (str): The foreign key referencing the personality information of the user.
        gender (Gender): The gender of the user.
        payment (Payment): The payment information of the user.
        personality (Personality): The personality information of the user.
    """

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
        """
        Converts the User object to a dictionary.

        Returns:
            dict: A dictionary representation of the User object.
        """
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "age_range": self.age_range,
            "gender": self.gender.to_dict() if self.gender else None,
            "payment": self.payment.to_dict() if self.payment else None,
            "personality": self.personality.to_dict() if self.personality else None
        }
    


    