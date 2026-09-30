"""Exact conventional Boolean-function measures for small n."""
from functools import lru_cache

def bit(mask,x): return (mask>>x)&1

def algebraic_degree(n,mask):
    # ANF coefficients via Möbius transform.
    a=[bit(mask,x) for x in range(1<<n)]
    for i in range(n):
        for x in range(1<<n):
            if x&(1<<i): a[x]^=a[x^(1<<i)]
    return max((x.bit_count() for x,c in enumerate(a) if c),default=0)

def real_polynomial_degree(n,mask):
    """Degree of the unique real multilinear polynomial representing f on {0,1}^n."""
    a=[bit(mask,x) for x in range(1<<n)]
    for i in range(n):
        b=1<<i
        for x in range(1<<n):
            if x&b:
                a[x]-=a[x^b]
    return max((x.bit_count() for x,coef in enumerate(a) if coef!=0),default=0)

def sensitivity_at(n,mask,x):
    return sum(bit(mask,x)!=bit(mask,x^(1<<i)) for i in range(n))

def block_sensitivity_at(n,mask,x):
    good=[s for s in range(1,1<<n) if bit(mask,x)!=bit(mask,x^s)]
    # maximum number of pairwise-disjoint good masks
    @lru_cache(None)
    def rec(used):
        best=0
        for s in good:
            if not (s&used):
                best=max(best,1+rec(used|s))
        return best
    return rec(0)

def block_sensitivity(n,mask):
    return max(block_sensitivity_at(n,mask,x) for x in range(1<<n))

def certificate_at(n,mask,x):
    target=bit(mask,x)
    # subset S of coordinates certifies x if all y agreeing on S have target output.
    for k in range(n+1):
        for S in range(1<<n):
            if S.bit_count()!=k: continue
            pattern=x&S
            ok=True
            for y in range(1<<n):
                if (y&S)==pattern and bit(mask,y)!=target:
                    ok=False; break
            if ok: return k
    return n

def certificate_complexity(n,mask):
    vals=[certificate_at(n,mask,x) for x in range(1<<n)]
    return max(vals),max((v for x,v in enumerate(vals) if bit(mask,x)==0),default=0),max((v for x,v in enumerate(vals) if bit(mask,x)==1),default=0)

def deterministic_decision_tree_depth(n,mask):
    # exact recursion over partial assignments encoded as (known_mask,values)
    @lru_cache(None)
    def D(known,values):
        outs=set()
        for x in range(1<<n):
            if (x&known)==values: outs.add(bit(mask,x))
        if len(outs)<=1: return 0
        best=n+1
        for i in range(n):
            b=1<<i
            if known&b: continue
            best=min(best,1+max(D(known|b,values&~b),D(known|b,values|b)))
        return best
    return D(0,0)

def conventional_profile(n,mask):
    return {
        "block_sensitivity":block_sensitivity(n,mask),
        "algebraic_degree":algebraic_degree(n,mask),
        "real_polynomial_degree":real_polynomial_degree(n,mask),
        "certificate_complexity":certificate_complexity(n,mask),
        "decision_tree_depth":deterministic_decision_tree_depth(n,mask),
    }


def xor_with_parity(n,mask,r):
    """Truth-table mask of f(x) XOR parity(z), with r fresh high coordinates."""
    out=0
    for z in range(1<<r):
        p=z.bit_count()&1
        for x in range(1<<n):
            y=x | (z<<n)
            if bit(mask,x)^p: out |= 1<<y
    return out
