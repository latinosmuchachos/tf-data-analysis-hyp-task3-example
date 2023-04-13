import pandas as pd
import numpy as np


chat_id = 649103283 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    mu = 300
    t_stat, p_value = ttest_1samp(data, mu)
    alpha = 0.05
    if p_value/2 < alpha and t_stat < 0:
        return True
    else:
        return False
