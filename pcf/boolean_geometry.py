"""Exact Boolean sensitivity-graph analysis using only Python's standard library."""
from collections import Counter, deque
from dataclasses import dataclass
from math import sqrt

@dataclass(frozen=True)
class BooleanGeometry:
    n:int; mask:int; essential_variables:tuple; sensitive_edges:tuple
    degree_histogram:tuple; max_sensitivity:int; component_sizes:tuple
    active_component_sizes:tuple; matching_number:int
    active_diameters:tuple; spectral_radius:float
    @property
    def total_directed_sensitivity(self): return 2*len(self.sensitive_edges)
    @property
    def scalar_signature(self):
        return (len(self.essential_variables),len(self.sensitive_edges),
                self.max_sensitivity,self.degree_histogram)

def bit(mask,x): return (mask>>x)&1

def sensitivity_edges(n,mask):
    return tuple((x,x^(1<<i)) for x in range(1<<n) for i in range(n)
                 if x < (x^(1<<i)) and bit(mask,x)!=bit(mask,x^(1<<i)))

def essential_variables(n,mask):
    return tuple(i for i in range(n) if any(bit(mask,x)!=bit(mask,x^(1<<i))
                 for x in range(1<<n)))

def adjacency(n,edges):
    a=[set() for _ in range(1<<n)]
    for u,v in edges: a[u].add(v); a[v].add(u)
    return a

def components(adj,active_only=False):
    seen=set(); out=[]
    verts=[v for v in range(len(adj)) if adj[v] or not active_only]
    for s in verts:
        if s in seen: continue
        stack=[s]; seen.add(s); c=[]
        while stack:
            u=stack.pop(); c.append(u)
            for v in adj[u]:
                if v not in seen: seen.add(v); stack.append(v)
        out.append(c)
    return out

def diameter(adj,comp):
    if len(comp)<=1: return 0
    allowed=set(comp); best=0
    for s in comp:
        dist={s:0}; q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v in allowed and v not in dist:
                    dist[v]=dist[u]+1; q.append(v)
        best=max(best,max(dist.values()))
    return best

def maximum_matching_size(adj):
    active=tuple(v for v,nbr in enumerate(adj) if nbr)
    idx={v:i for i,v in enumerate(active)}
    nm=[0]*len(active)
    for v in active:
        for w in adj[v]:
            if w in idx: nm[idx[v]] |= 1<<idx[w]
    memo={0:0}
    def solve(rem):
        if rem in memo: return memo[rem]
        low=rem & -rem; i=low.bit_length()-1; rest=rem & ~low
        best=solve(rest); cand=nm[i]&rest
        while cand:
            j=cand & -cand
            best=max(best,1+solve(rest & ~j)); cand &= ~j
        memo[rem]=best; return best
    return solve((1<<len(active))-1)

def spectral_radius(adj,iterations=200):
    nv=len(adj)
    if not any(adj): return 0.0
    x=[1/sqrt(nv)]*nv; lam2=0.0
    for _ in range(iterations):
        ax=[sum(x[j] for j in adj[i]) for i in range(nv)]
        y=[sum(ax[j] for j in adj[i]) for i in range(nv)]
        norm=sqrt(sum(v*v for v in y))
        if norm==0: return 0.0
        x=[v/norm for v in y]
        ax=[sum(x[j] for j in adj[i]) for i in range(nv)]
        a2=[sum(ax[j] for j in adj[i]) for i in range(nv)]
        lam2=sum(x[i]*a2[i] for i in range(nv))
    return sqrt(max(lam2,0.0))

def analyze(n,mask):
    edges=sensitivity_edges(n,mask); adj=adjacency(n,edges)
    deg=[len(x) for x in adj]; comps=components(adj); active=components(adj,True)
    return BooleanGeometry(n,mask,essential_variables(n,mask),edges,
        tuple(sorted(Counter(deg).items())),max(deg,default=0),
        tuple(sorted((len(c) for c in comps),reverse=True)),
        tuple(sorted((len(c) for c in active),reverse=True)),
        maximum_matching_size(adj),
        tuple(sorted((diameter(adj,c) for c in active),reverse=True)),
        spectral_radius(adj))

def truth_set(n,mask):
    return tuple(format(x,f"0{n}b") for x in range(1<<n) if bit(mask,x))

def enumerate_functions(n):
    for mask in range(1<<(1<<n)): yield analyze(n,mask)

def find_geometry_separations(n):
    groups={}
    for g in enumerate_functions(n): groups.setdefault(g.scalar_signature,[]).append(g)
    for sig,members in groups.items():
        geometries={}
        for g in members:
            key=(g.active_component_sizes,g.matching_number,g.active_diameters,round(g.spectral_radius,10))
            geometries.setdefault(key,[]).append(g)
        if len(geometries)>1: yield sig,geometries
