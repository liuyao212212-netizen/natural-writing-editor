#!/usr/bin/env python3
"""Flag common clarity and naturalness problems in Chinese and English prose."""
from __future__ import annotations
import argparse, json, re
from collections import Counter
from pathlib import Path

PATTERNS = {
 "empty_intro": [r"众所周知", r"在当今.{0,12}(时代|社会|世界)", r"毋庸置疑", r"As we all know", r"In today'?s .{0,20} world"],
 "inflated": [r"赋能", r"抓手", r"闭环", r"全面提升", r"极大地", r"revolutionary", r"game[- ]changer", r"unprecedented"],
 "vague_source": [r"有研究(表明|显示)", r"业内人士认为", r"数据显示", r"experts say", r"studies show", r"research suggests"],
 "formulaic": [r"值得注意的是", r"综上所述", r"总而言之", r"不仅.{0,30}而且", r"It is worth noting", r"In conclusion", r"delve into", r"a testament to"],
 "hedging": [r"可能在一定程度上", r"某种意义上", r"perhaps potentially", r"arguably may"]
}

def audit(text: str) -> list[dict]:
    findings=[]
    for category, patterns in PATTERNS.items():
        for pattern in patterns:
            for match in re.finditer(pattern, text, flags=re.I):
                findings.append({"category":category,"text":match.group(0),"start":match.start(),"suggestion":"Verify meaning, then replace with a concrete claim or remove."})
    sentences=[s.strip() for s in re.split(r"[。！？!?\.]+", text) if s.strip()]
    openings=Counter(s[:6].lower() for s in sentences if len(s)>=6)
    for opening,count in openings.items():
        if count>=3: findings.append({"category":"repeated_opening","text":opening,"count":count,"suggestion":"Vary sentence openings or combine repetitive points."})
    if text.count("**") >= 8: findings.append({"category":"formatting","text":"**","count":text.count("**"),"suggestion":"Reduce bold emphasis; let structure carry importance."})
    emoji=re.findall(r"[\U0001F300-\U0001FAFF]", text)
    if len(emoji)>=4: findings.append({"category":"formatting","text":"emoji","count":len(emoji),"suggestion":"Keep only channel-appropriate emoji."})
    return findings

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("--format",choices=["json","markdown"],default="json"); p.add_argument("--output",type=Path)
    a=p.parse_args(); findings=audit(a.input.read_text(encoding="utf-8"))
    if a.format=="json": result=json.dumps({"finding_count":len(findings),"findings":findings},ensure_ascii=False,indent=2)+"\n"
    else:
        rows=["# Style audit","",f"Findings: {len(findings)}",""]
        rows += [f'- **{x["category"]}**: `{x["text"]}` — {x["suggestion"]}' for x in findings]
        result="\n".join(rows)+"\n"
    if a.output: a.output.write_text(result,encoding="utf-8")
    else: print(result,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
