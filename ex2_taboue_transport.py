import itertools

COUT = [[5, 3, 4], [6, 7, 2]]
OFFRE = [8, 9]
DEMANDE = [4, 5, 8]
NB_D, NB_M = len(OFFRE), len(DEMANDE)


def cout_transport(x):
    return sum(COUT[i][j] * x[i][j] for i in range(NB_D) for j in range(NB_M))


def coin_nord_ouest():
    offre, demande = OFFRE[:], DEMANDE[:]
    x = [[0] * NB_M for _ in range(NB_D)]
    i = j = 0
    while i < NB_D and j < NB_M:
        q = min(offre[i], demande[j])
        x[i][j] = q
        offre[i] -= q
        demande[j] -= q
        if offre[i] == 0:
            i += 1
        else:
            j += 1
    return x


def voisins_transport(x):
    for i1, i2 in itertools.combinations(range(NB_D), 2):
        for j1 in range(NB_M):
            for j2 in range(NB_M):
                if j1 != j2 and x[i1][j1] > 0 and x[i2][j2] > 0:
                    y = [ligne[:] for ligne in x]
                    y[i1][j1] -= 1
                    y[i2][j2] -= 1
                    y[i1][j2] += 1
                    y[i2][j1] += 1
                    yield (i1, i2, j1, j2), y


def taboue_transport(nb_iter=12, duree_tabou=3):
    x = coin_nord_ouest()
    meilleur, c_meilleur = [l[:] for l in x], cout_transport(x)
    taboue = {}
    print("Solution initiale :", x, "cout =", c_meilleur)
    print(f"{'It':>3} {'Mouvement':>14} {'Cout':>5} {'Meilleur':>8}  Solution")
    for it in range(1, nb_iter + 1):
        candidats = []
        for m, y in voisins_transport(x):
            c = cout_transport(y)
            est_tabou = taboue.get(m, 0) >= it
            if (not est_tabou) or c < c_meilleur:
                candidats.append((c, m, y))
        if not candidats:
            break
        c, m, y = min(candidats, key=lambda t: t[0])
        x = y
        i1, i2, j1, j2 = m
        taboue[(i1, i2, j2, j1)] = it + duree_tabou
        if c < c_meilleur:
            meilleur, c_meilleur = [l[:] for l in x], c
        print(f"{it:>3} {str(m):>14} {c:>5} {c_meilleur:>8}  {x}")
    return meilleur, c_meilleur


def optimum_transport():
    best = None
    for a in range(0, min(OFFRE[0], DEMANDE[0]) + 1):
        for b in range(0, min(OFFRE[0] - a, DEMANDE[1]) + 1):
            c = OFFRE[0] - a - b
            if c < 0 or c > DEMANDE[2]:
                continue
            x = [[a, b, c], [DEMANDE[0] - a, DEMANDE[1] - b, DEMANDE[2] - c]]
            if sum(x[1]) != OFFRE[1] or min(x[1]) < 0:
                continue
            cc = cout_transport(x)
            if best is None or cc < best[0]:
                best = (cc, x)
    return best


if __name__ == "__main__":
    sol, c = taboue_transport()
    print("\nMeilleure solution :", sol, "-> cout total =", c)
    print("Verification :", optimum_transport())
