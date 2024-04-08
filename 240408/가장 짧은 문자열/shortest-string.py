n = input()
n1 = input()
n2 = input()
nn = len(n)
nn1 = len(n1)
nn2 = len(n2)
if nn == nn1:
    nn = nn1
elif nn == nn2:
    nn = nn2
elif nn1 == nn2:
    nn1 = nn2
if nn > nn1 and nn1 > nn2:
    print(nn-nn2)
elif nn1 > nn and nn > nn2:
    print(nn1-nn2)
elif nn2 > nn and nn > nn1:
    print(nn2-nn1)
elif nn > nn2 and nn2 > nn1:
    print(nn-nn1)
elif nn1 > nn2 and nn2 > nn:
    print(nn1-nn)
else:
    print(nn2-nn)