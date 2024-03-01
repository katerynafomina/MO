import matplotlib.pyplot as plt
import numpy as np

colors = ["red", "pink", "green", "blue", "purple", "#006400", "#000080"]

A = []
B = []
C = []
sig = []
size = int(input("How many inequalities do you have? "))
for i in range(size):
    print("Enter coefficients of inequality: ")
    A.append(float(input("a: ")))
    B.append(float(input("b: ")))
    C.append(float(input("c: ")))
    sig.append(input("Enter znak <= or >= : "))


fig, ax = plt.subplots()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')


for i in range(size):
    x = np.arange(-20, 20, 1)
    y = (C[i] - A[i] * x) / B[i]
    ax.plot(x, y, color=colors[i])
    if sig[i] == ">=" or B[i] < 0:
        ax.fill_between(x, 6, y, color=colors[i], alpha=0.2)
    else:
        ax.fill_between(x, -6, y, color=colors[i], alpha=0.2)

plt.show()