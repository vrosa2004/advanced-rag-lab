def database_3(conn):
    # Criamos a tabela com a coluna tsvector que se auto-preenche
    query_table = """
        CREATE TABLE IF NOT EXISTS documentos_lexical (
        id SERIAL PRIMARY KEY,
        texto TEXT NOT NULL,
        departamento TEXT NOT NULL,
        tipo TEXT NOT NULL,
        embedding vector(384),
        busca_lexical tsvector GENERATED ALWAYS AS (to_tsvector('portuguese', texto)) STORED
    );
    """
    query_index_vector = """
        CREATE INDEX IF NOT EXISTS documentos_lexical_embedding_hnsw
        ON documentos_lexical
        USING hnsw (embedding vector_cosine_ops)
        WITH (m = 16, ef_construction = 64);
    """
    # NOVO: Índice GIN para busca de texto super rápida
    query_index_lexical = """
        CREATE INDEX IF NOT EXISTS documentos_lexical_fts_idx
        ON documentos_lexical
        USING GIN (busca_lexical);
    """
    with conn.cursor() as cur:
        cur.execute(query_table)
        cur.execute(query_index_vector)
        cur.execute(query_index_lexical)
    conn.commit()

def insert_document_3(conn, texto, departamento, tipo, embedding_array):
    with conn.cursor() as cur:
        check_query = "SELECT texto FROM documentos_lexical WHERE texto = %s LIMIT 1;"
        cur.execute(check_query, (texto,))
        if cur.fetchone() is not None:
            return None
    # Repare que não inserimos nada na coluna 'busca_lexical', o Postgres faz sozinho!
    query = "INSERT INTO documentos_lexical (texto, departamento, tipo, embedding) VALUES (%s, %s, %s, %s);"
    with conn.cursor() as cur:
        cur.execute(query, (texto, departamento, tipo, embedding_array))
    conn.commit()

# --- A NOVA BUSCA LEXICAL ---
def search_lexical(conn, termo_busca, limite=3):
    query = """
        SELECT texto, ts_rank(busca_lexical, plainto_tsquery('portuguese', %s)) AS rank 
        FROM documentos_lexical 
        WHERE busca_lexical @@ plainto_tsquery('portuguese', %s)
        ORDER BY rank DESC 
        LIMIT %s;
    """
    with conn.cursor() as cur:
        # Passamos o termo duas vezes: uma para calcular o rank, outra para o WHERE
        cur.execute(query, (termo_busca, termo_busca, limite))
        return cur.fetchall()

def search_similar(conn, embedding_pergunta, limite=3, ef_search = 40):
    set_ef_query = "SET hnsw.ef_search = %s;"

    query = """
        SELECT texto, 1 - (embedding <=> %s) AS similaridade 
        FROM documentos_lexical
        ORDER BY embedding <=> %s ASC 
        LIMIT %s;   
    """
    
    with conn.cursor() as cur:
        cur.execute(set_ef_query, (ef_search, ))

        cur.execute(query, (embedding_pergunta, embedding_pergunta, limite))
        resultado = cur.fetchall()

    return resultado