#!urs/bin/env python
# --*-- coding:utf-8 --*--


s = [1, 2, 3, 4]
n = 0

for i in s:
	for j in s:
		for k in s:
			if i != j and j != k and i != k:
				n += 1
				print('第 {0} 个：{1}!'.format(n, 100*i+10*j+k))

print('共有{0}个数字'.format(n))