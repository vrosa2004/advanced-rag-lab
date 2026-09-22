# Advanced RAG Lab 🔬

Este repositório contém as provas de conceito (PoCs) e experimentações práticas do **Plano Intensivo de Estudos em RAG Avançado**. O objetivo deste laboratório é construir um pipeline de *Retrieval-Augmented Generation* (RAG) estruturado, evoluindo dos fundamentos matemáticos de busca vetorial até a orquestração híbrida com ranqueamento e observabilidade.

## 🗂️ Estrutura do Projeto - Dia 1: Vetores e Embeddings

A primeira etapa do laboratório foca em desmistificar a matemática por trás da busca semântica (Similaridade do Cosseno) e aplicar modelos de *Embeddings* para recuperação de informações (Retrieval) em memória.

```text
advanced-rag-lab/
└── dia1/
    ├── exercicio_1/
    │   └── main.py       # Similaridade do Cosseno com NumPy
    ├── exercicio_2/
    │   └── main.py       # Similaridade do Cosseno em Python Nativo (Math)
    └── exercicio_final/
        └── main.py       # Busca Semântica Real com Sentence-Transformers
```

### 1. Exercício 1: NumPy e Álgebra Linear (`dia1/exercicio_1/main.py`)
Demonstra o cálculo de **Similaridade do Cosseno** utilizando a biblioteca `numpy`. Aborda o uso de produto escalar (`np.dot`) e cálculo de magnitude (`np.linalg.norm`) com processamento vetorizado, simulando a lógica de otimização matemática utilizada por bancos de dados vetoriais em larga escala.

### 2. Exercício 2: A Matemática "Na Mão" (`dia1/exercicio_2/main.py`)
Desconstrói a fórmula matemática do cosseno ($A \cdot B / (\vert{}\vert{}A\vert{}\vert{} \times \vert{}\vert{}B\vert{}\vert{})$) utilizando apenas a biblioteca nativa `math` do Python. O código itera eixo por eixo vetorial para fixar o conceito de aproximação angular no espaço multidimensional.

### 3. Exercício Final: Busca Semântica Real (`dia1/exercicio_final/main.py`)
Implementa um pipeline de *Retrieval* funcional e semântico.
* Converte strings de texto em embeddings de 384 dimensões.
* Utiliza o modelo `paraphrase-multilingual-MiniLM-L12-v2` da HuggingFace para contornar a barreira do idioma e garantir alta precisão no agrupamento de termos em Português.
* Calcula o *score* de similaridade entre a query do usuário e uma base de documentos fictícia, gerando um ranking (Top-K) que prioriza o significado em vez de correspondências de palavras exatas.

## 🚀 Como Executar

### Pré-requisitos
Certifique-se de ter o Python (versão 3.8+) instalado em sua máquina. Recomenda-se a criação de um ambiente virtual (`venv`) para isolar as dependências do laboratório.

### Instalação das Dependências
Execute o comando abaixo no seu terminal para instalar as bibliotecas necessárias para os 3 exercícios:

```bash
pip install numpy sentence-transformers
```

### Rodando os Scripts
Navegue até o diretório do exercício que deseja testar e execute o arquivo principal:

```bash
# Exemplo para rodar a Busca Semântica Real
cd dia1/exercicio_final
python main.py
```

## 🧠 Próximos Passos
O próximo avanço arquitetural do projeto consiste em persistir esses cálculos vetorizados em um **Banco de Dados Vetorial** (utilizando PostgreSQL + `pgvector`), permitindo consultas eficientes em alto volume e a aplicação de filtros lógicos (Metadata Pre-filtering).