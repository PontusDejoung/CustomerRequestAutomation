# Industrial Customer Support System

This project is an **Industrial Customer Support System** designed to manage customer inquiries for an industrial technology company. The system uses a language model to generate responses based on company guidelines and a predefined context about the company's offerings, support philosophy, and interaction guidelines.

## Features

- **Automated Customer Query Handling**: Uses a language model (LLM) to respond to customer inquiries based on company-specific context.
- **Database Management**: SQLAlchemy is used to store and manage customer requests, statuses, and responses.
- **Structured Company Context**: Includes a detailed company profile, offerings, support philosophy, and communication guidelines to ensure consistent responses.
- **Customizable Prompt Generation**: Builds prompts dynamically for each customer question to maintain professionalism and adherence to company guidelines.

## Getting Started

### Prerequisites

- **Python 3.7 or higher**: Make sure Python is installed.
- **Ollama**: The system uses the Ollama language model API. Install Ollama on your system by following the instructions at [https://ollama.com](https://ollama.com).

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up the database**: The system uses SQLite as the default database. When you run the program for the first time, it will automatically create the required tables.

### Usage

1. **Run the main program**:

    ```bash
    python main.py
    ```

   This will:
   - Initialize the database and create necessary tables.
   - Process a series of sample customer questions.
   - Generate and store responses based on the predefined context and guidelines.

2. **Modifying Questions**: You can customize or add more customer questions in the `main.py` file to test additional scenarios.

### Project Structure

- **`baseContextPrompt.py`**: Defines the `base_context` variable, which contains structured information about the company, its offerings, and communication guidelines.
- **`CustomerRequest.py`**: Defines the `CustomerRequest` model for SQLAlchemy, used to manage customer requests in the database.
- **`DatabaseManager.py`**: Handles database operations, including saving, updating, and retrieving customer requests.
- **`LLMProcessor.py`**: Builds prompts and communicates with the language model to generate responses based on customer questions.
- **`main.py`**: The main entry point of the application. It initializes the components, processes customer questions, and manages interactions with the language model and database.

### Example Scenarios

Here are some example customer questions to demonstrate system functionality:

- "How can I optimize energy usage with your motor control systems?"
- "Can I integrate your automation systems with my existing equipment?"
- "What safety protocols are included in your control systems?"
- "What’s the weather like today in New York?" (Example of an irrelevant question)

The system is designed to recognize questions that fall outside the provided company context and respond accordingly, either by referring the customer to further support or providing the relevant information.

### Customization

You can easily modify the **company context** in `baseContextPrompt.py` to reflect your own company's offerings, mission, and support guidelines. Similarly, prompt-building rules in `LLMProcessor.py` can be customized to adjust the response style or structure.

## Requirements

See `requirements.txt` for a full list of dependencies.

## Troubleshooting

- **Database Issues**: Ensure that you have SQLite installed, or modify `DatabaseManager.py` to connect to another SQL database if needed.
- **Language Model Connection Errors**: If the LLM API fails to respond, verify that you have a stable internet connection and that Ollama is correctly installed. Follow installation instructions at [https://ollama.com](https://ollama.com).

## License

This project is licensed under the MIT License.


