
def printLeaders(arr,sz):
    
    for i in range(0, sz):
        for j in range(i+1, sz):
            if arr[i]<=arr[j]:
                break
        if j == sz-1: 
            print (arr[i],end=' ')

arr=[16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))

