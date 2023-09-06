
import math

def Log2(x):
	if x == 0 or x<0:
		return f'false'

	return (math.log10(x) /
			math.log10(2))

def isPowerOfTwo(n):
    
        return (math.ceil(Log2(n)) ==math.floor(Log2(n)))



if(isPowerOfTwo(3)):
	print("Yes")
else:
	print("No")

if(isPowerOfTwo(8)):
	print("Yes")
else:
	print("No")

