import numpy as np
def adjust_difficulty(data):
    if len(data) < 3:
        return 3
    recent = np.mean([correct for _, correct, _ in data[-3:]])
    if recent > 0.8:
        return 5
    elif recent < 0.4:
        return 1
    else:
        return 3
