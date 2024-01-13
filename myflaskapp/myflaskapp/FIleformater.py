import json

def reformat_json(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    reformatted_data = {}
    
    for item in data:
        category = item['Table']
        aspect = {
            "ID": item['ID'],
            "Aspect": item['Column'],
            "Description": item['Description']
        }

        if category not in reformatted_data:
            reformatted_data[category] = []

        reformatted_data[category].append(aspect)

    with open(output_file, 'w') as file:
        json.dump(reformatted_data, file, indent=4)

# Usage example
input_file_path = 'myflaskapp\myflaskapp\world_building_elements.json'  # Replace with your input file path
output_file_path = 'myflaskapp\world_building_elements.json'  # Replace with your desired output file path
reformat_json(input_file_path, output_file_path)
