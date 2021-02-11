listx = [0,1,2,3]
listx[0] = [1,0,1]
listx[1] = [0,0,1]
listx[2] = [1,1,1]
listx[3] = [1,1,1]
temp = []

for i in range(3):
    if 0 in listx[i]:
        pass
    else:
        temp.append(i)

for i in temp:
    for j in range(i, -1, -1):
        print(j,listx[j])
        if j == 0:
            listx[j] = [0,0,0]
        else:
            listx[j] = listx[j-1]

print(listx)