L = int(input())
N = int(input())

dimension = [input() for i in range(0,N)]

for item in dimension:
    W = int(item.split(' ')[0])
    H = int(item.split(' ')[1])
    if W < L or H < L: print('UPLOAD ANOTHER')
    elif W == H:print('ACCEPTED')
    else: print('CROP IT')
   
