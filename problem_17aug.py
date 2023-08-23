def check(arr, n, c1, c2):

   for i in range(c1, c2+1):
       a = False
       for j in range(n):
           if arr[j] == i:
               a = True
               break
       if not a:
           return False  
   return True  

arr = [1, 4, 5, 2, 7, 8, 3]
print('The array: ',arr)
n = len(arr)
print('check the rang of list')
c1 = int(input('Enter the first: '))
c2 = int(input('Enter tge second: '))
if check(arr, n, c1, c2):
   print("YES")
else:
   print("NO!!")