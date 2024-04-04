import os
import json

def push_variables_to_next_dimension(input_json_path, output_json_path, variables_to_push):
    # Load existing JSON data
    with open(input_json_path, 'r') as file:
        existing_data = json.load(file)

    # Create a new dictionary for the updated structure
    updated_data = {}

    # Iterate through the existing data
    for key, value in existing_data.items():
        # If the key is in the list of variables to push
        if key in variables_to_push:
            # Create a new dictionary for the variable and add it to the updated data
            updated_data[key] = {"value": value}
        else:
            # Otherwise, add the key-value pair directly to the updated data
            updated_data[key] = value

    # Write the updated data to a new JSON file
    with open(output_json_path, 'w') as file:
        json.dump(updated_data, file, indent=4)

# Example usage:
input_json_path = 'input.json'  # Path to the input JSON file
output_json_path = 'output.json'  # Path to the output JSON file
variables_to_push = ['name', 'age']  # List of variables to push to the next dimension

push_variables_to_next_dimension(input_json_path, output_json_path, variables_to_push)
