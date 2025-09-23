import re
import json
import os

def parse_qa_report(report_path):
    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    corrections = {}
    problem_blocks = re.findall(r'### \d+\. .*?\n\*\*Localização:\*\* `(.*?)`\n- \*\*PT:\*\* (.*?)\n- \*\*EN:\*\* (.*?)\n- \*\*Problema:\*\* (.*?)\n', content, re.DOTALL)

    for location, pt_text, en_text, problem in problem_blocks:
        key = location.strip()
        
        if key == 'hero.cta.secondary':
            corrections[key] = {'en': 'View demonstration'}
        elif key == 'stats.support':
            corrections[key] = {'en': '24/7 Technical support'}
        elif key == 'services.automation.content':
            corrections[key] = {'en': 'We automate repetitive tasks so you can focus on what really matters for your business.'}
        elif key == 'cta.description':
            corrections[key] = {'en': 'Contact us today and discover how we can help you.'}
        elif key == 'cta.button':
            corrections[key] = {'en': 'Talk to a specialist'}
        elif key == 'footer.copyright':
            corrections[key] = {'en': '© 2024 TechSolutions. All rights reserved.'}
        
    return corrections

if __name__ == '__main__':
    # O QA_TRANSLATION_REPORT.md já existe no diretório raiz do projeto
    report_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'QA_TRANSLATION_REPORT.md')
    
    if os.path.exists(report_file_path):
        corrections = parse_qa_report(report_file_path)
        print(json.dumps(corrections, indent=2))
    else:
        print(f"Erro: O arquivo de relatório de QA não foi encontrado em {report_file_path}")


