import quapy as qp

def from_name(err_name):
    if err_name == 'f1e':
        return f1e
    else:
        return qp.error.from_name(err_name)
    
def f1e(prev):
    return 1 - f1_score(prev)

def f1_score(prev):
    # https://github.com/dice-group/gerbil/wiki/Precision,-Recall-and-F1-measure
    if prev[0] == 0 and prev[1] == 0 and prev[2] == 0:
        return 1.0
    elif prev[0] == 0 and prev[1] > 0 and prev[2] == 0:
        return 0.0
    elif prev[0] == 0 and prev[1] == 0 and prev[2] > 0:
        return float('NaN')
    else:
        recall = prev[0] / (prev[0] + prev[1])
        precision = prev[0] / (prev[0] + prev[2]) 
        return 2 * (precision * recall) / (precision + recall)
