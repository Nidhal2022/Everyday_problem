def li(nu,de):
    m=0
    for i in range(len(nu)):
        m=m+(nu[i]/de[i])
        i+=1
    
    return m
print(li([1,2,2,8],[2,4,6,12]))