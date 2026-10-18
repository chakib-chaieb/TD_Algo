import itertools

INF = 1000
ARETES = {
    (1, 2): 14, (1, 3): 15, (1, 8): 17,
    (2, 3): 13, (2, 4): 14, (2, 5): 20, (2, 8): 21,
    (3, 4): 11, (3, 5): 21, (3, 6): 17, (3, 7): 9, (3, 8): 9,
    (4, 5): 11, (4, 6): 10, (4, 7): 8, (4, 8): 20,
    (5, 6): 15, (5, 7): 18,
    (6, 7): 9,
    (7, 8): 13,
}


def dist(a, b):
    return ARETES.get((min(a, b), max(a, b)), INF)


def longueur(tour):
    return sum(dist(tour[k], tour[(k + 1) % len(tour)]) for k in range(len(tour)))


def affiche(tour):
    return "-".join(map(str, tour)) + "-" + str(tour[0])


def echange(tour, p, q):
    t = tour[:]
    t[p], t[q] = t[q], t[p]
    return t


def optimum_tsp():
    best = None
    for perm in itertools.permutations(range(2, 9)):
        t = [1] + list(perm)
        l = longueur(t)
        if best is None or l < best[1]:
            best = (t, l)
    return best
