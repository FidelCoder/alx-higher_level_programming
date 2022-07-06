#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def main():
    """Main function of module"""
    try:
        my_list = load_from_json_file("add_item.json")
    except Exception:
        my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    main()
