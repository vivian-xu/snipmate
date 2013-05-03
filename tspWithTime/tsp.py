import itertools


timeBount = [[0, 24], [1, 4], [4, 6], [1, 2],
             [4, 7], [3, 5.5], [2, 5], [5, 8], [1.5, 4]]

timeReload = [0, 1, 2, 1, 3, 2, 2.5, 3, 0.8]

adj = [[0, 40, 60, 75, 90, 200, 100, 160, 80],
       [40, 0, 65, 40, 100, 50, 75, 110, 100],
       [60, 65, 0, 75, 100, 100, 75, 75, 75],
       [75, 40, 75, 0, 100, 50, 90, 90, 150],
       [90, 100, 100, 100, 0, 100, 75, 75, 100],
       [200, 50, 100, 50, 100, 0, 70, 90, 75],
       [100, 75, 75, 90, 75, 70, 0, 70, 100],
       [160, 110, 75, 90, 75, 90, 70, 0, 100],
       [80, 100, 75, 150, 100, 75, 100, 100, 0]]


def isTimeOk(source, target, timerange=None):  # tested
    if timerange is None:
        timerange = timeBount[source]
    v = 50
    cost = adj[source][target] / v
    left = [0, 0]
    if timerange[0] + cost > timeBount[target][1]:
        return [-1, []]
    else:
        left[0] = max(timerange[0] + cost + timeReload[target],
                      timeBount[target][0])
    if timerange[1] + cost < timeBount[target][0]:
        return [-1, []]
    else:
        left[1] = min(timerange[1] + cost + timeReload[target],
                      timeBount[target][1])
    return [adj[source][target], left]


def seq_time(choice):
    res = dict()
    for seq in itertools.permutations(choice):
        distance = 0
        trange = [0, 24]
        flag = 1
        cir = list(seq)
        cir.insert(0, 0)
        cir.append(0)
        for i in range(len(cir) - 1):
            d, t = isTimeOk(cir[i], cir[i+1], trange)
            if d == -1:
                flag = 0
                break
            else:
                distance += d
                trange = t
        if flag:
            res[seq] = distance
    return res


def isOverWeight(choice, weight=8):
    """ return True is overweight"""
    weight_demand = [0, 2, 1.5, 4.5, 3, 1.5, 4, 2.5, 3]  # q
    total = 0
    for i in choice:
        total += weight_demand[i]
    return total > 8


def single_car(clients):
    """calculate choices of optional cars for clients sequence"""
    choices = [[]]
    for client in clients:
        new_choices = []
        for choice in choices:
            new_choice = [client]
            new_choice.extend(choice)
            if not isOverWeight(new_choice):
                new_choices.append(new_choice)
        choices.extend(new_choices)
    choices.remove([])
    return choices


def list2set(orig):
    res = set()
    for ele in orig:
        if isinstance(ele, list):
            res.update(list2set(ele))
        else:
            res.add(ele)
    return res


def multi_car(choices):
    """calculate solutions of optional cars for choices sequence"""
    solutions = [[]]
    ok = []
    for choice in choices:
        new_solutions = []
        for solution in solutions:
            # drop if node repeated
            if len(list2set(choice) & list2set(solution)) is 0:
                new_solution = [choice]
                new_solution.extend(solution)
                if len(list2set(new_solution)) is 8:
                    ok.append(new_solution)
                else:
                    new_solutions.append(new_solution)
        solutions.extend(new_solutions)
    return ok
