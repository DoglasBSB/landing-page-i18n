import re
import json
import sys

def update_report_status(corrections_json_str, report_file_path):
    """
    Updates the status of processed items in the QA report from '🔴 Aberto' to '🟢 Resolvido'.

    Args:
        corrections_json_str (str): A JSON string with the corrections that were applied.
        report_file_path (str): The path to the QA_TRANSLATION_REPORT.md file.
    """
    try:
        corrections = json.loads(corrections_json_str)
    except json.JSONDecodeError:
        print("Error: Invalid JSON string provided for corrections.", file=sys.stderr)
        sys.exit(1)

    if not corrections:
        print("No corrections to process. QA report will not be updated.")
        return

    try:
        with open(report_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Report file not found at {report_file_path}", file=sys.stderr)
        sys.exit(1)

    updated_content = content
    updated_count = 0

    for item in corrections:
        location = item['location']
        # Regex to find the block for a given location and replace the status
        # It uses a negative lookahead to ensure it doesn't cross into the next "###" block.
        pattern = re.compile(r"(\*\*Localização:\*\* `{}`(?:.|\n)*?)(- \*\*Status:\*\* 🔴 Aberto)".format(re.escape(location)))
        
        if pattern.search(updated_content):
            updated_content = pattern.sub(r"\1- **Status:** 🟢 Resolvido", updated_content, count=1)
            updated_count += 1

    with open(report_file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

    print(f"Successfully updated status for {updated_count} item(s) in {report_file_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        report_file = 'QA_TRANSLATION_REPORT.md'
        update_report_status(sys.argv[1], report_file)