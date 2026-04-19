# tools.py - add this at the bottom

def calculator(expression):
    try:
        return str(eval(expression))
    except:
        return "Invalid expression"

def search_places(query):
    data = {
        "beach": ["Miami Beach", "Clearwater Beach"],
        "nature": ["Everglades", "Blue Spring"],
        "city": ["New York", "Los Angeles"]
    }
    return str(data.get(query, ["No results found"]))

# NEW — describe your tools so Llama 3 understands them
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Use this for ANY math, numbers, or calculation questions. Example: 5+5, 20% of 500, square root of 144",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The math expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_places",
            "description": "Use this for finding places, locations, travel spots, or destinations",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Category of place: beach, nature, or city"
                    }
                },
                "required": ["query"]
            }
        }
    }
]