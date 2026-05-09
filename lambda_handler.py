import json
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from mcps.local_mcp import fetch_local_person
from mcps.browser_mcp import fetch_celebrity_text
from agent.llm_client import extract_from_context, ask_directly

def handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        name = body.get("name", "").strip()

        if not name:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Name is required"})
            }

        # Try local MCP first
        context_data = fetch_local_person(name)
        if context_data:
            hobbies = extract_from_context(context_data)
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "name": name,
                    "source": "Local MCP (Private Person)",
                    "hobbies": hobbies
                })
            }

        # Try browser MCP
        context_data = fetch_celebrity_text(name)
        if context_data:
            hobbies = extract_from_context(context_data)
            return {
                "statusCode": 200,
                "body": json.dumps({
                    "name": name,
                    "source": "Browser MCP (Celebrity)",
                    "hobbies": hobbies
                })
            }

        # Fallback LLM
        hobbies = ask_directly(name)
        return {
            "statusCode": 200,
            "body": json.dumps({
                "name": name,
                "source": "LLM Direct",
                "hobbies": hobbies
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }