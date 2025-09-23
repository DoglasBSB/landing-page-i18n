import json
import os
import sys

def update_json_recursively(data, key_parts, value):
    if not key_parts:
        return value
    
    current_key = key_parts[0]
    if isinstance(data, dict):
        if current_key not in data:
            data[current_key] = {}
        data[current_key] = update_json_recursively(data[current_key], key_parts[1:], value)
    else:
        data = {current_key: update_json_recursively({}, key_parts[1:], value)}
    return data

def update_translation_file(file_path, corrections):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}
    except json.JSONDecodeError:
        print(f"Erro ao decodificar JSON em {file_path}. Iniciando com JSON vazio.")
        data = {}

    updated = False
    for key, lang_corrections in corrections.items():
        key_parts = key.split('.')
        for lang, new_value in lang_corrections.items():
            if os.path.basename(os.path.dirname(file_path)) == lang:
                temp_data = json.loads(json.dumps(data))
                updated_data = update_json_recursively(temp_data, key_parts, new_value)
                if updated_data != data:
                    data = updated_data
                    updated = True

    if updated:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Arquivo de tradução {file_path} atualizado com sucesso.")
    else:
        print(f"Nenhuma atualização necessária para {file_path}.")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python update_translations.py <json_corrections>")
        sys.exit(1)

    try:
        corrections_json = sys.argv[1]
        corrections = json.loads(corrections_json)
    except json.JSONDecodeError:
        print("Erro: Argumento JSON inválido.")
        sys.exit(1)

    project_root = os.path.dirname(os.path.dirname(__file__))
    en_file = os.path.join(project_root, 'src', 'locales', 'en', 'translation.json')
    pt_file = os.path.join(project_root, 'src', 'locales', 'pt', 'translation.json')

    update_translation_file(en_file, corrections)
    update_translation_file(pt_file, corrections)


