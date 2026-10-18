import random
from ex3_commun import longueur, affiche, optimum_tsp


def croisement_ox(p1, p2, rng):
    n = len(p1)
    a, b = sorted(rng.sample(range(n), 2))
    enfant = [None] * n
    enfant[a:b + 1] = p1[a:b + 1]
    reste = [g for g in p2 if g not in enfant]
    k = 0
    for i in range(n):
        if enfant[i] is None:
            enfant[i] = reste[k]
            k += 1
    return enfant


def mutation(chrom, rng):
    p, q = rng.sample(range(len(chrom)), 2)
    c = chrom[:]
    c[p], c[q] = c[q], c[p]
    return c


def ag_tsp(taille_pop=8, nb_gen=30, pc=0.9, pm=0.2, graine=3):
    rng = random.Random(graine)
    fitness = lambda ch: longueur([1] + ch)
    pop = []
    for _ in range(taille_pop):
        ch = list(range(2, 9))
        rng.shuffle(ch)
        pop.append(ch)
    print("Population initiale :")
    for ch in pop:
        print("   ", affiche([1] + ch), "longueur =", fitness(ch))
    for g in range(1, nb_gen + 1):
        pop.sort(key=fitness)
        nouvelle = [pop[0][:]]
        while len(nouvelle) < taille_pop:
            parents = []
            for _ in range(2):
                a, b = rng.sample(pop, 2)
                parents.append(a if fitness(a) <= fitness(b) else b)
            enfant = croisement_ox(parents[0], parents[1], rng) if rng.random() < pc else parents[0][:]
            if rng.random() < pm:
                enfant = mutation(enfant, rng)
            nouvelle.append(enfant)
        pop = nouvelle
        meilleur_gen = min(pop, key=fitness)
        if g <= 5 or g % 5 == 0:
            print(f"Generation {g:>2} : meilleur = {affiche([1] + meilleur_gen)} "
                  f"longueur = {fitness(meilleur_gen)}")
    best = min(pop, key=fitness)
    return [1] + best, fitness(best)


if __name__ == "__main__":
    t, l = ag_tsp()
    print("\nMeilleur circuit :", affiche(t), "longueur =", l)
    print("Optimum exact :", optimum_tsp())
