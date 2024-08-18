f = [1,2,3,2,2]

basket = 0
fruit1, fruit2 = None, None
count1, count2 = 0, 0
l = 0
maxx = 0

for r in range(len(f)):
    if fruit1 is None or f[r] == fruit1:
        fruit1 = f[r]
        count1 += 1
    elif fruit2 is None or f[r] == fruit2:
        fruit2 = f[r]
        count2 += 1
    else:
        while count1 > 0 and count2 > 0:
            if f[l] == fruit1:
                count1 -= 1
            else:
                count2 -= 1
            l += 1
        if count1 == 0:
            fruit1, count1 = f[r], 1
        else:
            fruit2, count2 = f[r], 1
    
    maxx = max(maxx, r - l + 1)

print(maxx)
