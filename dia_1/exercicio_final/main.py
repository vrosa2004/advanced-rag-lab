from sentence_transformers import SentenceTransformer, util

# 1. Carregando o Modelo
# Vamos usar o 'multilingual-MiniLM-L12-v2'. É um modelo pequeno, rápido e excelente para testar embeddings.
# Na primeira execução, ele fará o download do modelo (cerca de 80MB) para a sua máquina.
print("Carregando o modelo de embeddings...")
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# 2. Definindo nossos "Documentos" (o que estaria no seu banco de dados)
documentos = [
    "O setor de TI atualizou a política de senhas. Agora é necessário usar 12 caracteres.",
    "Para solicitar reembolso de viagens, envie a nota fiscal para o financeiro até o dia 5.",
    "A nova máquina de café do refeitório aceita pagamento por aproximação.",
    "A documentação técnica do sistema Atena está disponível no repositório oficial."
]

perguntas = [
    "Como pedir reembolso de uma viagem?",
    "Qual o prazo para enviar uma nota fiscal?",
    "Onde encontro informações sobre o sistema Atena?",
    "Como funciona a política de senhas?"
]

for pergunta in perguntas :
    # 3. Definindo a "Pergunta" do usuário (Query)
    # pergunta = "Como faço para receber de volta o dinheiro gasto com hotel e voo?"

    # 4. Gerando os Embeddings (A Mágica!)
    # O modelo converte cada texto em um vetor real de 384 dimensões
    print("Gerando vetores matemáticos...")
    embedding_pergunta = model.encode(pergunta)
    embeddings_documentos = model.encode(documentos)

    print(f"\nSua pergunta foi transformada em um array de {len(embedding_pergunta)} posições!")
    print(f"Exemplo das 5 primeiras posições: {embedding_pergunta[:5]}\n")

    # 5. Calculando a Similaridade do Cosseno
    # A biblioteca já possui uma função utilitária otimizada para aplicar a fórmula do cosseno
    resultados = util.cos_sim(embedding_pergunta, embeddings_documentos)[0]

    # 6. Ranqueando os Resultados (O início do Retrieval)
    # Vamos parear cada documento com sua nota e ordenar do maior para o menor
    ranking = []
    for i in range(len(documentos)):
        ranking.append({'score': resultados[i].item(), 'texto': documentos[i]})

    ranking_ordenado = sorted(ranking, key=lambda x: x['score'], reverse=True)

    # 7. Exibindo o Top-K
    print(f"=== RESULTADO DA BUSCA SEMÂNTICA === para a pergunta: {pergunta}")
    for i, item in enumerate(ranking_ordenado):
        print(f"{i+1}º Lugar (Score: {item['score']:.4f}) -> {item['texto']}")