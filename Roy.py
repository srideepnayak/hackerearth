L = int(input())
N = int(input())
dimension=[]

while N>0:
    s = input()
    dimension.append(s)
    N-=1

print(dimension)

def check(L,W,H):
    if W < L or H < L:
        print('UPLOAD ANOTHER')
    elif W >= L or H >= L:
        if W == H:
            print('ACCEPTED')
        else:
            print('CROP IT')

for item in dimension:
    i = item.split(' ')
    W = i[0]
    H = i[1]
    check(L,int(W),int(H))




