import pandas as pd
import numpy as np
from scipy.stats import expon

chat_id = 728846853 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = (x.mean()+14)/10
    return a # Ваш ответ
