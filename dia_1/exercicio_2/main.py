import math

def cosine_similarity(a, b) :
    dot_product = sum(x * y for x, y in zip(a, b))

    magnitude_a = math.sqrt(sum(x ** 2 for x in a))
    magnitude_b = math.sqrt(sum(x ** 2 for x in b))

    return dot_product / (magnitude_a * magnitude_b)

a = [3, 4]
b = [4, 3]

print(cosine_similarity(a, b))