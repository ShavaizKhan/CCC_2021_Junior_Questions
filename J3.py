odd = ['1', '3', '5', '7', '9']
even = ['2', '4', '6', '8', '0']


codes = []
x = 0

while 1 > 0:
  s = input()
  if s == '99999':
    break
  else:
    codes.append(s)
    x += 1


for i in range(0, x, 1):
  if (codes[i][1] in odd and codes[i][0] in odd) or (codes[i][1] in even and codes[i][0] in even):
    direction = 'right'
    print(direction, codes[i][2:5])
  elif codes[i][0] == '0' and codes[i][1] == '0':
    print(direction, codes[i][2:5])
  else:
    direction = 'left'
    print(direction, codes[i][2:5])
