import numpy as np

a = np.array([1, 0])
b = np.array([0, 1])

produto_escalar = np.dot(a, b)

magnetude_a = np.linalg.norm(a)
magnetude_b = np.linalg.norm(b)

cosine_similarity = produto_escalar / (magnetude_a * magnetude_b)

print("Produto escalar é = ", produto_escalar)
print("Magnetude de a é = ", magnetude_a)
print("Magnetude de b é = ", magnetude_b)
print("Cosseno de similiaridade é = ", cosine_similarity)