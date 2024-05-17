#!/usr/bin/python3
arr = [1, 2, 3, 4,5,6,7,8,9,10]
track = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr.insert(track, arr.pop(i))
        track += 1
print(arr)




