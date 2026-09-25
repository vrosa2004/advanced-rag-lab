import os
import psycopg2
from dotenv import load_dotenv
from pgvector.psycopg2 import register_vector

load_dotenv()

def get_connection():
    """Cria a conexão com o Supabase e registra o tipo vector."""
    db_url = os.getenv("DATABASE_URL")
    conn = psycopg2.connect(db_url)
    
    # Ativa a extensão no banco caso seja a primeira vez
    with conn.cursor() as cur:
        cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    conn.commit()
    
    # Ensina o Python a converter arrays numpy para vetores do Postgres
    register_vector(conn)
    return conn