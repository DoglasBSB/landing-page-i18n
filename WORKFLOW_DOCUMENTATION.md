# Análise do Fluxo de Automação de Traduções (i18n)

## Visão Geral do Fluxo

O objetivo principal deste sistema é **automatizar a correção de textos (traduções) em inglês** com base em um relatório criado pelo time de Qualidade (QA).

O fluxo funciona da seguinte maneira:
1.  Um analista de QA encontra um erro de tradução no site e documenta o problema e a sugestão de correção no arquivo `QA_TRANSLATION_REPORT.md`.
2.  Ao enviar essa alteração para o repositório no GitHub, uma automação (GitHub Action) é disparada.
3.  A automação lê o relatório, extrai as correções sugeridas e as aplica diretamente no arquivo de tradução em inglês (`en/translation.json`).
4.  Em seguida, a automação faz um "commit" com as correções e:
    *   Se a alteração foi em um **Pull Request**, o commit é adicionado a esse PR para ser revisado por um desenvolvedor.
    *   Se a alteração foi direto na branch **`main`**, um novo Pull Request é criado para que as correções sejam revisadas antes de irem para produção.
5.  Por fim, a automação gera uma versão de preview do site com as correções aplicadas e notifica a equipe no Slack.

---

## Detalhamento dos Arquivos

### 1. `QA_TRANSLATION_REPORT.md` (O Relatório do QA)

Este é o ponto de partida. É um arquivo de texto simples (Markdown) onde o time de QA documenta os problemas de tradução.

-   **Função:** Servir como uma "lista de tarefas" para as correções. É um documento legível por humanos.
-   **Estrutura Crucial para a Automação:**
    -   `**Localização:** \`hero.cta.secondary\``: Indica a "chave" da tradução que precisa ser corrigida. É como um endereço para o texto dentro dos arquivos JSON.
    -   `**Sugestão:** "View demonstration"`: Esta é a parte mais importante. É o texto corrigido que o robô usará para substituir o texto errado.

**Exemplo:**
```markdown
### 1. Hero Section - CTA Secundário
**Localização:** `hero.cta.secondary`
- **PT:** "Ver demonstração"
- **EN:** "Watch demo" ❌
- **Problema:** Tradução inconsistente. Deveria ser "View demonstration" para manter a formalidade
- **Sugestão:** "View demonstration"
- **Status:** 🔴 Aberto
```

---

### 2. Os Scripts Python (O "Robô" Corretor)

Estes dois scripts são o coração da automação. Eles leem o relatório e aplicam as correções.

#### `scripts/parse_qa_report.py`
-   **Função:** Ler o `QA_TRANSLATION_REPORT.md` e extrair as informações importantes.
-   **Como Funciona:** Ele usa expressões regulares (regex) para "escanear" o texto e encontrar todos os blocos de problema. Para cada bloco, ele captura a `Localização` e a `Sugestão`.
-   **Saída:** Ele gera um texto em formato JSON, que é uma lista estruturada das correções a serem feitas. Exemplo:
    ```json
    [{"location": "hero.cta.secondary", "suggestion": "View demonstration"}, {"location": "stats.support", "suggestion": "24/7 Technicall support"}]
    ```

#### `scripts/update_translations.py`
-   **Função:** Pegar a lista de correções (o JSON do script anterior) e aplicá-la no arquivo de tradução.
-   **Como Funciona:**
    1.  Recebe a string JSON como argumento.
    2.  Lê o arquivo `src/locales/en/translation.json`.
    3.  Para cada item da lista, ele navega na estrutura do JSON usando a "chave" (ex: `stats.support`) e substitui o valor antigo pela nova `suggestion`.
    4.  Salva o arquivo `translation.json` com todas as alterações.

---

### 3. Arquivos de Tradução (`translation.json`)

Estes são os arquivos que a sua aplicação React usa para exibir os textos nos diferentes idiomas.

-   **`src/locales/pt/translation.json`**: Contém os textos em português. Geralmente é a fonte de verdade.
-   **`src/locales/en/translation.json`**: Contém os textos em inglês. **Este é o arquivo que o robô modifica automaticamente.**

A estrutura deles é aninhada, permitindo organizar os textos por seções do site, o que corresponde às "chaves" usadas no relatório de QA.

**Exemplo (`en/translation.json`):**
```json
{
  "stats": {
    "projects": "Projects delivered",
    "satisfaction": "Satisfaction rate",
    "support": "24/7 Technicall support"
  }
}
```

---

### 4. `.github/workflows/i18n-automation.yml` (O Orquestrador)

Este é o arquivo que define todo o fluxo de automação no GitHub Actions. Ele diz ao GitHub "quando" e "como" executar os scripts.

-   **`on:` (Gatilho):** Define que a automação deve rodar sempre que houver uma alteração no `QA_TRANSLATION_REPORT.md` ou nos arquivos de tradução, seja em um `push` direto para a `main` ou em um `pull_request`.
-   **`jobs:` e `steps:` (Passos):** Descreve a sequência de ações:
    1.  **Setup**: Prepara o ambiente com Node.js e Python.
    2.  **Parse QA Report**: Executa o `parse_qa_report.py` e salva a saída JSON.
    3.  **Update Translation Files**: Executa o `update_translations.py` usando a saída do passo anterior.
    4.  **Commit and Push / Create Pull Request**:
        *   Se o gatilho foi um PR, ele faz um commit com as correções na branch daquele PR.
        *   Se o gatilho foi um push na `main`, ele cria um novo PR para que as correções sejam revisadas.
    5.  **Build e Deploy**: Instala as dependências do projeto, gera a versão de produção (`build`) e a publica em um link de preview na Netlify.
    6.  **Notificação**: Envia uma mensagem para o Slack com o link do preview e posta um comentário no Pull Request.

---

## Conclusão

Este sistema cria um ciclo de feedback rápido e automatizado, onde o time de QA pode efetivamente "programar" as correções de tradução simplesmente atualizando um arquivo Markdown. Isso reduz a carga de trabalho manual dos desenvolvedores, minimiza erros e integra o processo de i18n diretamente ao fluxo de revisão de código.