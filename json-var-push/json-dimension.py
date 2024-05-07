import os
import json

def restructure_json(json_data):
    # Recursive function to traverse and restructure JSON data
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            # If A or B are found, restructure them under variable C
            for key in variables_to_push:
                json_data[nest_variable] = {
                    key: value
                }
                del json_data[key]
            else:
                # Recursively process nested dictionaries
                restructure_json(value)
    elif isinstance(json_data, list):
        for item in json_data:
            # Recursively process list items
            restructure_json(item)

def json_push_dimension():

    # Load input JSON data
    with open(input_file_path, "r") as file:
        json_data = json.load(file)

    # Restructure JSON data
    restructure_json(json_data)

    # Write output JSON data to a new file
    with open(output_file_path, "w") as file:
        json.dump(json_data, file, indent=4)

    print("JSON data restructured and saved to:", output_file_path)

# Example usage:
input_file_path = r"C:\Users\vietdung.truong\Documents\Work\OCI project\Claudiu\infra-mapping.json"  # Path to the input JSON file
output_file_path = r"C:\Users\vietdung.truong\Documents\Work\OCI project\Claudiu\infra-mappingoutput.json"  # Path to the output JSON file
variables_to_push = ['vcn_dns_infra_resolver_destination', 'vcn_infra_subnet_cidr']  # List of variables to push to the next dimension
nest_variable = 'name' #variable to nest the pushed variables

json_push_dimension()