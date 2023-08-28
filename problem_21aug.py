def rr(arr, n, ofp, cur):
    
    temp = arr[cur]
    for i in range(cur, ofp, -1):
        arr[i] = arr[i - 1]
        arr[ofp] = temp
    return arr


def rearrange(arr, n):
    ofp = -1
    for index in range(n):
        if(ofp >= 0):

            if((arr[index] >= 0 and arr[ofp] < 0) or
               (arr[index] < 0 and arr[ofp] >= 0)):
                arr = rr(arr, n, ofp, index)
        if(index-ofp > 2):
                    ofp += 2
        else:
                    ofp = - 1

        if(ofp == -1):
            if((arr[index] >= 0 and index % 2 == 0) or
               (arr[index] < 0 and index % 2 == 1)):
                ofp = index
    return arr


arr = [-5, -2, 5, 2, 4,
       7, 1, 8, 0, -8]

print("Given Array is:")
print(arr)

print("\nRearranged array is:")
print(rearrange(arr, len(arr)))
