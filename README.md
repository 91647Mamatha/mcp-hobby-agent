# MCP Hobby Extraction Agent 🤖

An AI Agent that extracts hobbies and interests of a person from multiple profile sources using MCP (Model Context Protocol) and LLM.

---

# 📌 Overview

This project is an MCP-based AI Agent that identifies and extracts only hobbies/interests from multiple profile sources.

The agent collects contextual profile data from different MCP sources such as:

* LinkedIn
* Instagram
* Facebook
* Resume/CV
* Portfolio/Website
* Wikipedia

The collected data is analyzed using the Groq LLaMA model, and the system returns only hobbies/interests while ignoring unrelated information like:

* Education
* Skills
* Work Experience
* Certifications
* Contact Details

---

# ⚙️ How It Works

1. User provides a person's name.
2. The AI Agent checks the Local MCP for profile data.
3. If data is found, hobbies/interests are extracted and returned.
4. If not found, the agent checks the Browser MCP (Wikipedia).
5. If still not found, the request is directly handled by the LLM.
6. The final response contains only hobbies/interests.

---

# 🏗️ Architecture Flow

```text
User Request (Person Name)
        ↓
      Flask API
        ↓
Check Local MCP
        ↓
Found? → Extract Hobbies → Return Response
        ↓ Not Found
Check Browser MCP (Wikipedia)
        ↓
Found? → Extract Hobbies → Return Response
        ↓ Not Found
LLM Direct Fallback
        ↓
Return Hobbies/Interests
```

---

# 📁 Project Structure

```text
mcp-hobby-agent/
│
├── agent/
│   └── llm_client.py
│
├── mcps/
│   ├── local_mcp.py
│   └── browser_mcp.py
│
├── app.py
├── lambda_handler.py
├── main.tf
├── variables.tf
├── outputs.tf
└── requirements.txt
```

---

# 👤 Personas Implemented

## 1. Private/Fictional Person

Source:

* Local MCP

Mocked sources include:

* LinkedIn
* Instagram
* Facebook
* Resume
* Portfolio

Example:

* Mamatha

---

## 2. Celebrity

Source:

* Browser MCP (Wikipedia API)

Example:

* Elon Musk

---

## 3. Unknown Person (Fallback)

Source:

* LLM Direct Fallback

Example:

* Random unknown names

---

# 🛠️ Tech Stack

* Python
* Flask
* Swagger UI (Flasgger)
* Groq API
* LLaMA 3.1 8B
* AWS Lambda
* API Gateway
* Terraform
* Wikipedia API

---

# 🚀 Local Setup

## 1. Clone Repository

```bash
git clone https://github.com/91647Mamatha/mcp-hobby-agent.git
cd mcp-hobby-agent
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add Groq API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from:

* [https://console.groq.com](https://console.groq.com)

---

## 5. Run the Application

```bash
python app.py
```

---

## 6. Open Swagger UI

```text
http://127.0.0.1:5000/apidocs
```

---

# 🧪 API Testing

Test using:

* Postman
* Swagger UI

---

## Endpoint

```http
POST /get-hobbies
```

---

## Request Body

```json
{
  "name": "Mamatha"
}
```

---

# ✅ Test Cases

## Private Person

```json
{
  "name": "Mamatha"
}
```

---

## Celebrity

```json
{
  "name": "Elon Musk"
}
```

---

## Unknown Person (Fallback)

```json
{
  "name": "Shravya"
}
```

---

# ☁️ AWS Deployment

This project is deployed using:

* AWS Lambda
* API Gateway
* Terraform

---

## Deployment Commands

```bash
terraform init
terraform apply -var="groq_api_key=your_key_here"
```

---

# 🌐 Live API URL

```text
https://hddiyhdl21.execute-api.us-east-1.amazonaws.com/get-hobbies
```

---

# 📤 Sample Output

```json
{
  "name": "Mamatha",
  "source": "Local MCP (Private Person)",
  "hobbies": [
    "Cooking",
    "Traveling",
    "Watching web series and movies",
    "Road trips",
    "Badminton"
  ]
}
```

---

# ✨ Key Features

* MCP-based AI Agent architecture
* Multiple MCP source integration
* Hobby/interest extraction using LLM
* Local MCP + Browser MCP support
* LLM fallback mechanism
* Swagger API documentation
* AWS serverless deployment
* Terraform infrastructure setup
* Clean filtered output

---



This project demonstrates how an AI Agent can use MCP-based contextual data retrieval and LLM intelligence to extract only hobbies/interests from multiple profile sources while filtering unrelated information.
