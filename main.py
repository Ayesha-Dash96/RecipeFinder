import requests

def searchByIngredients(ingredients):
    # Spoonacular API endpoint for recipe search
    url = "https://api.spoonacular.com/recipes/findByIngredients"

    # API parameters
    params = {
        "ingredients": ",".join(ingredients),
        "number": 5,
        "apiKey": "7b9b8c4e63a44ba3b175113d93725123"  # replace it with your api key
    }

    try:
        # Send GET request to the API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for any HTTP errors

        # Parse JSON response
        recipes = response.json()

        # Print information about each recipe
        for recipe in recipes:
            print(f"Recipe: {recipe['title']}")
            print(f"Missing ingredients: {recipe['missedIngredientCount']}")
            print(f"Used ingredients: {recipe['usedIngredientCount']}")
            print(f"Likes: {recipe['likes']}")
            # print(f"Link: {recipe['sourceUrl']}")
            print()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage: search recipes using provided ingredients

    ingredients = input("Enter the ingredients separated by comma :").strip().split(",")
    searchByIngredients(ingredients)
