import argparse,csv,json
from collections import defaultdict

def summarize(data):
    names={c["id"]:c["name"] for c in data.get("categories",[])}
    groups=defaultdict(lambda:[0,0.0,set()])
    for a in data["annotations"]:
        item=groups[a["category_id"]]; item[0]+=1
        box=a.get("bbox",[0,0,0,0]); item[1]+=float(box[2])*float(box[3]); item[2].add(a["image_id"])
    return [{"category":names.get(k,str(k)),"instances":v[0],"images":len(v[2]),
             "mean_box_area":round(v[1]/v[0],2)} for k,v in sorted(groups.items())]

def main():
    p=argparse.ArgumentParser(); p.add_argument("input");p.add_argument("output");a=p.parse_args()
    rows=summarize(json.load(open(a.input,encoding="utf-8")))
    with open(a.output,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["category","instances","images","mean_box_area"])
        w.writeheader();w.writerows(rows)
if __name__=="__main__":main()

