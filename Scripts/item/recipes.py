import json
import os
import string


def update(data,file,name):
    """Convert the recipe to the desired format with pattern and key mappings."""
    pattern = data['recipe']
    ingredient_mapping = {}
    new_pattern = []
    letters = iter(string.ascii_uppercase)  # Iterator for generating unique letters A, B, C, etc.

    # Traverse through the pattern to create mappings
    for row in pattern:
        new_row = ""
        for item in row:
            if item == "":
                new_row += " "  # Empty spots in the pattern
            else:
                # If the item is not already in the mapping, add it
                if item not in ingredient_mapping:
                    ingredient_mapping[item] = next(letters)
                new_row += ingredient_mapping[item]
        new_pattern.append(new_row)

    # Create the key mapping
    key_mapping = {value: key if ":" in key else f"minecraft:{key}"
                   for key, value in ingredient_mapping.items()}

    # Create the new recipe format
    new_recipe = {
        "type": "minecraft:crafting_shaped",
        "category": "equipment",
        "pattern": new_pattern,
        "key": key_mapping,
        "result": {
            "id": f"cgn:{name[:-5]}",  # Example result
            "count": 1
        }
    }

def open_item_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r+') as json_file:
                        data = json.load(json_file)
                        if "recipe" in data and isinstance(data["recipe"],list):
                            update(data,json_file,file)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON file {file_path}: {e}")
                except Exception as e:
                    print(f"Error opening file {file_path}: {e}")



def main():
    open_item_files('items')

# Example usage: Process JSON files in the 'recipes' directory
if __name__ == '__main__':
    main()
