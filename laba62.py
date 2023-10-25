def matr_mult(A, B):
    rows_A = len(A)
    cols_A = len(A[1])
    rows_B = len(B)
    cols_B = len(B[1])
    result = [[0 for row in range(cols_B)] for col in range(rows_A)]

    for s in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[s][j] += A[s][k] * B[k][j]

    return result

def prove(A , b):
    for i in range(len(A)):
        if len(A[i]) > b or len(A[i]) < b:
            return 0
    return 1

matr1 = []
matr2 = []

print("Введите размеры первой матрицы")
try:
    stlb_A = int(input())
    strok_A = int(input())
except:
    print("Это неправильное число емае")
    exit()

if stlb_A <= 0 or strok_A <= 0:
        print("Количество строк или столбцов не может быть таким")
        exit()

print("Введите размеры второй матрицы")
try:
    stlb_B = int(input())
    strok_B = int(input())
except:
    print("Это неправильное число емае")
    exit()

if stlb_B <= 0 or strok_B <= 0:
    print("Количество строк или столбцов не может быть таким")
    exit()

if stlb_A != strok_B:
    print("Такие матрицы нельзя перемножить, так как количество столбцов матрицы А не равно количеству строк матрицы В")
    exit()

print("Введите первую матрицу")
for i in range(stlb_A):
    try: 
        row = input().split() 
        for i in range(len(row)): 
            row[i] = int(row[i]) 
        matr1.append(row)
        if not prove(matr1, strok_A):
            exit()
    except:
        print("Это неправильное число емае")
        exit()

print("Введите вторую матрицу")
for i in range(stlb_B):
    try: 
        row = input().split() 
        for i in range(len(row)): 
            row[i] = int(row[i]) 
        matr2.append(row)
        if not prove(matr2, strok_B):
            exit()
    except:
        print("Это неправильное число емае")
        exit()


print(matr1, matr2)
print(matr_mult(matr1, matr2))
