import json
import sys
from functools import reduce
import os

def set_nested_key(d, keys, value):
    """
    Sets a value in a nested dictionary using a list of keys.
    """
    reduce(lambda d, k: d.setdefault(k, {}), keys[:-1], d)[keys[-1]] = value

def update_translations(corrections_json_str, translation_file_path):
    """
    Updates the translation JSON file based on the provided corrections.

    Args:
        corrections_json_str (str): A JSON string with the corrections.
        translation_file_path (str): The path to the en/translation.json file.
    """
    try:
        corrections = json.loads(corrections_json_str)
    except json.JSONDecodeError:
        print("Error: Invalid JSON string provided for corrections.", file=sys.stderr)
        sys.exit(1)

    try:
        with open(translation_file_path, 'r', encoding='utf-8') as f:
            translations = json.load(f)
    except FileNotFoundError:
        print(f"Error: Translation file not found at {translation_file_path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {translation_file_path}", file=sys.stderr)
        sys.exit(1)

    for item in corrections:
        keys = item['location'].split('.')
        suggestion = item['suggestion']
        set_nested_key(translations, keys, suggestion)

    with open(translation_file_path, 'w', encoding='utf-8') as f:
        json.dump(translations, f, indent=2, ensure_ascii=False)

    print(f"Successfully updated {len(corrections)} translation(s) in {translation_file_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # The script is expected to be run from the 'landing-page-i18n' directory
        target_file = 'src/locales/en/translation.json'
        update_translations(sys.argv[1], target_file)