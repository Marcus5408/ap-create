import random
import json

class JSONExplorer:
    def __init__(self, data):
        self.data = data

    def find_all_values(self, key):
        values = []

        def helper(data, key, path):
            for k, v in data.items():
                new_path = path + [k]
                if k == key:
                    values.append({"location": new_path, "key_value": v})
                elif isinstance(v, dict):
                    helper(v, key, new_path)
                elif isinstance(v, list):
                    for i, item in enumerate(v):
                        if isinstance(item, dict):
                            helper(item, key, new_path + [i])

        helper(self.data, key, [])
        return values

    def pretty_print(self):
        """Pretty-prints the JSON data."""
        print(json.dumps(self.data, indent=4))


if __name__ == "__main__":
    print(f"{'*' * 12}\JSON Explorer\n{'*' * 12}")
    file_name = input("Enter the name of the json file (including the extension): ")
    try:
        with open(f"{__file__.replace('__init__.py', '')}{file_name}", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(
            "Could not find the file. Please make sure the file is in the same directory as this script."
        )
        exit()
    else:
        print(f"'{file_name}' loaded successfully.")

    print("What would you like to do?")
    menu_options = {
        "1": "Find all values of a key",
        "2": "Pretty-print the JSON data",
        "3": "Exit the program",
    }

    for key, value in menu_options.items():
        print(f"[{key}] {value}")

    main_menu_choice = input("Enter your choice: ")
    while main_menu_choice not in menu_options.keys():
        print("Invalid choice. Please try again.")
        main_menu_choice = input("Enter your choice: ")
