# --*-- coding:utf-8 --*--

def trim(s):
	num = 0
	n = -1

	if len(s) == 0:
		#print('空值')
		return ''
	else:
		while num < len(s):
			if s[num] != ' ':
				s = s[num:]
				break
			else:
				if num == len(s)-1:
					s = ''
					#print('第一:'+"'"+s+"'",len(s))
			num += 1
		if len(s) == 0:
			#print('第二:'+"'"+s+"'",len(s))
			return s
		else:
			while n >= (-1)*len(s):
				if s[n] != ' ':
					if n == -1:
						s = s[:]
					else:
						s = s[:(n+1)]
					#print("第三'"+s+"'")
					return s
				n -= 1
				#print("最后'"+s+"'", len(s))


if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')