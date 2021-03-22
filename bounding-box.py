from turtle import *
penup()
n = int(input())
data = []
for i in range(n):
    cordination = input().split()
    x = int(cordination[0])
    y = int(cordination[1])
    #implement dots
    goto(x,y)
    pendown()
    begin_fill()
    circle(4)
    end_fill()
    penup()
    data.append((x, y))
x_big = []
x_small = []
y_big = []
y_small = []
for i in range(0, n, 2):
    if i == n-1:
        x_big.append(data[i][0])
        x_small.append(data[i][0])
        y_big.append(data[i][1])
        y_small.append(data[i][1])
        break
    if data[i][0] < data[i+1][0]:
        x_big.append(data[i+1][0])
        x_small.append(data[i][0])
    else:
        x_big.append(data[i][0])
        x_small.append(data[i+1][0])
    if data[i][1] < data[i+1][1]:
        y_big.append(data[i+1][1])
        y_small.append(data[i][1])
    else:
        y_big.append(data[i][1])
        y_small.append(data[i+1][1])

x_max = float('-inf')
x_min = float('inf')
y_max = float('-inf')
y_min = float('inf')

for i in x_big:
    if x_max < i:
        x_max = i
for i in x_small:
    if x_min > i:
        x_min = i

for i in y_big:
    if y_max < i:
        y_max = i
for i in y_small:
    if y_min > i:
        y_min = i
#implement graphic bond
color("red")
pensize(4)
goto(x_max,y_max)
pendown()
goto(x_max,y_min)
goto(x_min,y_min)
goto(x_min,y_max)
goto(x_max,y_max)
#printing result
print("X:","Max:",x_max,"Min", x_min)
print("Y:","Max:",y_max,"Min", y_min)
ht()
done()


