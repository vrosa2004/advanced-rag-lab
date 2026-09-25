# 🏷️ Dia 5: Metadata Filtering (Pre-filtering)

A busca vetorial pura é excelente para capturar intenção e contexto, mas falha quando precisamos de restrições exatas (como regras de negócios, limites de preços, ou escopo de departamentos). Neste laboratório, resolvemos esse problema combinando o poder do `pgvector` com filtros SQL tradicionais, implementando a técnica de **Pre-filtering**.

## 🎯 Resumo do Aprendizado

* **Limitações da Busca Semântica:** Vetores calculam similaridade de significado, ignorando regras absolutas. Uma política de TI e uma do RH podem ser escritas de forma muito parecida, o que faria a IA misturar os documentos.
* **Pre-filtering na Prática:** Aplicamos a regra restritiva (o `WHERE` do SQL) *antes* da ordenação por distância vetorial. O banco de dados primeiro isola apenas os documentos do departamento correto e, dentro desse universo reduzido, encontra os mais relevantes semanticamente.
* **Metadados Estruturados:** Em vez de depender apenas do texto e do vetor, adicionamos colunas estruturadas (`departamento` e `tipo`) para classificar a informação. (Nota: Para esquemas mais flexíveis, colunas `JSONB` são frequentemente utilizadas na indústria).

## 🗂️ O que fizemos no Código

Atualizamos nossa arquitetura de repositório e orquestração para suportar metadados:

1. **Nova Tabela e Índices:** Criamos a tabela `documentos_metadata` contendo as colunas `departamento` e `tipo`, além do `embedding` e do texto. Recriamos o índice HNSW para essa nova tabela.
2. **Injeção de Metadados:** Ajustamos o nosso padrão de inserção (`insert_document_2`) para salvar as tags do dicionário de documentos junto com os vetores.
3. **Busca Híbrida (WHERE + pgvector):** Criamos a função `search_similar_2`, que é o coração deste módulo. Nela, o PostgreSQL executa:
   ```sql
   SELECT texto, departamento, tipo, 1 - (embedding <=> %s)
   FROM documentos_metadata 
   WHERE departamento = %s -- PRE-FILTERING ACONTECE AQUI
   ORDER BY embedding <=> %s ASC

   4. **Comparativo (A/B Testing):** No `main.py`, executamos a busca clássica e a busca com filtros de metadados para provar matematicamente como o filtro restringe o escopo de busca antes do cálculo de similaridade.

## 🚀 Como Executar

Certifique-se de estar com o `.env` configurado e a extensão do `pgvector` habilitada no seu Supabase.

```bash
# Certifique-se de ter as dependências instaladas
pip install psycopg2-binary python-dotenv pgvector sentence-transformers

# Execute o pipeline de inserção com metadados e as buscas comparativas
python main.py
```