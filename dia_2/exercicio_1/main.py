from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

textos = [
    "Como solicitar férias?",
    "Quero pedir minhas férias.",
    "Qual é o procedimento para tirar férias?",
    "Como configurar um servidor Linux?",
    "O servidor precisa ser configurado com Linux."
]

embeddings = model.encode(textos)

for i in range(len(textos)):
    for j in range(i + 1, len(textos)):
        similaridade = util.cos_sim(embeddings[i], embeddings[j])
        print(f"Similaridade entre '{textos[i]}' e '{textos[j]}': {similaridade.item():.4f}")