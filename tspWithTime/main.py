import tsp

choices = tsp.single_car(range(1, 9))

res = dict()
for choice in choices:
    res.update(tsp.seq_time(choice))

print(len(res))

sols = tsp.multi_car(res.keys())
print(len(sols))
