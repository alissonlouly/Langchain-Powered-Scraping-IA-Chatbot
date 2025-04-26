# Langchain Scraping IA Agent Chatbot

## Overview

This project is a self-developed Retrieval-Augmented Generation (RAG) application focused on Brazilian culture. It allows users to ask questions and receive concise, relevant answers based on information scraped from the web, primarily the Itaú Cultural Encyclopedia. The application leverages Langchain, web scraping techniques, and a language model to understand and respond to user queries. Interaction is facilitated through a Streamlit chatbot interface.

## Features

- **Ask Questions About Brazilian Culture:** Input your questions about Brazilian culture through a user-friendly chat interface.
- **Intelligent Information Retrieval:** Uses web scraping to gather relevant information from online sources, with a focus on the Itaú Cultural Encyclopedia.
- **Concise and Relevant Answers:** Employs Langchain and a language model to process the scraped data and generate succinct answers tailored to your questions.
- **Streamlit Chat Interface:** Provides an intuitive and interactive chatbot experience for users.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python packages (see `requirements.txt`)
- Ollama installation with a language model (e.g., Llama 3) installed

### Installation

1. Clone the repository:
   ```bash
   git clone [your_repository_url_here]
   cd [your_repository_directory]
   ```

2. Install the necessary packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Download and install a language model using Ollama (if you haven't already): 
    ```bash
    ollama pull llama3 # Or your preferred model
    ```

### Usage
1. Run the Streamlit application: 
```bash
streamlit run app.py # Assuming your main Streamlit file is named app.py
```
2. Interact with the chatbot by typing your questions in the input field and pressing Enter (or the send icon).

### Features In Progress
- [X] Web Chat Interface: A user interface built with Streamlit for easy interaction.
- [X] External Tool Integration (Exa.ai): Incorporating external tools like Exa.ai for broader information retrieval.
- [ ] Use LangGraph for Tool Orchestration: Implement LangGraph to manage the flow and selection of different tools more effectively.
- [ ] Integrate Tavily for Enhanced Search: Add Tavily as a tool to broaden search capabilities and potentially improve result relevance.
- [ ] Implement a Router for Tool Selection: Employ a Langchain Router to dynamically choose the most appropriate tool (e.g., web scraping, Tavily) based on the user's query.
- [ ] Contextual Awareness: Implementing memory to retain conversation history for better context handling.
- [ ] More Sophisticated Question Summarization: Improving the agent's ability to focus on the core entity of the question.

### Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. For significant changes or if you encounter any bugs, please open an issue first to discuss what you would like to change.