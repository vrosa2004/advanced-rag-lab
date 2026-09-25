from sentence_transformers import SentenceTransformer
from database import get_connection
import repository

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

conn = get_connection()

try:
    # Prepara o banco de dados
    repository.database_3(conn)

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
    },
    {
        "texto": "O código de aprovação para despesas de viagem acima de mil reais é o ADM-839271.",
        "departamento": "Financeiro",
        "tipo": "politica"
    }
    ]

    for doc in documentos:
        # Transforma o texto em vetor
        vetor = model.encode(doc["texto"]) 
        # Salva no banco via Repository
        repository.insert_document_3(conn, doc["texto"], doc["departamento"], doc["tipo"], vetor)

    # --- HORA DA BUSCA (RETRIEVAL) ---
    pergunta_usuario = { 
        "pergunta": "Qual o código de aprovação para despesas de viagem acima de mil reais?",
        "departamento": "Financeiro"
    }

    vetor_pergunta = model.encode(pergunta_usuario["pergunta"])
    termo_lexical = "ADM-839271"

    print(f"\n=== PROCURANDO PELO CÓDIGO: {termo_lexical} ===")
    
    # 1. Tentando com Vetores (A IA vai sofrer)
    vetor_lexical = model.encode(termo_lexical)
    resultados_vetor = repository.search_similar(conn, vetor_lexical, limite=2, ef_search=30)
    
    print("\n[ BUSCA VETORIAL ]:")
    for i, (conteudo, similaridade) in enumerate(resultados_vetor):
        print(f"{i+1}º Lugar (Score: {similaridade:.4f}) -> {conteudo}")

    # 2. Tentando com Lexical (O motor de texto vai brilhar)
    resultados_texto = repository.search_lexical(conn, termo_lexical, limite=2)
    
    print("\n[ BUSCA LEXICAL (FTS/BM25) ]:")
    for i, (conteudo, rank) in enumerate(resultados_texto):
        print(f"{i+1}º Lugar (Rank: {rank:.4f}) -> {conteudo}")

finally:
    # Garante que a conexão será fechada mesmo se der erro
    conn.close()
    print("\nConexão com banco encerrada.")