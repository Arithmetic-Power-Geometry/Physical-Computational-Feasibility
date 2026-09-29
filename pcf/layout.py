"""Exact small graph-layout experiments for sensitivity graphs."""
from itertools import permutations
from pcf.boolean_geometry import analyze

def active_vertices(n,mask):
    g=analyze(n,mask)
    return tuple(sorted({u for e in g.sensitive_edges for u in e}))

def minimum_linear_arrangement(n,mask):
    """Exact MinLA on active sensitivity-graph vertices.

    Cost = sum over sensitive edges of absolute position difference.
    Intended only for tiny witnesses.
    """
    g=analyze(n,mask); verts=active_vertices(n,mask)
    idx={v:i for i,v in enumerate(verts)}
    edges=tuple((idx[u],idx[v]) for u,v in g.sensitive_edges)
    k=len(verts)
    best=None; best_perm=None
    # Fix reversal symmetry by requiring first label position < last label position.
    for perm in permutations(range(k)):
        if perm[0] > perm[-1]: continue
        pos=[0]*k
        for p,v in enumerate(perm): pos[v]=p
        cost=sum(abs(pos[u]-pos[v]) for u,v in edges)
        if best is None or cost<best:
            best=cost; best_perm=perm
    return best,best_perm

def fixed_hypercube_coordinate_wirelength(n,mask):
    """Wirelength if Boolean states retain their natural n-cube embedding.
    Every sensitivity edge is one cube edge, so this intentionally collapses
    to sensitive-edge count and serves as a control.
    """
    return len(analyze(n,mask).sensitive_edges)
