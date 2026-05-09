from flask import Flask, request, jsonify, redirect
from flasgger import Swagger

from mcps.local_mcp import fetch_local_person
from mcps.browser_mcp import fetch_celebrity_text
from agent.llm_client import extract_from_context, ask_directly

app = Flask(__name__)
swagger = Swagger(app)


# Home → redirect to Swagger UI
@app.route("/")
def home():
    return redirect("/apidocs")


# Main API
@app.route("/get-hobbies", methods=["POST"])
def get_hobbies():
    """
    Get hobbies of a person
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Alex
    responses:
      200:
        description: Hobbies extracted successfully
        schema:
          type: object
          properties:
            name:
              type: string
            source:
              type: string
            hobbies:
              type: string
      404:
        description: Person not found
    """
    data = request.get_json()
    name = data.get("name", "").strip()

    if not name:
        return jsonify({"error": "Name is required"}), 400

    # Try local MCP first (private/fictional person)
    context = fetch_local_person(name)
    print(f"Celebrity context: {context[:100] if context else 'None'}")
    if context:
        hobbies = extract_from_context(context)
        return jsonify({
            "name": name,
            "source": "Local MCP (Private Person)",
            "hobbies": hobbies
        })

    # Try browser MCP (celebrity)
    context = fetch_celebrity_text(name)
    print(f"Celebrity context: {context[:100] if context else 'None'}")
    if context:
        hobbies = extract_from_context(context)
        return jsonify({
            "name": name,
            "source": "Browser MCP (Celebrity)",
            "hobbies": hobbies
        })

    # Fallback: ask LLM directly
    hobbies = ask_directly(name)
    return jsonify({
        "name": name,
        "source": "LLM Direct",
        "hobbies": hobbies
    })


if __name__ == "__main__":
    app.run(debug=True)