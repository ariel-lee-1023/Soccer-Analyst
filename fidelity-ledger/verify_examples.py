"""Independent arithmetic checks for source-derived examples; no live football data."""
import json
import math
from fractions import Fraction
from pathlib import Path

checks = {}
def check(name, got, expected, tolerance=1e-10):
    assert abs(got - expected) <= tolerance, (name, got, expected)
    checks[name] = {'actual': got, 'expected': expected, 'tolerance': tolerance, 'passed': True}

check('Graham 25 completed passes net expected goals', 25*.04-75*.013, .025)
check('Graham 24 completed passes net expected goals', 24*.04-76*.013, -.028)
check('Graham break-even completion rate', .013/(.04+.013), 13/53)
check('Graham illustrative independent eight-factor success', .92**8, .5132188731375618)
check('Maguire annual Neymar amortisation EUR million', 222/5, 44.4)
check('Maguire carrying amount after two full years EUR million', 222-2*(222/5), 133.2)
check('Maguire hypothetical extension amortisation EUR million', (222-3*(222/5))/5, 17.76)
check('McElreath conjugate posterior mean', float(Fraction(6+1,9+2)), 7/11)
check('McElreath predictive mean for ten trials', 10*float(Fraction(7,11)), 70/11)

# Enumerate independent Poisson score probabilities; rows are home scores.
def score_probs(h, a, n=20):
    hp=[math.exp(-h)*h**i/math.factorial(i) for i in range(n+1)]
    ap=[math.exp(-a)*a**i/math.factorial(i) for i in range(n+1)]
    out=[0.,0.,0.]
    for i in range(n+1):
        for j in range(n+1):
            out[0 if i>j else 1 if i==j else 2] += hp[i]*ap[j]
    return out + [max(0,1-sum(out))]
values=score_probs(1.5,1.)
check('Beggs illustrative home probability rounded', round(values[0],3), .488)
check('Beggs illustrative draw probability rounded', round(values[1],3), .260)
check('Beggs illustrative away probability rounded', round(values[2],3), .252)
check('Poisson probability mass including tail', sum(values), 1.)
check('Poisson equal-rate symmetry', score_probs(1,1)[0], score_probs(1,1)[2])
check('Poisson zero-rate draw', score_probs(0,0)[1], 1.)
assert score_probs(8,6,2)[3] > .9, 'Short grids must retain their omitted-mass warning'
checks['score_grid_tail_disclosed']={'passed':True,'actual_omitted_mass':score_probs(8,6,2)[3]}
result={'status':'passed','method':'Python standard-library arithmetic; no R execution, fitting or behavioral model run','checks':checks,'poisson_illustration':dict(zip(['home','draw','away','omitted_tail'],values))}
Path(__file__).with_name('arithmetic-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'checks':len(checks),'poisson_illustration':result['poisson_illustration']},indent=2))
