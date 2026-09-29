"""Targeted n=5 collision search for strengthened Boolean summaries."""
import argparse, random, math
from collections import defaultdict
from pcf.boolean_geometry import analyze
from pcf.measures import conventional_profile

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

def strong_key(n,mask,digits=9):
    g=analyze(n,mask); p=conventional_profile(n,mask)
    C,C0,C1=p["certificate_complexity"]
    return (g.essential_variables,len(g.sensitive_edges),g.max_sensitivity,
            g.degree_histogram,round(g.spectral_radius,digits),
            p["block_sensitivity"],p["algebraic_degree"],
            p["decision_tree_depth"],C,tuple(sorted((C0,C1))))

def search(n=5,samples=10000,seed=20260929):
    rng=random.Random(seed); buckets=defaultdict(list); checked=set()
    cheap_collisions=0
    for _ in range(samples):
        mask=canonical_complement(n,rng.getrandbits(1<<n))
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
        strong=defaultdict(list)
        for m in masks:
            strong[strong_key(n,m)].append((m,residual_key(analyze(n,m))))
        for sk,items in strong.items():
            geoms={x[1] for x in items}
            if len(geoms)>1:
                candidates.append((sk,items))
    return {"unique":len(checked),"cheap_buckets":len(buckets),
            "cheap_collisions":cheap_collisions,"strong_separations":candidates}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--samples",type=int,default=10000)
    ap.add_argument("--seed",type=int,default=20260929)
    a=ap.parse_args(); r=search(samples=a.samples,seed=a.seed)
    print("unique",r["unique"])
    print("cheap_buckets",r["cheap_buckets"])
    print("cheap_collisions",r["cheap_collisions"])
    print("strong_separations",len(r["strong_separations"]))
    for sk,items in r["strong_separations"][:10]:
        print("SUMMARY",sk)
        for item in items: print(" ",item)

if __name__=="__main__": main()
