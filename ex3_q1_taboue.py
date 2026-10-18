import itertools
from ex3_commun import longueur, affiche, echange, optimum_tsp


def taboue_tsp(nb_iter=20, duree_tabou=4):
    s = [1, 2, 3, 4, 5, 6, 7, 8]
    meilleur, l_meilleur = s[:], longueur(s)
    taboue = {}
    print("Solution initiale :", affiche(s), "longueur =", l_meilleur)
    print(f"{'It':>3} {'Echange':>8} {'Voisin choisi':>18} {'Long.':>6} {'Meilleur':>9}  Liste taboue")
    for it in range(1, nb_iter + 1):
        candidats = []
        for p, q in itertools.combinations(range(1, 8), 2):
            t = echange(s, p, q)
            m = tuple(sorted((s[p], s[q])))
            l = longueur(t)
            est_tabou = taboue.get(m, 0) >= it
            if (not est_tabou) or l < l_meilleur:
                candidats.append((l, m, t))
        l, m, s = min(candidats, key=lambda c: c[0])
        taboue[m] = it + duree_tabou
        if l < l_meilleur:
            meilleur, l_meilleur = s[:], l
        actifs = [k for k, v in taboue.items() if v > it]
        print(f"{it:>3} {str(m):>8} {affiche(s):>18} {l:>6} {l_meilleur:>9}  {actifs}")
    return meilleur, l_meilleur


if __name__ == "__main__":
    t, l = taboue_tsp()
    print("\nMeilleur circuit :", affiche(t), "longueur =", l)
    print("Optimum exact :", optimum_tsp())
