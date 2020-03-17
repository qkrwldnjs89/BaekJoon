while True:
    s = input()
    s = int(s)
    if s > 100:
        continue
    elif s >= 90:
        print('A')
        break
    elif s >= 80:
        print('B')
        break
    elif s >= 70:
        print('C')
        break
    elif s >= 60:
        print('D')
        break
    else:
        print('F')
        break
