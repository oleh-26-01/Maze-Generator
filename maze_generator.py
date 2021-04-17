from random import randint
from time import time, sleep
from os import system, name

dt = lambda x = time(): round(time() -x, 3)
n = 15
l = 2*n+1
m = [["+" for o in range(l)] for i in range(l)]

for y in range(l):
	for x in range(l):
		if y % 2 == 1 and x % 2 == 1:
			if y + 1 < l - 1:
				m[y+1][x] = '-'
			if x + 1 < l - 1:
				m[y][x+1] = '-'

def draw():
	system('cls' if name=='nt' else 'clear')
	for y in range(l):
		for x in range(l):
			print(m[y][x], end=" ")
		print()

s = [[1, 2, 1, 3], [2, 1, 3, 1]]
r = [[1, 0, -1, 0], [0, 1, 0, -1]]
m[1][1] = ' '
c = 1
while True:
	if c == (n)**2:
		break

	z = s[randint(0, len(s)-1)]
	
	m[z[0]][z[1]] = ' '
	m[z[2]][z[3]] = ' '
	new = []
	for i in range(len(s)):
		if s[i][2:] != z[2:]:
			new += [s[i]]
		else:
			if m[s[i][0]][s[i][1]] != ' ':
				m[s[i][0]][s[i][1]] = '+'
	s = new
	for i in range(4):
		if 0 < z[2] + r[0][i] < l - 1 and 0 < z[3] + r[1][i]:
			if m[z[2] + r[0][i]][z[3] + r[1][i]] == '-':
				s += [[z[2] + r[0][i], z[3] + r[1][i], z[2] + r[0][i] * 2, z[3] + r[1][i] * 2]]
	c += 1
	# draw()


t = dt()
draw()
print("time:", t)
