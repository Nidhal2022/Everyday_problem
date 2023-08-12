def sum_two(n, k):   
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] + n[j] == k:
                return f'the numbers {n[i],[j]} can be sum of {m}'
    return False
list=[]
N1 = int(input('the length of array : '))

for i in range(N1):
    a=int(input('Enter a number : '))
    list.append(a)
    i+=1
'''N1 = int(input('Enter First number : '))
list.append(N1)
N2 = int(input('Enter First number : '))
list.append(N2)

N3 = int(input('Enter First number : '))
list.append(N3)'''
m=4
print("the list is: ",list,"the number: ",m)
print("------------------------------")
n=0
r=""

'''while n < (len(list)):
    
    if list[n]==m:
        r=f"{list[n]}"
    elif (list[n]+list[n-1])==m:
        r=f"{list[n],list[n-1]}"
    else:
        #r=f"the number: {list[n]} cant be added to get: {m}"
        print("")
    n+=1
    print(r)
'''
print(sum_two(list, m))


