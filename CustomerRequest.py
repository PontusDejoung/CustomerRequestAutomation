from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid

Base = declarative_base()

class CustomerRequest(Base):
    """
    Represents a customer request in the database. Each request includes information
    such as the customer ID, the question asked, the status of the request, the response,
    any additional feedback, and the date of creation.
    """
    __tablename__ = 'customer_requests'
    request_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = Column(String, nullable=False)
    question = Column(Text, nullable=False)
    status = Column(String, default='Pending')
    response = Column(Text)
    feedback = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    

    def update_status(self, new_status, response=None):
        """
        Updates the status and response of the customer request.
        
        Parameters:
            new_status (str): The new status for the request (e.g., 'Completed', 'Pending').
            response (str, optional): The response text to update for the request.
        """
        self.status = new_status
        self.response = response

    def __str__(self):
        """
        Returns a string representation of the CustomerRequest instance, 
        displaying the request ID, question, and status.
        
        Returns:
            str: Formatted string with key details of the request.
        """
        return f"Request ID: {self.request_id}, Question: {self.question}, Status: {self.status}"
