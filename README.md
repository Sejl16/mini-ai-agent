# AI Agent

A simple Python-based AI Agent built using OpenRouter with Tool Calling, Memory, Task Management, File Reading, Web Search, and JSON Data Extraction.

## Features

* AI Chat Assistant
* Calculator Tool
* Task Management
  * Add Task
  * List Tasks
* File Reader Tool
* Web Search Tool
* Conversation Memory Last 5
* JSON Data Extraction using `/extract`
* OpenRouter Integration

## Project Structure

```text
project/
│
├── main.py
├── agent.py
├── tools.py
├── memory.py
├── config.py
├── .env
└── README.md
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd project-name
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create .env File

```env
OPENROUTER_API_KEY=your_api_key_here
```

## Run Project

```bash
python main.py
```

## Available Commands

### Calculator

```text
calculator 25*8
```

### Add Task

```text
add task Learn Python
```

### List Tasks

```text
list tasks
```

### Read File

```text
read file notes.txt
```

### Web Search

```text
search latest AI news
```

### Extract JSON

```text
/extract My name is Yash. I am 20 years old and live in Surat.
```

Example Output:

```json
{
  "name": "Rahul",
  "age": 22,
  "city": "Surat"
}
```

## Technologies Used

* Python
* OpenRouter API
* OpenAI SDK
* JSON
* dotenv

## Author

Developed as a learning project for building AI Agents using Python and Tool Calling.
