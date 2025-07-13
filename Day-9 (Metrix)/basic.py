metrix = [[1,2,3,10],[4,5,6,11],[7,8,9,12]]
rows = len(metrix)
cols = len(metrix[0])
print(f"{rows} X {cols}")
# print all elements
for i in range(0,rows):
    for j in range(0,cols):
        print(metrix[i][j],end=" ")
    print()
# print upper triangle
for i in range (0,rows):
    for j in range(0,cols):
        if j >= i:
            print(metrix[i][j], end=" ")
        else:
            print("*", end = " ")
    print()
# print lower triangle
for i in range (0,rows):
    for j in range(0,cols):
        if j <= i:
            print(metrix[i][j], end=" ")
        else:
            print("*", end = " ")
    print()
# transpose metrix
result = [[0]*rows for _ in range(0,cols)]
print(result)
for i in range (0,rows):
    for j in range(0,cols):
      result[j][i] = metrix[i][j]
print(result)