# --*-- coding:utf-8 --*--

def triangles():
	L=[1]

	while True:
		yield L

		#方法一：
		N = [0] + L + [0]
		L = [N[i] + N[i+1] for i in range(len(N)-1)]
		
		#方法二：
		#N = L[:]
		#for i in range(len(N)-1):
		#	N[i+1] = L[i] + L[i+1]
		#N.append(1)
		#L = N[:]
		#直接在L上进行append，则L的指向没有变化，在最后其测试中results中的元素全部为杨辉三角的最后一行

		#方法三：
		#L.append(0)
		#L = [L[i-1] + L[i] for i in range(len(L))]
		#在测试中，result前n-1个元素中指定的位置是经过了L.append（0），所以都在后面加了一个元素[0]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

print(results)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')

#triangles(10)

'''
def triangles():
	L=[1]
	while True:
		yield L
		N = [0] + L + [0]
		L = [N[i] + N[i+1] for i in range(len(N)-1)]
		n += 1


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
'''