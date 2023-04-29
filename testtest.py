ans = input().split()

m1 = int(ans[0])
m2 = int(ans[1])
m3 = int(ans[2])

a = [m1, m2, m3]
a.sort()

if a[2] >= 94 and a[2] <= 727:
    print(a[2])
else:
    print("Error")