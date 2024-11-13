from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from CustomerRequest import CustomerRequest, Base

class DatabaseManager:
    def __init__(self, db_url="sqlite:///customer_requests.db"):
        """
        Initializes the DatabaseManager with a connection to the SQLite database.
        If the database does not already exist, it creates one and sets up tables based on the 
        SQLAlchemy Base metadata.

        Parameters:
            db_url (str): The database URL. Defaults to a SQLite database file named 'customer_requests.db'.
        """

        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)  
        self.Session = sessionmaker(bind=self.engine)

    def save_request(self, customer_request):
        """
        Saves a new customer request to the database.

        Parameters:
            customer_request (CustomerRequest): An instance of the CustomerRequest model containing
                                                the details of the customer request to be saved.

        Raises:
            Exception: If there is an issue with saving the request, it catches the exception,
                       prints an error message, and rolls back the session if needed.
        """

        try:
            session = self.Session()
            session.add(customer_request)
            session.commit()
            print(f"Saved request: {customer_request}")
        except Exception as e:
            print(f"Failed to save request: {e}")
        finally:
            session.close()

    def get_requests(self, status):
        """
        Retrieves all customer requests from the database with the specified status.

        Parameters:
            status (str): The status of customer requests to retrieve (e.g., 'Pending', 'Completed').

        Returns:
            list: A list of CustomerRequest instances with the specified status.
                If no requests with the specified status are found, or if an error occurs, 
                returns an empty list.

        Raises:
            Exception: If there is an issue retrieving requests, it catches the exception 
                    and prints an error message.
        """
        try:
            session = self.Session()
            requests = session.query(CustomerRequest).filter_by(status=status).all()
            return requests
        except Exception as e:
            print(f"Failed to retrieve requests with status '{status}': {e}")
            return []
        finally:
            session.close()


    def update_request(self, request_id, response, feedback=None):
        """
        Updates an existing customer request with a response and changes its status to 'Completed'.
        Optionally, it can also store feedback.

        Parameters:
            request_id (str): The unique ID of the customer request to update.
            response (str): The response to be saved for the customer request.
            feedback (str, optional): Any additional feedback about the request. Defaults to None.

        Raises:
            Exception: If there is an issue updating the request, it catches the exception 
                       and prints an error message.
        """

        try:
            session = self.Session()
            request = session.query(CustomerRequest).filter_by(request_id=request_id).first()
            if request:
                request.response = response
                request.status = 'Completed'
                request.feedback = feedback
                session.commit()
                print(f"Updated request {request_id} with response: {response}")
            else:
                print(f"Request ID {request_id} not found")
        except Exception as e:
            print(f"Failed to update request {request_id}: {e}")
        finally:
            session.close()
