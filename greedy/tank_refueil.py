from math import inf
# Tank refueil
# trace:  =====\s1\====\s2\==\s3\=============\s4\===...===
#  s(i) - station distance from point 0
#  L - tank capacity (liters)
#  Tank starts with a full tank and use 1l / km
#  p(i) - price per liter at each station

# Problems:
# 1. Minimum number of refuelings to reach point t.
# 2. Minimum cost of getting to point t (at each station you can refuel as much as you want).
# 3. Minimum cost of getting to point t (if we refuel, we refuel to the full).


# ___1.solution___
def car_fueling(t, l, n, s):
    num_refill, curr_refill, max_distance = 0, 0, l

    while max_distance < t:
        if curr_refill >= n or s[curr_refill] > max_distance:
            return -1

        while curr_refill < n - 1 and s[curr_refill + 1] <= max_distance:
            curr_refill += 1

        num_refill += 1
        max_distance = s[curr_refill] + l
        curr_refill += 1

    return num_refill


# ___2. solution___
def refueil_how_much_want(s, p, l, t):
    curr_stat = last_stat = 0
    prev_cost = inf
    curr_l = l
    cost = 0
    while s[curr_stat] < l:
        if prev_cost > p[curr_stat]:
            prev_cost = p[curr_stat]
            last_stat = curr_stat
            curr_l = l - s[curr_stat]
        curr_stat += 1

    # We have to get to the end point t
    while s[last_stat] + curr_l < t:
        # szukam najdalszej stacji oddalonej od last stat o l
        while s[last_stat] + l > s[curr_stat + 1] and curr_stat + 1 < len(s) - 1:
            curr_stat += 1

        next_station = -1
        curr_cost = inf

        # within the distance radius from the previous station - I am looking for a station with minimal cost
        for i in range(last_stat + 1, curr_stat + 1):
            if p[i] < curr_cost:
                curr_cost = p[i]
                next_station = i

        # The price at the previous station is cheaper - so we refuel (full)
        if curr_cost > prev_cost:

            # At the last station, we refuel just enough to reach t
            while s[last_stat] + l - curr_l > t:
                curr_l += 1

            curr_koszt = prev_cost * (l - curr_l)
            cost += curr_koszt
            curr_l = l - (s[next_station] - s[last_stat])

        # We refuel just enough to get to the next - cheaper station
        else:
            curr_koszt = (s[next_station] - s[last_stat] - curr_l) * p[last_stat]
            cost += curr_koszt
            curr_l = 0

        last_stat, curr_stat = next_station, next_station

    return cost


# ___3.solution___
def refueil_to_full(s, p, l, t):
    n = len(s)
    f = [[sum(p) * 10] * 2 for _ in range(n)]
    curr_stat = 0

    while s[curr_stat] <= l:
        f[curr_stat][0] = 0
        f[curr_stat][1] = l - s[curr_stat]
        curr_stat += 1

    for i in range(curr_stat, n):
        k = 0
        while s[k] + l < s[i]:
            k += 1

        minim = sum(p) * 10
        fuel = 0

        for j in range(k, i):
            if f[j][0] + p[j] * (l - f[j][1]) < minim:
                fuel = l - (s[i] - s[j])

                if s[i] + fuel < t and i == len(s) - 1:
                    continue
                else:
                    minim = f[j][0] + p[j] * (l - f[j][1])

        f[i] = [minim, fuel]

    res = 0
    while s[res] + f[res][1] < t:
        res += 1

    return f[res][0]


# Examples:
l = 14
s = [1, 9, 15, 16, 17, 27, 28]
p = [1, 100, 10, 15, 1, 30, 30]
t = 30

print("Number of fueling: ")
for i in range(21):
    c = car_fueling(i, l, len(s), s)
    print("Point:", i, "-> ", c)
print()

print("Minimum cost of getting to point t (at each station you can refuel as much as you want):")
print(refueil_how_much_want(s, p, l, t), end = "\n\n")

print("Minimum cost of getting to point t (if we refuel, we refuel to the full): ")
for i in range(t + 1):
    a = refueil_to_full(s, p, l, i)
    print("Point:", i, "-> ", a)