import pandas as pd
import numpy as np
from scipy.stats import expon

chat_id = 728846853 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 10
    n = len(x)
    y = expon.rvs(loc = 15, size = n)
    x = x + y
    x = x/t
    return x.mean() # Ваш ответ
