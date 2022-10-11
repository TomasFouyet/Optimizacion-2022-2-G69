
def determinar_q(f, j, k):
    if f == 1 and j == 1 and k == 1:
        Q_fjk = 1
    else:
        Q_fjk = 0

    if f == 2 and j == 2 and k == 2:
        Q_fjk = 1
    else:
        Q_fjk = 0
    
    if f == 3 and j == 3 and k == 3:
        Q_fjk = 1

    if f == 4 and j == 1 and k == 4:
        Q_fjk = 1

    if f == 5 and j == 2 and k == 5:
        Q_fjk = 1

    return(Q_fjk)

    
x= determinar_q(1,1,1)
print(x)



    