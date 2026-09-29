#!/usr/bin/env python3
import argparse,csv
from pathlib import Path
from pcf.boolean_geometry import find_geometry_separations,truth_set
def main():
    p=argparse.ArgumentParser(); p.add_argument("--n",type=int,default=4)
    p.add_argument("--output",type=Path); p.add_argument("--limit",type=int,default=20); a=p.parse_args()
    rows=[]
    for sig,geoms in find_geometry_separations(a.n):
        reps=[m[0] for m in geoms.values()]
        for i in range(len(reps)):
            for j in range(i+1,len(reps)):
                x,y=reps[i],reps[j]
                rows.append({"n":a.n,"mask_a":x.mask,"mask_b":y.mask,
                  "essential":len(x.essential_variables),"sensitive_edges":len(x.sensitive_edges),
                  "max_sensitivity":x.max_sensitivity,"degree_histogram":repr(x.degree_histogram),
                  "components_a":repr(x.active_component_sizes),"components_b":repr(y.active_component_sizes),
                  "matching_a":x.matching_number,"matching_b":y.matching_number,
                  "diameters_a":repr(x.active_diameters),"diameters_b":repr(y.active_diameters),
                  "spectral_a":f"{x.spectral_radius:.12g}","spectral_b":f"{y.spectral_radius:.12g}",
                  "ones_a":" ".join(truth_set(a.n,x.mask)),"ones_b":" ".join(truth_set(a.n,y.mask))})
                if len(rows)>=a.limit: break
            if len(rows)>=a.limit: break
        if len(rows)>=a.limit: break
    if a.output and rows:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        with a.output.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    else:
        for r in rows: print(r)
if __name__=="__main__": main()
