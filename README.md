MCP Hobby Extraction Agent 
An AI Agent that extracts hobbies and interests of a person from multiple profile sources using MCP (Model Context Protocol) and LLM.

📌 What it does
Given a person's name, the agent:
Searches for their data across multiple sources (LinkedIn, Instagram, Facebook, Resume, Portfolio, Wikipedia)
Sends the data to an LLM (Groq - LLaMA 3)
Returns only hobbies and interests — ignoring education, work experience, and skills


🏗️ Architecture
User Request (name)
        ↓
    Flask API
        ↓
Local MCP → found? → Extract Hobbies → Return
        ↓ not found
Browser MCP (Wikipedia) → found? → Extract Hobbies → Return
        ↓ not found
LLM Direct → Extract Hobbies → Return

📁 Project Structure
mcp-hobby-agent/
├── agent/
│   └── llm_client.py       # Groq LLM integration
├── mcps/
│   ├── local_mcp.py        # Local database (private person)
│   └── browser_mcp.py      # Wikipedia fetch (celebrity)
├── app.py                  # Flask API with Swagger UI
├── lambda_handler.py       # AWS Lambda handler
├── main.tf                 # Terraform - AWS infrastructure
├── variables.tf            # Terraform variables
├── outputs.tf              # Terraform outputs
└── requirements.txt        # Python dependencies

👤 Personas Implemented
PersonTypeSourceMamathaPrivate/Fictional PersonLocal MCP (mocked LinkedIn, Instagram, Facebook, Resume, Portfolio)Elon MuskCelebrityBrowser MCP (Wikipedia API)Unknown NameFallbackLLM Direct

🛠️ Tech Stack

Backend: Python, Flask
API Docs: Swagger UI (Flasgger)
LLM: Groq API (LLaMA 3.1 8B)
Cloud: AWS Lambda + API Gateway
Infrastructure: Terraform
Celebrity Data: Wikipedia API


🚀 Local Setup
1. Clone the repository
bashgit clone https://github.com/91647Mamatha/mcp-hobby-agent.git
cd mcp-hobby-agent
2. Create virtual environment
   python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
  pip install -r requirements.txt
4. Add your Groq API key
Create a .env file:
GROQ_API_KEY=your_groq_api_key_here
Get your free key at: https://console.groq.com
5. Run the app
   python app.py
6. Open Swagger UI
http://127.0.0.1:5000/apidocs

🧪 Testing
Using Postman or Swagger UI

Method: POST
URL: http://127.0.0.1:5000/get-hobbies
Body:

json{
  "name": "Mamatha"
}
Test Cases
Private Person:
json{ "name": "Mamatha" }
Celebrity:
json{ "name": "Elon Musk" }
Unknown (Fallback):
json{ "name": "Shravya" }

☁️ AWS Deployment
Deployed using Terraform on AWS Lambda + API Gateway.
Deploy steps:
bashterraform init
terraform apply -var="groq_api_key=your_key_here"
Live API URL:
https://hddiyhdl21.execute-api.us-east-1.amazonaws.com/get-hobbies

📤 Sample Output
json{
  "name": "Mamatha",
  "source": "Local MCP (Private Person)",
  "hobbies": "1. Cooking\n2. Traveling\n3. Watching web series and movies\n4. Road trips\n5. Badminton"
}
