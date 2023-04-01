import pandas as pd
import numpy as np
from scipy.stats import expon

chat_id = 728846853 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n=len(x)
    y = expon.rvs(size = [n])
    x = x - 15 + y
    return x.mean() # Ваш ответ
