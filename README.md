# TechSolutions Landing Page - i18n Implementation

## 📋 Descrição do Projeto

Landing page responsiva da TechSolutions com sistema de internacionalização (i18n) implementado usando React e react-i18next. O projeto inclui traduções para português (PT) e inglês (EN) com quebras intencionais para testes de QA.

## 🚀 Tecnologias Utilizadas

- **React 19.1.0** - Framework frontend
- **Vite** - Build tool e dev server
- **Tailwind CSS** - Framework CSS
- **shadcn/ui** - Componentes UI
- **react-i18next** - Sistema de internacionalização
- **Lucide React** - Ícones

## 🌐 Funcionalidades de i18n

- ✅ Detecção automática de idioma do navegador
- ✅ Persistência da escolha de idioma no localStorage
- ✅ Alternância dinâmica entre PT/EN
- ✅ Estrutura de arquivos de tradução organizados
- ✅ Fallback para português como idioma padrão

## 📁 Estrutura de Arquivos

```
src/
├── locales/
│   ├── pt/
│   │   └── translation.json    # Traduções em português
│   └── en/
│       └── translation.json    # Traduções em inglês (com quebras)
├── components/
│   └── ui/                     # Componentes shadcn/ui
├── i18n.js                     # Configuração do i18next
├── App.jsx                     # Componente principal
└── main.jsx                    # Entry point
```

## 🐛 Problemas de QA Identificados

O arquivo `QA_TRANSLATION_REPORT.md` contém uma lista detalhada dos problemas de tradução identificados durante os testes, incluindo:

- Inconsistências terminológicas
- Textos muito longos que podem quebrar o layout
- Traduções incompletas
- Problemas gramaticais

## 🔧 Como Executar

### Desenvolvimento
```bash
# Instalar dependências
pnpm install

# Executar em modo desenvolvimento
pnpm run dev
```

### Build para Produção
```bash
# Gerar build otimizado
pnpm run build

# Preview do build
pnpm run preview
```

## 🌍 Como Usar o Sistema de Tradução

1. **Alternância de Idioma**: Clique no botão PT/EN no header
2. **Detecção Automática**: O sistema detecta o idioma do navegador
3. **Persistência**: A escolha é salva no localStorage

## 📝 Adicionando Novas Traduções

1. Adicione a chave no arquivo `src/locales/pt/translation.json`
2. Adicione a tradução correspondente em `src/locales/en/translation.json`
3. Use `t('chave.da.traducao')` no componente React

Exemplo:
```json
// pt/translation.json
{
  "nova": {
    "secao": "Texto em português"
  }
}

// en/translation.json
{
  "nova": {
    "secao": "Text in English"
  }
}
```

```jsx
// No componente React
import { useTranslation } from 'react-i18next';

function MeuComponente() {
  const { t } = useTranslation();
  return <h1>{t('nova.secao')}</h1>;
}
```

## 🔍 Processo de QA

1. **Teste Visual**: Verificar layout em ambos os idiomas
2. **Teste de Conteúdo**: Validar traduções e terminologia
3. **Teste de Responsividade**: Verificar em diferentes tamanhos de tela
4. **Teste de Funcionalidade**: Validar alternância de idiomas
5. **Teste de Persistência**: Verificar se a escolha é mantida

## 📊 Métricas de Build

- **Bundle Size**: ~286KB (gzipped: ~90KB)
- **CSS Size**: ~97KB (gzipped: ~15KB)
- **Build Time**: ~3s

## 🚀 Deploy

O projeto está configurado para deploy automático. O build é gerado na pasta `dist/` e pode ser servido por qualquer servidor de arquivos estáticos.

---

**Desenvolvido para demonstração de fluxo de trabalho de QA/i18n**

