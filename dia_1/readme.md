# 🧮 Dia 1: Vetores e Embeddings

Este diretório contém os laboratórios práticos do primeiro dia de estudos em RAG Avançado. O objetivo aqui é desmistificar a matemática da **Similaridade do Cosseno** e aplicá-la na recuperação semântica de textos utilizando IA.

## 🎯 Resumo do Aprendizado

1. **A Matemática da Busca:** O computador não compara palavras exatas, mas sim a distância e o ângulo entre pontos (vetores) em um espaço multidimensional.
2. **Similaridade do Cosseno:** Mede o ângulo entre dois vetores. 
   * A fórmula é: `(Produto Escalar) / (Magnitude A * Magnitude B)`. 
   * Scores próximos a `1.0` indicam alta similaridade (mesmo significado). Scores próximos a `0` ou negativos indicam assuntos não relacionados.
3. **Embeddings:** A conversão de frases reais em arrays numéricos através de modelos de Inteligência Artificial.
4. **O Fator Idioma:** Modelos treinados apenas em inglês geram falsos positivos em português. A utilização de modelos multilíngues (como o `paraphrase-multilingual-MiniLM-L12-v2`) é crucial para precisão no nosso idioma.

## 🗂️ Estrutura de Arquivos

```text
dia1/
├── exercicio_1/
│   └── main.py       # Cálculo otimizado de Similaridade do Cosseno usando NumPy.
├── exercicio_2/
│   └── main.py       # Desconstrução da matemática do cosseno usando Python nativo (math).
└── exercicio_final/
    └── main.py       # Busca Semântica Real (Retrieval) com Sentence-Transformers.
```

## 🚀 Como Executar

Certifique-se de estar no ambiente virtual do projeto e ter as bibliotecas instaladas:

```bash
pip install numpy sentence-transformers
```

Para rodar os testes matemáticos:

```bash
# Executa a versão com NumPy
python exercicio_1/main.py

# Executa a versão desconstruída "na mão"
python exercicio_2/main.py
```

Para rodar o simulador de Busca Semântica Real (Onde a IA converte a pergunta e os documentos, avaliando e ranqueando a resposta):

```bash
python exercicio_final/main.py
```

*Nota: Na primeira execução do exercicio_final, o Python fará o download do modelo da HuggingFace para a sua máquina local (aprox. 80MB).*
