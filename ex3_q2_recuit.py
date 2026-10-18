import math
import random
from ex3_commun import longueur, affiche, echange, optimum_tsp


def recuit_tsp(temperatures=(30, 24, 18, 12, 6), graine=1):
    rng = random.Random(graine)
    s = [1, 2, 3, 4, 5, 6, 7, 8]
    l_s = longueur(s)
    meilleur, l_meilleur = s[:], l_s
    print("Solution initiale :", affiche(s), "longueur =", l_s)
    print(f"{'It':>3} {'T':>4} {'Voisin':>18} {'Long.':>6} {'Delta':>6} {'exp(-D/T)':>10} {'r':>6}  Decision")
    for it, T in enumerate(temperatures, start=1):
        p, q = rng.sample(range(1, 8), 2)
        v = echange(s, p, q)
        l_v = longueur(v)
        delta = l_v - l_s
        if delta <= 0:
            proba, r, ok = 1.0, None, True
        else:
            proba = math.exp(-delta / T)
            r = rng.random()
            ok = r < proba
        if ok:
            s, l_s = v, l_v
            if l_s < l_meilleur:
                meilleur, l_meilleur = s[:], l_s
        r_txt = "  -  " if r is None else f"{r:.3f}"
        print(f"{it:>3} {T:>4} {affiche(v):>18} {l_v:>6} {delta:>6} {proba:>10.4f} {r_txt:>6}  "
              f"{'accepte' if ok else 'rejete'}")
    return meilleur, l_meilleur


if __name__ == "__main__":
    t, l = recuit_tsp()
    print("\nMeilleur circuit :", affiche(t), "longueur =", l)
    print("Optimum exact :", optimum_tsp())
