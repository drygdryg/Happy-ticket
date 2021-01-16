s = str(input())

pre = s.zfill(6)

sum1 = int(pre[0]) + int(pre[1]) + int(pre[2])
sum2 = int(pre[3]) + int(pre[4]) + int(pre[5])

# Alternative implementation of the sum of digits of a number
#n = int(pre)
#sum1 = n // 100000 + n // 10000 % 10 +  n // 1000 % 10
#sum2 = n % 1000 // 100 + n % 100 // 10 + n % 10

if sum1 == sum2:
    print("YES")
else:
    print("NO")
