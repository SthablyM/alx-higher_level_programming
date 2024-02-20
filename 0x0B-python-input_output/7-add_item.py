#!/usr/bin/python3
"""Add all arguments to a python"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('4-from_json_string').from_json_string

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
        items.extend(sys.argv[1:])
        save_to_json_file(items, "add_items.json")
