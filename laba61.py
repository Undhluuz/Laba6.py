print("Введите размеры вектора")
try:
    vector_size = int(input())
except:
    print("Введено неправильное число")
    exit()

vec1 = []
vec2 = []

i = 0
print("Введите первый вектор")
while i < vector_size:
    try:
        vec1.append(int(input()))
        i += 1
    except:
        print("НЕПРАВИЛЬНОЕ ЧИСЛО")
        exit()

i = 0
print("Введите второй вектор")
while i < vector_size:
    try:
        vec2.append(int(input()))
        i += 1
    except:
        print("НЕПРАВИЛЬНОЕ ЧИСЛО")
        exit()

print(vec1)
print(vec2)                

#a · b = ax · bx + ay · by + az · bz

result = sum(map(lambda a, b: a * b, vec1, vec2))
print(result)