import logging
import random
import numpy as np
from tqdm.notebook import tqdm
from matplotlib import pyplot as plt
from matplotlib import cm

logging.basicConfig(
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)
def rastrigin(x, A=10):
    """NumPy Rastrigin test function"""
    return -np.sum(A - A * np.cos(2 * np.pi * x) + x**2, axis=0)
N_POINTS = 200
r = np.linspace(-5, 5, N_POINTS)

def Sphere(x,A = 10):
    return -np.sum(x**2, axis=0)


x = np.array(np.meshgrid(r, r))
z = rastrigin(x)
z1 = Sphere(x)
plt.figure(figsize=(10, 10))
ax = plt.axes(projection="3d")
ax.plot_surface(*np.meshgrid(r, r), z1, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)
None

np.random.seed(42)
random.seed(42)
N_DIM = 2

time = 1
x1, y1 = random.uniform(-5,5), random.uniform(-5,5)
first_point = np.array([x1,y1])
top  = first_point
#second_point = np.array([random.uniform(-5,5), random.uniform(-5,5)])
print(Sphere(top))

while time < 250:
    checkCoord = False
    while checkCoord == False:
        xi = top[0] + random.randint(-2,2)
        yi = top[1]+ random.randint(-2,2)
        if x1<5 and xi>-5 and yi<5 and yi>-5:
            checkCoord = True
    if Sphere(top) < Sphere(np.array([xi,yi])):
        top = np.array([xi,yi])
    time += 1

print(Sphere(top))

time = 0 
while Sphere(top) <= 0.000009:
    checkCoord = False
    while checkCoord == False:
        xi = top[0] + random.uniform(-0.5,0.5)
        yi = top[1] + random.uniform(-0.5,0.5)
        if x1<5 and xi>-5 and yi<5 and yi>-5:
            checkCoord = True
    if Sphere(top) < Sphere(np.array([xi,yi])):
        top = np.array([xi,yi])
    time += 1

print(f"{Sphere(top)} found in {250+time} steps")

        







