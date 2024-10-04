import os
import json
import string


def load_json_files(directory):
    """Load all JSON files from the given directory."""
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]
    data_list = []

    for file in json_files:
        with open(os.path.join(directory, file), 'r') as f:
            data = json.load(f)
            data_list.append((file, data))

    return data_list


def convert_recipe(recipe_data):
    """Convert the recipe to the desired format with pattern and key mappings."""
    pattern = recipe_data['recipe']
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
            "id": "cgn:automatic_bow",  # Example result
            "count": 1
        }
    }

    return new_recipe


def process_directory(directory):
    """Process all JSON files in the directory and convert their recipes."""
    json_data = load_json_files(directory)

    for file_name, data in json_data:
        if 'recipe' in data:
            converted_recipe = convert_recipe(data)

            # Save the converted recipe to a new JSON file
            output_file = os.path.join(directory, f"converted_{file_name}")
            with open(output_file, 'w') as f:
                json.dump(converted_recipe, f, indent=4)

            print(f"Processed {file_name} -> {output_file}")


# Example usage: Process JSON files in the 'recipes' directory
process_directory('items')
