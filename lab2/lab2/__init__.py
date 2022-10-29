import random 
import numpy as np
from tkinter import N

# Function for the problem 
def problem(N, seed=42):
    """Creates an instance of the problem"""

    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

def checkFeasible(individual, N):
    goal = set(list(range(N)))
    flag = False
    coverage = set()
    for list_ in individual:
        for num in list_:
            coverage.add(num)
        if coverage == goal:
            return True
    return False

def createIndividual(indexes,len_):
    individual01 = np.zeros(len_)
    individual01[indexes] = 1
    return individual01

def createFitness(induvual):
    fitness = 0
    for list_ in induvual:
        fitness += len(list_)
    return fitness 

N = [5]

#Inital list of lists
for i in N:
    initial_formulation = problem(i)


random.seed(42)
"""
TODO:
    indexs = random_choice(0,len(initial_formulation), (len(initial_formulation)//2) +1)
    check feasiable 
    save
    creation of initial population -> len( ) = (len(initial_formulation)//2) +1
    mutation with p = 0.3
    check feasiable
    crossover
    check feasiable
"""
gap = list(range(0,len(initial_formulation)))
population = list()

while len(population) != ((len(initial_formulation)//2)+1):
    indexes = np.random.choice(gap, (len(initial_formulation)//2)+1)
    individual = np.array(initial_formulation, dtype=object)[indexes]
    if checkFeasible(individual,5) == True:
        individual01 = createIndividual(indexes, len(initial_formulation))
        population.append((createFitness(individual),individual01))

print(initial_formulation)
print(len(population))



"""
popolazione --> p1 p2 
101010
111000
o1 = p1[:x]+p2[x:]
o1 = 101000  -->  fitness
02 = 111010  -->  fitness
chekFeasibile
addPopulation 
"""


