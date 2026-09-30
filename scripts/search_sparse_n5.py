"""Structured n=5 search over sparse truth-table layers.

Enumerates functions with exactly k one-inputs. Output complements cover the
corresponding dense layers. Expensive controls are evaluated only after cheap
summary collisions with differing residual geometry are found.
"""
import argparse
from itertools import combinations, permutations
from collections import defaultdict
from scripts.search_n5 import canonical_symmetry, cheap_key, residual_key, refinement_keys, strong_key
from pcf.boolean_geometry import analyze

def _permute_vertex(n,x,p):
    y=0
    for old in range(n):
        if x&(1<<old): y|=1<<p[old]
    return y

def canonical_sparse_vertices(n,vertices):
    """Canonical mask under input-variable permutations for a sparse truth set.

    For the sparse layers used here (k < 2^(n-1)), output complementation
    cannot produce another mask in the same sparse layer, so only coordinate
    permutations need be considered.
    """
    best=None
    for p in permutations(range(n)):
        m=0
        for x in vertices: m |= 1<<_permute_vertex(n,x,p)
        if best is None or m<best: best=m
    return best

def mask_from_vertices(vertices):
    m=0
    for v in vertices:
        m |= 1<<v
    return m

def search_layer(n=5,k=4):
    buckets=defaultdict(list); seen=set(); raw=0
    for ones in combinations(range(1<<n),k):
        raw+=1
        m=canonical_symmetry(n,mask_from_vertices(ones))
        if m in seen: continue
        seen.add(m)
        buckets[cheap_key(n,m)].append(m)

    candidate_groups=[]
    for masks in buckets.values():
        if len(masks)<2: continue
        geoms={residual_key(analyze(n,m)) for m in masks}
        if len(geoms)<2: continue
        work=[masks]
        for level in range(4):
            nxt=[]
            for group in work:
                split=defaultdict(list)
                for m in group:
                    split[refinement_keys(n,m)[level]].append(m)
                for subgroup in split.values():
                    if len(subgroup)>1 and len({residual_key(analyze(n,m)) for m in subgroup})>1:
                        nxt.append(subgroup)
            work=nxt
            if not work: break
        for group in work:
            candidate_groups.append((strong_key(n,group[0]),
                                     [(m,residual_key(analyze(n,m))) for m in group]))
    return {"n":n,"k":k,"raw":raw,"unique_canonical":len(seen),
            "cheap_buckets":len(buckets),
            "cheap_collision_classes":sum(1 for v in buckets.values() if len(v)>1),
            "strong_separations":candidate_groups}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--k",type=int,default=4)
    a=ap.parse_args()
    r=search_layer(k=a.k)
    print("n",r["n"],"k",r["k"],"raw",r["raw"],
          "unique_canonical",r["unique_canonical"],
          "cheap_buckets",r["cheap_buckets"],
          "cheap_collision_classes",r["cheap_collision_classes"],
          "strong_separations",len(r["strong_separations"]))
    for key,items in r["strong_separations"][:20]:
        print("SUMMARY",key)
        for item in items: print(" ",item)

if __name__=="__main__":
    main()
