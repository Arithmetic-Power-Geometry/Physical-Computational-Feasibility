"""Deterministic multi-seed n=5 campaign with persistent machine-readable results."""
import argparse,csv,json,time
from pathlib import Path
from scripts.search_n5 import search

def run_campaign(samples,seeds,base_seed):
    rows=[]; witnesses=[]
    for j in range(seeds):
        seed=base_seed+j
        t0=time.time(); r=search(n=5,samples=samples,seed=seed)
        row={
            "seed":seed,"requested_samples":samples,"unique_canonical":r["unique"],
            "cheap_buckets":r["cheap_buckets"],"cheap_collisions":r["cheap_collisions"],
            "strong_separations":len(r["strong_separations"]),
            "seconds":round(time.time()-t0,6),
        }
        rows.append(row)
        for sk,items in r["strong_separations"]:
            witnesses.append({"seed":seed,"summary":repr(sk),"items":repr(items)})
    return rows,witnesses

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--samples",type=int,default=5000)
    ap.add_argument("--seeds",type=int,default=4)
    ap.add_argument("--base-seed",type=int,default=20260929)
    ap.add_argument("--out",default="artifacts/n5_campaign")
    a=ap.parse_args()
    out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
    rows,witnesses=run_campaign(a.samples,a.seeds,a.base_seed)
    with (out/"summary.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    manifest={"n":5,"samples_per_seed":a.samples,"seeds":a.seeds,
              "base_seed":a.base_seed,"rows":rows,"witnesses":witnesses}
    (out/"manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    print(json.dumps(manifest,indent=2))

if __name__=="__main__": main()
