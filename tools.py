def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"


def search_places(query):
    data = {
        "beach": ["Miami Beach", "Clearwater Beach"],
        "nature": ["Everglades", "Blue Spring"],
        "city": ["New York", "Los Angeles"]
    }
    return data.get(query, ["No results found"])