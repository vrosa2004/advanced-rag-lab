# 🗺️ Dia 4: Índices de Busca Aproximada (HNSW e IVFFlat)

Se você acha que fazer busca vetorial comparando um por um (busca exata) funciona para bancos de dados com milhões de registros, achou errado! Neste laboratório, entramos no mundo da **Busca Aproximada (ANN - Approximate Nearest Neighbor)** no `pgvector` para manter nosso RAG rápido e eficiente sem derreter o servidor.

## 🎯 Resumo do Aprendizado

A busca exata é perfeita, mas não escala. Para resolver isso, implementamos índices vetoriais:

### 1. HNSW (Hierarchical Navigable Small World)
É o padrão ouro da busca vetorial atual. Ele cria um "mapa de caminhos" (grafo) em várias camadas para encontrar os vetores mais próximos pulando etapas.
* **`m`**: Define o número máximo de conexões (caminhos) que cada ponto pode ter.
* **`ef_construction`**: Nível de esforço que o banco de dados faz na hora de **criar** o índice (processamento pesado, feito apenas uma vez na estrutura).
* **`ef_search`**: Nível de esforço na hora da **busca** (dinâmico, aplicado direto na query SQL).

**O Conceito de Trade-off:** Configurar o `ef_search` é um jogo de cobertor curto. Valores altos aumentam a precisão (**Recall**), mas deixam a busca mais demorada (**Latência**). Valores baixos deixam a busca super rápida, mas você pode perder documentos relevantes.

### 2. IVFFlat (Inverted File Flat)
Em vez de um grafo, o IVFFlat usa **Agrupamento (Clustering)**. Ele divide os dados em várias "caixas" (clusters) e, na hora da busca, olha apenas para a caixa que mais se parece com a pergunta.
* **Vantagem:** Consome muito menos memória RAM que o HNSW.
* **Desvantagem:** Você precisa já ter bastante dado no banco *antes* de criar o índice, para que ele saiba como dividir as caixas corretamente.

Neste laboratório, optamos por implementar o **HNSW** para priorizar o recall e a velocidade extrema, já que não temos limitação de memória RAM no momento.

## 🗂️ O que fizemos no Código

Atualizamos o nosso padrão Repository (`repository.py`) do Dia 3 para incluir as otimizações do banco:

1. **Idempotência no Índice:** Adicionamos a criação do índice HNSW usando a cláusula `IF NOT EXISTS` para evitar erros de execução dupla.
2. **Setup do Índice:** Cravamos os parâmetros de construção diretamente na tabela: `WITH (m = 16, ef_construction = 64)`.
3. **Busca Dinâmica:** Passamos a injetar o `ef_search` de forma dinâmica no cursor do psycopg2 (`SET hnsw.ef_search = %s;`) milissegundos antes de executar o `SELECT` da busca vetorial, permitindo controlar o trade-off em tempo de execução.

## 🚀 Como Executar

Certifique-se de estar com o `.env` configurado e o Supabase rodando.

```bash
# Instale as dependências caso ainda não tenha
pip install psycopg2-binary python-dotenv pgvector sentence-transformers

# Execute a orquestração para criar as tabelas, índices e rodar a busca
python main.py