H,M = map(int,input().split())

EM = M - 45

if EM < 0 :
    M = EM + 60
    H = (H-1)%24
    print(H,M)
else: print(H,EM)
