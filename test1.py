s = str(input())

pre = s.zfill(6)

sum1 = int(pre[0]) + int(pre[1]) + int(pre[2])
sum2 = int(pre[3]) + int(pre[4]) + int(pre[5])

if sum1 == sum2:
    print("YES")
else:
    print("NO")
