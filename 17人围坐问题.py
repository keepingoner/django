#coding:utf-8
#有17个人围成一圈（编号为0~16），从第0号的人开始从1报数，凡报到3的倍数的人离开圈子，然后再数下去，直到最后只剩下一个人为止。问此人原来的位置是多少号？
a = ['%da' % x for x in range(1, 8)]
counts = 0
while True:
	if len(a) == 1:
		print(a)
		break
	else:
		lis = []
		for x in a:
			counts+=1
			print(counts)
			if counts %3 ==0:
				lis.append(x)
		print( lis)
		a = [ x for x in a if x not in lis]
		print(a)
