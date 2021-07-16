def add(x, y):
	return x + y 

result = add(3, 4)
print(result)

def avg(list):
	return sum(list) / len(list)

a = avg([1, 2, 3])
print(a)

def is_leap(year):
	year = int(year)
	if year % 4 != 0:
		return False
	elif year % 4 == 0 and year % 100 != 0:
		return True
	elif year % 100 == 0 and year % 400 != 0:
		return False
	elif year % 400 == 0 and year % 3200 != 0:
		return True
	else:
		return False

y = is_leap(input('請輸入西元年分: '))
if y == True:
	print('閏年')
elif y == False:
	print('平年')

#邏輯清楚版
def is_leap(year):
	year = int(year)
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	elif year % 3200 != 0:
		return True
	else:
		return False

y = is_leap(input('請輸入西元年分: '))
if y == True:
	print('閏年')
else:
	print('平年')


def sum_of_list():
	l = []
	while True:
		a = input('請輸入數字: ')
		if a == 'q':
			break
		if 'q' in a:
			continue
		a = float(a)
		l.append(a)

	return sum(l)

print(sum_of_list())



