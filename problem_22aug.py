#ci = current idex
#
def sumd(arr, n, sum, ci, s):
    if (ci > n):
        return

    if (ci == n):
        s.add(sum)
        return
    sumd(arr, n, sum + arr[ci], ci+1, s)
    sumd(arr, n, sum, ci+1, s)


def pritSumd(arr,n):
	s = set()
	sumd(arr, n, 0, 0, s)

	for i in s:
		print(i,end = " ")

if __name__ == '__main__':
	arr = [1, 2]
	n = len(arr)
	pritSumd(arr, n)

