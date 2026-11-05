"""Evaluate recorded HTTP responses against JSON expectations (offline)."""
import argparse
import json
import sys

def evaluate(cases):
    if not isinstance(cases,list): raise ValueError("cases must be a list")
    results=[]
    for i,case in enumerate(cases):
        if not isinstance(case,dict): raise ValueError("each case must be an object")
        actual=case.get("actual",{})
        expected=case.get("expected",{})
        if not isinstance(actual,dict) or not isinstance(expected,dict): raise ValueError("actual/expected must be objects")
        failures=[]
        if "status" in expected and actual.get("status")!=expected["status"]: failures.append("status")
        for field in ("headers","body"):
            wanted=expected.get(field,{})
            observed=actual.get(field,{})
            if not isinstance(wanted,dict) or not isinstance(observed,dict): raise ValueError("headers/body must be objects")
            for key,value in wanted.items():
                if observed.get(key)!=value: failures.append(field+"."+key)
        results.append({"name":case.get("name",str(i+1)),"passed":not failures,"failures":failures})
    return {"total":len(results),"passed":sum(x["passed"] for x in results),"results":results}

def main(argv=None):
    p=argparse.ArgumentParser(description="Evaluate recorded API responses")
    p.add_argument("cases",help="JSON file containing a list of cases")
    args=p.parse_args(argv)
    try:
        with open(args.cases,encoding="utf-8") as f: data=json.load(f)
        result=evaluate(data)
    except (OSError,ValueError,TypeError) as exc:
        print(str(exc),file=sys.stderr)
        return 2
    print(json.dumps(result,indent=2))
    return 0 if result["passed"]==result["total"] else 1
if __name__=="__main__": raise SystemExit(main())
