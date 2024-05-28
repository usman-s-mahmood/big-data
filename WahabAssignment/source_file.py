import json

def read_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def access_and_manipulate_data(data):
    employee_names = [employee['fullName'] for employee in data['Employees']]
    data['Employees'][0]['jobTitle'] = "Senior Developer"
    data['Employees'][1]['jobTitle'] = "Software Engineer"

    return data

def write_json_file(data, filename):
    """Writes a Python dictionary to a new JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file)
    print("Data written to", filename)

def visualize_data(data):
    print("Employees:")
    for employee in data['Employees']:
        print(employee)

def convert_python_to_json(python_object):
    json_string = json.dumps(python_object)
    return json_string

def main():
    # Task 1: Reading JSON Data
    data = read_json_file('employees.json')
    
    # Task 2: Accessing and Manipulating JSON Data
    modified_data = access_and_manipulate_data(data)
    
    # Task 3: Writing JSON Data
    write_json_file(modified_data, 'modified_employees.json')
    
    # Task 6: Visualization
    visualize_data(modified_data)
    
    # Task 7: Convert Python objects into JSON strings
    python_object = {"name": "John", "age": 30}
    json_string = convert_python_to_json(python_object)
    print("JSON string:", json_string)
    
    # Task 8: Reiteration of converting Python objects into JSON strings
    another_python_object = {"name": "Alice", "age": 25}
    another_json_string = convert_python_to_json(another_python_object)
    print("Another JSON string:", another_json_string)

if __name__ == "__main__":
    main()
