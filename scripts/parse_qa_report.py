import re
import json
import sys

def parse_qa_report(file_path):
    """
    Parses the QA translation report to extract correction suggestions.

    Args:
        file_path (str): The path to the QA_TRANSLATION_REPORT.md file.

    Returns:
        list: A list of dictionaries, where each dictionary contains the
              'location' (i18n key) and the 'suggestion' (corrected text).
    """
    corrections = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find all problem blocks and capture location and suggestion
        # This is a more robust regex to handle variations in the report
        pattern = re.compile(
            r"### \d+\..*?\n"
            r"**Localização:** `(.*?)`.*?\n"
            r"(?:- \*\*PT:\*\*.*\n- \*\*EN:\*\*.*\n- \*\*Problema:\*\*.*?Deveria ser \"(.*?)\"|.*?Falta informação \"(.*?)\" na versão em inglês|.*?tem texto excessivamente longo.*?sugerida: \"(.*?)\"|.*?Falta tradução de \"mesmo\".*?sugerida: \"(.*?)\"|.*?Falta artigo \"a\" - deveria ser \"(.*?)\")",
            re.DOTALL | re.MULTILINE
        )

        matches = pattern.findall(content)

        for match in matches:
            location = match[0]
            # Find the first non-empty suggestion from the captured groups
            suggestion = next((s for s in match[1:] if s), None)
            if location and suggestion:
                corrections.append({"location": location, "suggestion": suggestion})

    except FileNotFoundError:
        print(f"Error: Report file not found at {file_path}", file=sys.stderr)
        return []

    return corrections

if __name__ == "__main__":
    # The script is expected to be run from the 'landing-page-i18n' directory
    report_path = 'QA_TRANSLATION_REPORT.md'
    parsed_corrections = parse_qa_report(report_path)
    print(json.dumps(parsed_corrections, indent=2))