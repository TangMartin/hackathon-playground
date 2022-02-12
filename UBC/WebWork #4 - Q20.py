import math 

data = [
0.00,
3.37,
6.00,
7.34,
7.17,
5.62,
3.18,
0.53,
-1.65,
-2.84,
-2.82,
-1.72,
0.00,
1.72,
2.82,
2.84,
1.65,
-0.53,
-3.18,
-5.62,
-7.17,
-7.34,
-6.00,
-3.37,
0.00,
]

for k in range(1,5):
    answer = 0
    for i in range(len(data)):
        answer += data[i] * math.sin(i * k / 24.00 * math.pi)
    answer *=  math.pi / 24
    print(answer)