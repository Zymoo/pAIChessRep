import pickle

size = 40
filename = 'generation29.pkl'
population = []

print('Odpicklowanie')
with open(filename, 'rb') as input:
    for x in range(0, size):
        unpickledOrganism = pickle.load(input)
        population.append(unpickledOrganism)

for unpickledOrganism in population:
    print(unpickledOrganism)