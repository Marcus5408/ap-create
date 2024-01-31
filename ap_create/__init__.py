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
                    values.append(
                        {"location": self.pretty_location(new_path), "key_value": v}
                    )
                elif isinstance(v, dict):
                    helper(v, key, new_path)
                elif isinstance(v, list):
                    for i, item in enumerate(v):
                        if isinstance(item, dict):
                            helper(item, key, new_path + [i])

        helper(self.data, key, [])
        return values

    def pretty_location(self, location):
        pretty_location = ""
        for index, part in enumerate(location):
            if isinstance(part, str):
                pretty_location += f"{part}"
                if (index < len(location) - 1) and (
                    isinstance(location[index + 1], int)
                ):
                    pretty_location += f"[{location[index + 1]}]"
                pretty_location += " -> " if part != location[-1] else ""

        return pretty_location

    def pretty_print(self):
        print(json.dumps(self.data, indent=2))

    def find_all_values_UI(self, key: str):
        values = self.find_all_values(key)
        if values:
            print(f"Found {len(values)} values:")
            for value in values:
                print(f"{'-' * 20}\nLocation: {value['location']}")
                print(f"Value: {value['key_value']}")
        else:
            print(f"No values found for the key '{key}'.")


if __name__ == "__main__":
    print(f"{'*' * 13}\nJSON Explorer\n{'*' * 13}")
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

    if main_menu_choice == "1":
        key = input("Enter the key: ")
        JSONExplorer(data).find_all_values_UI(key)
    elif main_menu_choice == "2":
        explorer = JSONExplorer(data)
        explorer.pretty_print()
    else:
        print("Goodbye!")
        exit()
