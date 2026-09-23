# 🧠 Dia 2: Embeddings na Prática (Profundidade Vetorial)

Este diretório contém o laboratório prático do segundo dia. O objetivo deste exercício é explorar a **profundidade técnica dos vetores** e observar como o modelo de Inteligência Artificial agrupa assuntos semelhantes e separa contextos distintos dentro do espaço multidimensional.

## 🎯 Resumo do Aprendizado

Neste exercício, fomos além da simples busca (Query vs Documento) e criamos uma **Matriz de Similaridade**. Ao comparar todas as frases de uma lista entre si, aprendemos que:

1. **Agrupamento Semântico (Clustering):** Frases com palavras completamente diferentes, mas com a mesma intenção (ex: "Como solicitar férias?" e "Quero pedir minhas férias."), geram vetores que habitam a mesma região no espaço, resultando em scores altos de similaridade.
2. **Separação de Contexto:** Frases de domínios diferentes (ex: "Férias" vs "Servidor Linux") são empurradas para direções opostas pelo modelo, resultando em scores baixos.
3. **Comportamento do Modelo Multilíngue:** O `paraphrase-multilingual-MiniLM-L12-v2` demonstra sua força ao entender perfeitamente o contexto gramatical e a intenção em português, sem se prender a palavras-chave (Busca Lexical).

## 🗂️ Estrutura de Arquivos

```text
dia2/
└── exercicio_1/
    └── main.py       # Análise cruzada de similaridade vetorial entre pares de frases.
```

## 🚀 Como Executar

Certifique-se de estar no ambiente virtual do projeto e ter as bibliotecas instaladas (as mesmas do Dia 1):

```bash
pip install sentence-transformers
```

Para rodar o script de análise vetorial:

```bash
python exercicio_1/main.py
```

### 💡 O que observar na saída do terminal:
Ao rodar o código, preste atenção aos valores gerados. A similaridade entre as frases sobre "férias" será muito próxima de `1.0`, enquanto a comparação entre uma frase de "férias" e uma de "Linux" cairá drasticamente, provando matematicamente que a IA sabe separar os assuntos.