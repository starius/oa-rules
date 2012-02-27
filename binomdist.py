from scipy.stats.distributions import binom

rows = 100
cols = rows
alpha = 0.05

def cell(v):
    return '%3s' % str(v)

def result(a, b):
    if alpha < binom.cdf(b, a + b + 1, 0.5) < 1- alpha:
        return '-'
    else:
        return '+'

print(cell('') + ''.join(map(cell, range(cols))))

for a in range(rows):
    print(cell(a) + ''.join(cell(result(a, b)) for b in range(cols)))

