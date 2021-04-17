from random import randint
from time import time, sleep
from pygame import init, display, draw, FULLSCREEN, event, KEYDOWN, K_ESCAPE, QUIT

init()
window = display.set_mode((0, 0), FULLSCREEN)
width, height = window.get_size()
center = [int(width/2), int(height/2)]
size = min(width, height) / 2
x, y = int((width - size) / 2), int((height - size) / 2)
dt = lambda h = time() : time() - h
window.fill([20]*3)
draw.rect(window, [0]*3, [center[0] - size, center[1] - size, size*2, size*2])
n = 100
l = 2*n+1
rs = size / l * 2

m = [[0 for o in range(l)] for i in range(l)]

for y in range(l):
	for x in range(l):
		if y % 2 == 1 and x % 2 == 1:
			if y + 1 < l - 1:
				m[y+1][x] = 2
			if x + 1 < l - 1:
				m[y][x+1] = 2

s = [[1, 2, 1, 3], [2, 1, 3, 1]]
r = [[1, 0, -1, 0], [0, 1, 0, -1]]
m[1][1] = 1
draw.rect(window, [255]*3, [int(center[0] - size + rs), int(center[1] - size + rs), rs+1, rs+1])
c = 1
while True:
	if c == (n)**2:
		break

	z = s[randint(0, len(s)-1)]
	
	m[z[0]][z[1]] = 1
	m[z[2]][z[3]] = 1
	x1, y1 = int(center[0] - size + z[0] * rs), int(center[1] - size + z[1] * rs)
	x2, y2 = int(center[0] - size + z[2] * rs), int(center[1] - size + z[3] * rs)
	draw.rect(window, [255]*3, [x1, y1, rs+1, rs+1])
	draw.rect(window, [255]*3, [x2, y2, rs+1, rs+1])
	if c % 10 == 0:
		display.flip()
	new = []
	for i in range(len(s)):
		if s[i][2:] != z[2:]:
			new += [s[i]]
		else:
			if m[s[i][0]][s[i][1]] != 1:
				m[s[i][0]][s[i][1]] = 0
	s = new
	for i in range(4):
		if 0 < z[2] + r[0][i] < l - 1 and 0 < z[3] + r[1][i]:
			if m[z[2] + r[0][i]][z[3] + r[1][i]] == 2:
				s += [[z[2] + r[0][i], z[3] + r[1][i], z[2] + r[0][i] * 2, z[3] + r[1][i] * 2]]
	c += 1

	for _event in event.get():
		if _event.type == KEYDOWN or _event.type == QUIT:
			if _event.key == K_ESCAPE or _event.type == QUIT:
				quit()
	
while True:
	for _event in event.get():
		if _event.type == KEYDOWN or _event.type == QUIT:
			if _event.key == K_ESCAPE or _event.type == QUIT:
				quit()
