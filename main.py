import random
import time

random.seed(time.time())
balls = [x for x in range(50)]
pawns = []
num_balls = [14, 11, 9, 7, 5, 4]
for i in range(6):
    for j in range(num_balls[i]):
        pawns.append([])
        pawns[i].append(balls.pop(int(random.random() * len(balls))) + 1)
    pawns[i].sort()
    print(pawns[i])
