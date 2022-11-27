def sumMatrice(matrice1:list, matrice2:list):
    try :
        #check row and col lenght
        if len(matrice1) == len(matrice2) :
            for i in range(len(matrice1)) :
                if (len(matrice1[i]) != len(matrice2[i])):
                    raise Exception("MatriceSizeError")

        sum = []

        for i in range(len(matrice1)) :
            sum.append([])
            for j in range(len(matrice1[i])):
                sum[i].append(matrice1[i][j] + matrice2[i][j])

        return sum

    except:
        print("Matrices incompatibles")
        return None


def scalaireMatrice(matrice1:list, scalaire:float) :

    result = []

    for i in range(len(matrice1)):
        result.append([])
        for j in range(len(matrice1[i])):
            result[i].append((matrice1[i][j]*scalaire))
    return result

def multiplyMatrice(matrice1:list, matrice2:list) :

    result = []

    for i in range(len(matrice1)):
        result.append([])
        for k in range(len(matrice1[i])):
            val = 0
            result[i].append([])
            for j in range(len(matrice2[i])):
                val += ((matrice1[i][j]*matrice2[j][k]))
            result[i][k] = val

    return result

A = [[1,2,3],
     [4,-1,2],
     [5,-2,1]]


B = [[2,-1,-2],
     [0,3,2],
     [1,4,3]]

Identity = [[1,0],
            [0,1]]

print(sumMatrice(A, B))
print(scalaireMatrice(A, 2))
print(multiplyMatrice(A, B))
