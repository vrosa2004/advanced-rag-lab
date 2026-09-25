from sentence_transformers import SentenceTransformer
from database import get_connection
import repository

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

conn = get_connection()

try:
    # Prepara o banco de dados
    #repository.setup_database(conn)
    repository.database_2(conn)

    # Nossos documentos fictícios
    documentos = [
    {
        "texto": "Para solicitar férias, o funcionário deve acessar o portal de RH.",
        "departamento": "RH",
        "tipo": "politica"
    },
    {
        "texto": "O pagamento de reembolso deve ser solicitado ao setor financeiro.",
        "departamento": "Financeiro",
        "tipo": "politica"
    },
    {
        "texto": "Para acessar a VPN da empresa, utilize o token gerado no aplicativo Authy.",
        "departamento": "TI",
        "tipo": "manual"
    },
    {
        "texto": "Para configurar o email corporativo no celular, utilize o Outlook.",
        "departamento": "TI",
        "tipo": "manual"
    },
    {
        "texto": "Os benefícios dos funcionários estão disponíveis no portal de RH.",
        "departamento": "RH",
        "tipo": "beneficios"
    }
    ]

    for doc in documentos:
        # Transforma o texto em vetor
        vetor = model.encode(doc["texto"]) 
        # Salva no banco via Repository
        repository.insert_document_2(conn, doc["texto"], doc["departamento"], doc["tipo"], vetor)

    # --- HORA DA BUSCA (RETRIEVAL) ---
    pergunta_usuario = { 
        "pergunta": "Como faço para solicitar férias?",
        "departamento": "RH"
    }

    vetor_pergunta = model.encode(pergunta_usuario["pergunta"])
    resultados = repository.search_similar(conn, vetor_pergunta, limite=5, ef_search=30)
    resultados_2 = repository.search_similar_2(conn, vetor_pergunta, pergunta_usuario["departamento"], limite=5, ef_search=30)

    print("\n=== RESULTADOS DO PGVECTOR ===")
    for i, (conteudo, similaridade) in enumerate(resultados):
        print(f"{i+1}º Lugar (Score: {similaridade:.4f}) -> {conteudo}")

    print("\n=== RESULTADOS DO PGVECTOR COM METADADOS ===")
    for i, (conteudo, departamento, tipo, similaridade) in enumerate(resultados_2):
        print(f"{i+1}º Lugar (Score: {similaridade:.4f}) -> {conteudo} ({departamento} - {tipo})")

finally:
    # Garante que a conexão será fechada mesmo se der erro
    conn.close()
    print("\nConexão com banco encerrada.")