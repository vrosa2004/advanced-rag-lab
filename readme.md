# 🔬 Advanced RAG Lab

Repositório dedicado ao laboratório prático e estudo intensivo de **Retrieval-Augmented Generation (RAG) Avançado**. O objetivo deste projeto é construir, etapa por etapa, um ecossistema completo de recuperação de informação, passando por buscas semânticas, lexicais, ranqueamento, geração embasada e observabilidade.

## 🏗️ Arquitetura do Pipeline

O fluxo de processamento de ponta a ponta implementado neste laboratório segue a arquitetura abaixo:

```text
QUERY → EMBEDDING → [pgvector + BM25] → RRF → RERANKER → CONTEXT → LLM → RESPOSTA
                               ↓                                      ↓
                           Retrieval                              Generation
                               ↓                                      ↓
                             Ragas                                 Langfuse
```
## 🛠️ Stack Tecnológica

* **Busca e Vetorização:** `numpy`, `sentence-transformers`, PostgreSQL com extensão `pgvector`.
* **Busca Lexical:** Algoritmo BM25 e Full Text Search.
* **Reranking:** Modelos Cross-Encoder e bi-encoder.
* **Orquestração de LLMs:** LiteLLM (Proxy server).
* **Avaliação de RAG:** Framework `ragas` (Context Precision, Context Recall, Faithfulness, Answer Relevance).
* **Observabilidade:** Plataforma `langfuse` para tracing, latência, tokens e custos.

## 🗺️ Índice de Estudos (Roadmap)

Este projeto está dividido em pequenos módulos diários. Cada pasta contém o seu próprio `README.md` com os conceitos aprendidos e os comandos de execução dos scripts.

### Semana 1: Retrieval (Vector, Busca Lexical e Metadados)
* [x] Dia 1: Vetores e embeddings.
* [x] Dia 2: Embeddings na prática.
* [x] Dia 3: PostgreSQL + pgvector.
* [ ] Dia 4: Índices de busca aproximada (HNSW e IVFFlat).
* [ ] Dia 5: Metadata filtering (Pre-filtering e Post-filtering).
* [ ] Dia 6: BM25 e busca lexical.
* [ ] Dia 7: Mini projeto de retrieval paralelo.

### Semana 2: Hybrid Search, Reranking e Generation
* [ ] Dia 8: Algoritmo RRF (Reciprocal Rank Fusion).
* [ ] Dia 9: Hybrid Search na prática.
* [ ] Dia 10: Bi-encoder vs Cross-encoder e Reranking.
* [ ] Dia 11: Reranker na prática (Refinamento de candidatos).
* [ ] Dia 12: Grounded Generation com citações.
* [ ] Dia 13: LiteLLM proxy e roteamento.
* [ ] Dia 14: RAG completo (Integração ponta a ponta).

### Semana 3: Avaliação e Observabilidade
* [ ] Dia 15: Métricas RAG teóricas.
* [ ] Dia 16: Avaliação com LLM-as-a-Judge usando Ragas[cite: 5].
* [ ] Dia 17: Instrumentação e traces com Langfuse[cite: 5].
* [ ] Dia 18: Concorrência com Async/Await e revisão final[cite: 5].

## 🚀 Como Iniciar o Projeto Base

Clone este repositório e instale as dependências globais na sua máquina:

```bash
git clone [https://github.com/SEU_USUARIO/advanced-rag-lab.git](https://github.com/SEU_USUARIO/advanced-rag-lab.git)
cd advanced-rag-lab

# Crie um ambiente virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
