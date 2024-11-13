from baseContextPrompt import base_context
from CustomerRequest import CustomerRequest, Base
from DataBaseManager import DatabaseManager
from LLMProcessor import LLMProcessor

def main():
    """
    Main function to simulate handling multiple customer requests using the following steps:
    
    1. Initializes a database connection and creates required tables if they do not exist.
    2. Processes a list of customer questions, which includes:
        - Creating and saving each customer request in the database.
        - Generating a prompt for each question and retrieving a response using LLMProcessor.
        - Updating the database with the generated response and marking the request as completed.
    3. Retrieves and displays all pending requests to verify updates in the database.
    
    Customer questions include both relevant inquiries and an irrelevant one to test the system's ability
    to differentiate and respond appropriately based on available information.
    """
    model_name = "qwen2.5:3b"
    db_manager = DatabaseManager(db_url="sqlite:///customer_requests.db")

    customer_questions = [
        "Hello, I'd like to know how to optimize energy usage in your motor control systems. Could you provide some guidance?",
        "Hi there! What's the recommended maintenance schedule for your digital IoT sensors? Just trying to keep everything running smoothly.",
        "Good afternoon. Can I integrate your automation systems with my existing factory equipment?",
        "Hello, I'm setting up a new system and would like to know how to enable real-time monitoring in the control system.",
        "Hi, could you tell me what safety protocols are included in your control systems to prevent overload or accidents?",
        "Hey, what's the weather like today in New York? Just curious :)"
    ]
    
    llm_processor = LLMProcessor(model_name)
    
    for i, question in enumerate(customer_questions, start=1):
        customer_request = CustomerRequest(customer_id=f"C1234{i}", question=question)
        db_manager.save_request(customer_request)
        print(f"\nSaved Customer Request {i}:")
        print(customer_request)
        
        prompt = llm_processor.build_prompt(question)
        print("\nGenerated Prompt:")
        print(prompt)
        
        response = llm_processor.get_response(question)
        print("\nLLM Response:")
        print(response)
        
        # Use update_status to set the response and mark as 'Completed' before updating the database
        customer_request.update_status(new_status="Completed", response=response)
        
        # Update the request in the database
        db_manager.update_request(customer_request.request_id, customer_request.response, feedback="Completed")
    
    updated_requests = db_manager.get_requests(status="Completed")
    print("\nUpdated Customer Requests in Database:")
    for req in updated_requests:
        print(req)

if __name__ == "__main__":
    main()
