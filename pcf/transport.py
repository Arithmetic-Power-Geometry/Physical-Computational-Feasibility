"""Explicit local noisy-transport model for Boolean sensitivity edges."""
from dataclasses import dataclass
from itertools import permutations
from pcf.boolean_geometry import analyze

@dataclass(frozen=True)
class TransportResult:
    mask:int; eta:float; epsilon:float; permutation:tuple
    readout_site:int; worst_margin:float; failed_edges:int
    mean_distance:float; max_distance:int; weighted_distance:float

def evaluate_line(n,mask,eta,epsilon,permutation,readout_site):
    """Inputs i occupy line site permutation[i]. Sensitive-edge signals contract as eta**distance."""
    g=analyze(n,mask); threshold=1-2*epsilon
    dists=[]; failed=0; margins=[]; weighted=0.0
    # Every undirected sensitivity edge differs in exactly one bit; identify that bit.
    for x,y in g.sensitive_edges:
        diff=x^y; i=diff.bit_length()-1
        dist=abs(permutation[i]-readout_site)
        signal=eta**dist
        margins.append(signal-threshold)
        dists.append(dist); weighted += dist
        if signal+1e-15 < threshold: failed += 1
    return TransportResult(mask,eta,epsilon,tuple(permutation),readout_site,
        min(margins) if margins else 1.0-threshold,failed,
        sum(dists)/len(dists) if dists else 0.0,max(dists,default=0),weighted)

def optimize_line(n,mask,eta,epsilon):
    """Lexicographically minimize failures, max distance, total sensitivity-edge transport, then maximize margin."""
    best=None
    for perm in permutations(range(n)):
        for r in range(n):
            z=evaluate_line(n,mask,eta,epsilon,perm,r)
            key=(z.failed_edges,z.max_distance,z.weighted_distance,-z.worst_margin)
            if best is None or key<best[0]: best=(key,z)
    return best[1]

def refreshes_needed(distance,eta,epsilon):
    """Minimum ideal refresh breaks needed so every unrefreshed segment satisfies eta**segment >= 1-2epsilon."""
    if distance<=0: return 0
    threshold=1-2*epsilon
    # longest integer segment allowed by contraction
    allowed=0
    while eta**(allowed+1) >= threshold-1e-15: allowed+=1
    if allowed==0: return distance
    # number of internal refreshes splitting path into ceil(distance/allowed) segments
    segments=(distance+allowed-1)//allowed
    return max(0,segments-1)

def refresh_load_line(n,mask,eta,epsilon,permutation,readout_site):
    g=analyze(n,mask); total=0; worst=0
    for x,y in g.sensitive_edges:
        i=(x^y).bit_length()-1
        d=abs(permutation[i]-readout_site)
        r=refreshes_needed(d,eta,epsilon)
        total+=r; worst=max(worst,r)
    return total,worst

def optimize_refresh_line(n,mask,eta,epsilon):
    best=None
    for perm in permutations(range(n)):
        for r in range(n):
            total,worst=refresh_load_line(n,mask,eta,epsilon,perm,r)
            z=evaluate_line(n,mask,eta,epsilon,perm,r)
            key=(total,worst,z.weighted_distance,z.max_distance)
            if best is None or key<best[0]: best=(key,z,total,worst)
    return best[1],best[2],best[3]
