from sentence_transformers import SentenceTransformer
from database import get_connection
import repository

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

conn = get_connection()

try:
    # Prepara o banco de dados
    repository.setup_database(conn)

    # Nossos documentos fictícios
    documentos = [
        "Para acessar a VPN da empresa, utilize o token gerado no aplicativo Authy.",
        "O refeitório serve almoço das 11:30 às 13:30.",
        "As solicitações de equipamento de TI devem ser feitas via portal de chamados.",
        "Como acessar a rede VPN remotamente.",
        "Quero configurar meu email corporativo no celular.",
        "Como configuro o email no outlook?"
    ]

    for doc in documentos:
        # Valida se o documento já existe no banco
        valida = repository.select_document(conn, doc)
        if valida:
            continue
        else:
            # Transforma o texto em vetor
            vetor = model.encode(doc) 
            # Salva no banco via Repository
            repository.insert_document(conn, doc, vetor)

    # --- HORA DA BUSCA (RETRIEVAL) ---
    pergunta_usuario = "Como configuro o email da empresa no meu celular?"

    vetor_pergunta = model.encode(pergunta_usuario)
    resultados = repository.search_similar(conn, vetor_pergunta, limite=5)

    print("\n=== RESULTADOS DO PGVECTOR ===")
    for i, (conteudo, similaridade) in enumerate(resultados):
        print(f"{i+1}º Lugar (Score: {similaridade:.4f}) -> {conteudo}")

finally:
    # Garante que a conexão será fechada mesmo se der erro
    conn.close()
    print("\nConexão com banco encerrada.")