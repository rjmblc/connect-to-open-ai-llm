# connect-to-open-ai-llm
# Connect to OpenAI LLM using LangChain

A simple Python project demonstrating how to connect to OpenAI Large Language Models (LLMs) using LangChain and the OpenAI API.

This project shows:

* Loading API keys securely using `.env`
* Connecting to OpenAI models using LangChain
* Sending prompts to the model
* Receiving AI-generated responses

---

# Project Structure

```bash
connect-to-open-ai-llm/
│
├── .env
├── connect_openai.py
├── requirements.txt
└── README.md
```

---

# Technologies Used

* Python
* LangChain
* OpenAI API
* python-dotenv

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/rjmblc/connect-to-open-ai-llm.git
```

## 2. Navigate to Project Directory

```bash
cd connect-to-open-ai-llm
```

## 3. Create Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate virtual environment:

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Setup Environment Variables

Create a `.env` file in the project root directory.

```env
OPENAI_API_KEY=your_openai_api_key
```

Get your API key from:

https://platform.openai.com/api-keys

---

# Sample Code

```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def connect_openai():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    return llm

def fire_prompt(llm):
    response = llm.invoke("What is the capital of India?")
    print(response.content)

if __name__ == "__main__":
    llm = connect_openai()
    fire_prompt(llm)
```

---

# Run the Project

```bash
python connect_openai.py
```

---

# Expected Output

```bash
New Delhi
```

---

# Common Errors

## 1. `NameError: name 'llm' is not defined`

Cause:

* Variable was used before initialization.

Fix:

* Create the LLM object first and pass it into the function.

---

## 2. `RateLimitError` or `insufficient_quota`

Cause:

* OpenAI billing or quota issue.

Fix:

* Add billing details in OpenAI platform
* Generate a new API key
* Verify API usage limits

---

# Learning Outcomes

By completing this project, you will understand:

* How to use OpenAI API with Python
* How LangChain integrates with OpenAI
* Environment variable management
* Basic LLM prompt execution workflow

---

# Future Improvements

* Add Streamlit frontend
* Build chatbot interface
* Add conversation memory
* Create FastAPI backend
* Integrate multiple LLM providers

---

# Author

Rajmohan B

GitHub:
https://github.com/rjmblc

---

# License

This project is for learning and educational purposes.

