"""Targeted n=5 collision search for strengthened Boolean summaries."""
import argparse, random, math
from itertools import permutations
from collections import defaultdict
from pcf.boolean_geometry import analyze
from pcf.measures import conventional_profile

def _permute_mask(n,mask,p):
    out=0
    for x in range(1<<n):
        y=0
        for old in range(n):
            if x&(1<<old): y|=1<<p[old]
        if (mask>>x)&1: out|=1<<y
    return out

def canonical_symmetry(n,mask):
    """Canonicalize input-variable permutations and output complement."""
    full=(1<<(1<<n))-1
    best=None
    for p in permutations(range(n)):
        m=_permute_mask(n,mask,p)
        v=min(m,full^m)
        if best is None or v<best: best=v
    return best

def canonical_complement(n,mask):
    full=(1<<(1<<n))-1
    return min(mask,full^mask)

def cheap_key(n,mask):
    g=analyze(n,mask)
    # Exclude spectral radius from first-stage hashing to avoid spending effort
    # interpreting numerical equality before a collision exists.
    return (g.essential_variables,len(g.sensitive_edges),g.max_sensitivity,
            g.degree_histogram)

def residual_key(g):
    return (g.active_component_sizes,g.matching_number,g.active_diameters)

def refinement_keys(n,mask,digits=9):
    """Return progressively more expensive exact/numerical controls."""
    g=analyze(n,mask)
    k1=(round(g.spectral_radius,digits),)
    p=conventional_profile(n,mask)
    C,C0,C1=p["certificate_complexity"]
    k2=k1+(p["algebraic_degree"],p["real_polynomial_degree"],)
    k3=k2+(p["block_sensitivity"],)
    k4=k3+(p["decision_tree_depth"],C,tuple(sorted((C0,C1))),)
    return k1,k2,k3,k4

def strong_key(n,mask,digits=9):
    return cheap_key(n,mask)+refinement_keys(n,mask,digits)[-1]

def search(n=5,samples=10000,seed=20260929):
    rng=random.Random(seed); buckets=defaultdict(list); checked=set()
    cheap_collisions=0
    for _ in range(samples):
        mask=canonical_symmetry(n,rng.getrandbits(1<<n))
        if mask in checked: continue
        checked.add(mask)
        ck=cheap_key(n,mask)
        if buckets[ck]: cheap_collisions+=1
        buckets[ck].append(mask)

    # Only expensive-check cheap buckets that already contain differing geometry.
    candidates=[]
    for ck,masks in buckets.items():
        if len(masks)<2: continue
        bygeom=defaultdict(list)
        for m in masks:
            g=analyze(n,m); bygeom[residual_key(g)].append(m)
        if len(bygeom)<2: continue
        # Progressive refinement: retain only sub-buckets that still contain
        # at least two residual geometries after each additional control.
        work=[masks]
        for level in range(4):
            nxt=[]
            for group in work:
                split=defaultdict(list)
                for m in group:
                    split[refinement_keys(n,m)[level]].append(m)
                for subgroup in split.values():
                    if len(subgroup)<2: continue
                    geoms={residual_key(analyze(n,m)) for m in subgroup}
                    if len(geoms)>1: nxt.append(subgroup)
            work=nxt
            if not work: break
        for group in work:
            sk=strong_key(n,group[0])
            items=[(m,residual_key(analyze(n,m))) for m in group]
            candidates.append((sk,items))
    return {"unique":len(checked),"cheap_buckets":len(buckets),
            "cheap_collisions":cheap_collisions,"strong_separations":candidates}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--samples",type=int,default=10000)
    ap.add_argument("--seed",type=int,default=20260929)
    ap.add_argument("--multi-seed",type=int,default=1)
    a=ap.parse_args(); r=search(samples=a.samples,seed=a.seed)
    print("unique",r["unique"])
    print("cheap_buckets",r["cheap_buckets"])
    print("cheap_collisions",r["cheap_collisions"])
    print("strong_separations",len(r["strong_separations"]))
    for sk,items in r["strong_separations"][:10]:
        print("SUMMARY",sk)
        for item in items: print(" ",item)

if __name__=="__main__": main()
