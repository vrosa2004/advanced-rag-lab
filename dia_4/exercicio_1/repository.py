def setup_database(conn):
    query = """
    CREATE TABLE IF NOT EXISTS documentos (
        id SERIAL PRIMARY KEY,
        texto TEXT NOT NULL,
        embedding vector(384)
    );
    """
    with conn.cursor() as cur:
        cur.execute(query)
    conn.commit()
    query2 = """
            CREATE INDEX IF NOT EXISTS documentos_embedding_hnsw
            ON documentos
            USING hnsw (embedding vector_cosine_ops)
            WITH (m = 16, ef_construction = 64);
            """
    with conn.cursor() as cur:
        cur.execute(query2)
    conn.commit()

def insert_document(conn, texto, embedding_array):
    with conn.cursor() as cur:
        check_query = "SELECT texto FROM documentos WHERE texto = %s LIMIT 1;"
        cur.execute(check_query, (texto,))
        if cur.fetchone() is not None:
            return None
    query = "INSERT INTO documentos (texto, embedding) VALUES (%s, %s);"
    with conn.cursor() as cur:
        cur.execute(query, (texto, embedding_array))
    conn.commit()

def select_document(conn, texto):
    with conn.cursor() as cur:
        query = "SELECT texto FROM documentos WHERE texto = %s LIMIT 1;"
        cur.execute(query, (texto,))
        return cur.fetchone()

def search_similar(conn, embedding_pergunta, limite=3, ef_search = 40):
    set_ef_query = "SET hnsw.ef_search = %s;"

    query = """
        SELECT texto, 1 - (embedding <=> %s) AS similaridade 
        FROM documentos 
        ORDER BY embedding <=> %s ASC 
        LIMIT %s;   
    """
    
    with conn.cursor() as cur:
        cur.execute(set_ef_query, (ef_search, ))

        cur.execute(query, (embedding_pergunta, embedding_pergunta, limite))
        resultado = cur.fetchall()

    return resultado