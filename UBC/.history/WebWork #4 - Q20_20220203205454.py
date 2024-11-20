import math 

data = [
0.00,
3.54,
6.36,
7.90,
7.91,
6.47,
3.97,
1.04,
-1.65,
-3.55,
-4.31,
-3.89,
-2.55,
-0.73,
1.04,
2.29,
2.76,
2.40,
1.43,
0.19,
-0.91,
-1.54,
-1.53,
-0.94,
0.00,
]

for k in range(4):
    answer = 0
    for i in range(len(data)-1):
        answer += data[i] * math.sin(i * k / 24.00 * math.pi)
    answer *=  math.pi
    print(answer)