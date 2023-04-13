import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


chat_id = 649103283 # Ваш chat ID, не меняйте название переменной

def solution(data) -> bool:
    mu = 300
    t_stat, p_value = ttest_1samp(data, mu)
    alpha = 0.02
    if p_value/2 < alpha and t_stat < 0:
        return True
    else:
        return False
