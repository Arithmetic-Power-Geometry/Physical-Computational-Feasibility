"""Shared-capacity protection models on a Boolean sensitivity graph.

A round may protect a set of sensitive transitions subject to an explicit
resource-sharing rule. These models test whether residual graph geometry has
operational consequences beyond scalar/spectral sensitivity summaries.
"""
from dataclasses import dataclass
from pcf.boolean_geometry import analyze, adjacency

@dataclass(frozen=True)
class CapacityResult:
    mask:int
    edge_capacity:int
    matching_number:int
    matching_round_lower_bound:int
    exact_edge_coloring_rounds:int

def _edge_coloring_number_bipartite(n,mask):
    """Sensitivity graphs are subgraphs of the hypercube and hence bipartite.
    By Konig's line-coloring theorem, edge chromatic number equals max degree.
    """
    g=analyze(n,mask)
    return g.max_sensitivity

def shared_endpoint_capacity(n,mask,edge_capacity=1):
    """One physical state may participate in at most one protected sensitive
    transition per round. With edge_capacity parallel protection units, return
    basic operational quantities.

    The endpoint-conflict scheduling problem is edge coloring. Since every
    sensitivity graph is bipartite, exact rounds = maximum sensitivity.
    """
    if edge_capacity < 1:
        raise ValueError("edge_capacity must be positive")
    g=analyze(n,mask)
    # If there are B identical global units as well as endpoint exclusion,
    # at least ceil(|E|/B) rounds and at least Delta rounds are necessary.
    global_bound=(len(g.sensitive_edges)+edge_capacity-1)//edge_capacity
    exact_without_global_cap=_edge_coloring_number_bipartite(n,mask)
    rounds=max(global_bound,exact_without_global_cap)
    return CapacityResult(mask,edge_capacity,g.matching_number,
        (len(g.sensitive_edges)+max(g.matching_number,1)-1)//max(g.matching_number,1),
        rounds)

def component_serial_rounds(n,mask):
    """Toy model: disconnected active components share one exclusive global
    refresh controller and must be serviced serially; within each component,
    endpoint-conflicting edges are scheduled by edge coloring.

    This is intentionally model-specific and is not asserted as a universal
    physical law.
    """
    g=analyze(n,mask)
    adj=adjacency(n,g.sensitive_edges)
    seen=set(); total=0; per=[]
    for s in range(1<<n):
        if s in seen or not adj[s]: continue
        stack=[s]; seen.add(s); comp=[]
        while stack:
            u=stack.pop(); comp.append(u)
            for v in adj[u]:
                if v not in seen: seen.add(v); stack.append(v)
        delta=max(len(adj[u]) for u in comp)
        per.append(delta); total+=delta
    return total,tuple(sorted(per,reverse=True))
