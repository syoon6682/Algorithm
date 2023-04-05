import numpy as np
import sympy as sym
from sympy.abc import x
from sympy.plotting import plot

train_x = (np.random.rand(1000) - 0.5) * 10
train_y = np.zeros_like(train_x)

def func(val):
    fun = sym.poly(7*x + 2)
    return fun.subs(x, val)

for i in range(1000):
    train_y[i] = func(train_x[i])

# initialize
w, b = 0.0, 0.0

lr_rate = 1e-2
n_data = 10
errors = []

# batch size는 10 -> train_x에서 10개를 '비복원추출'로 뽑는 것이 핵심!
for i in range(100):
    # 비복원추출
    batch_select = np.random.choice(1000, 10, replace=False)
    new_train_x = train_x[batch_select]
    new_train_y = train_y[batch_select]

    # 이후는 새로운 train data를 활용하여 경사하강법 진행
    _y = new_train_x * w + b
    error = np.sum((_y - new_train_y) ** 2) / n_data

    gradient_w = np.sum((_y - new_train_y) * new_train_x) / n_data
    gradient_b = np.sum((_y - new_train_y)) / n_data

    w -= lr_rate * gradient_w
    b -= lr_rate * gradient_b

    # Error graph 출력하기 위한 부분
    errors.append(error)

print("w : {} / b : {} / error : {}".format(w, b, error))