# 🔍 Dia 6: Busca Lexical (FTS / BM25) vs Busca Vetorial

A busca vetorial (`pgvector`) é revolucionária para entender intenção e contexto, mas tem um "calcanhar de Aquiles": ela é péssima para encontrar palavras-chave exatas, códigos alfanuméricos, IDs e siglas. Neste laboratório, implementamos a **Busca Lexical (Full Text Search - FTS)** nativa do PostgreSQL para cobrir essa fraqueza.

## 🎯 Resumo do Aprendizado

* **O Problema da Vetorização:** Quando pedimos para a IA (modelo de embeddings) vetorizar uma string como `"ADM-839271"`, ela não encontra "significado semântico" e se perde, retornando scores muito baixos ou até associando com documentos completamente errados.
* **A Solução (FTS):** O PostgreSQL possui um motor poderoso para busca de texto. Ele converte nosso texto para um formato otimizado e utiliza algoritmos de ranqueamento clássicos (baseados nos mesmos princípios do **BM25 / TF-IDF**) para encontrar a correspondência exata das palavras.

### ⚙️ Os Motores do Postgres FTS:
* **`tsvector`**: O formato onde o banco guarda as palavras do documento (removendo conectivos inúteis como "de", "para", "o" - as chamadas *stop words*).
* **`tsquery`**: O formato da nossa pergunta, que pesquisa dentro do `tsvector`.
* **`ts_rank`**: A função que dá a "nota" da busca com base na frequência das palavras (não é uma porcentagem de 0 a 1, mas um score absoluto).
* **Índice GIN**: O índice especializado para deixar a busca em `tsvector` super rápida.

## 🗂️ O que fizemos no Código

Atualizamos nosso `repository.py` e `main.py` para colocar as duas buscas numa "batalha":

1. **Coluna Auto-gerada:** Criamos a coluna `busca_lexical` usando `GENERATED ALWAYS AS (to_tsvector('portuguese', texto)) STORED`. Isso significa que o Python não precisa fazer nada: assim que o texto é inserido, o Postgres gera o vetor de texto automaticamente.
2. **Índice GIN:** Adicionamos o índice `documentos_lexical_fts_idx` para otimizar o FTS.
3. **A Batalha (A/B Testing):** No `main.py`, tentamos buscar um código de aprovação financeiro ("ADM-839271") usando Vetores e depois usando Lexical.
   * *Resultado:* A busca vetorial trouxe lixo com baixo score, enquanto a Lexical encontrou o documento com precisão cirúrgica e filtrou o resto.

## 🚀 Como Executar

Certifique-se de estar com o `.env` configurado.

```bash
# Instale as dependências caso ainda não tenha
pip install psycopg2-binary python-dotenv pgvector sentence-transformers

# Execute o teste para ver a diferença entre Lexical e Vetorial
python main.py