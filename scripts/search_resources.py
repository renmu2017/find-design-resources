#!/usr/bin/env python3
"""Search the bundled design-resource index locally, using Python stdlib only."""

import argparse
import json
import re
import unicodedata
from pathlib import Path

INDEX_PATH = Path(__file__).resolve().parents[1] / "references" / "resources.json"


def normalize(value):
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def mentioned(term, query):
    term = normalize(term)
    if re.search(r"[\u3400-\u9fff]", term):
        return term in query
    return re.search(r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])", query) is not None


def rank(resource, query):
    if not query:
        return 1, []
    hits = list(dict.fromkeys(word for word in resource["keywords"] if mentioned(word, query)))
    score = 4 * len(hits)
    for name in (resource["name"], resource["id"]):
        if mentioned(name, query):
            score += 12
            hits.append(name)
    return score, list(dict.fromkeys(hits))


def positive_int(value):
    parsed = int(value)
    if parsed < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return parsed


def main():
    catalog = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    resources = catalog["resources"]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="?", default="", help="Chinese or English keywords; omit to list")
    parser.add_argument("--kind", choices=sorted({k for r in resources for k in r["kinds"]}))
    parser.add_argument("--format", choices=sorted({f for r in resources for f in r["formats"]}))
    parser.add_argument("--limit", type=positive_int, default=5)
    parser.add_argument("--json", action="store_true", help="Print machine-readable results")
    args = parser.parse_args()
    query = normalize(args.query)
    matches = []
    for resource in resources:
        if args.kind and args.kind not in resource["kinds"]:
            continue
        if args.format and args.format not in resource["formats"]:
            continue
        score, hits = rank(resource, query)
        if score:
            matches.append({**resource, "score": score, "matched_keywords": hits})
    matches.sort(key=lambda r: (-r["score"], r["order"]))
    result = {
        "reviewed_at": catalog["reviewed_at"],
        "query": args.query,
        "filters": {"kind": args.kind, "format": args.format},
        "total_matches": len(matches),
        "results": matches[: args.limit],
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    print(f"资料核验日期：{catalog['reviewed_at']}；本地关键词检索，未实时访问网站。")
    if not matches:
        print("没有匹配项。换成页面、控件或动作关键词；索引未收录的需求需另外搜索。")
        return
    for number, resource in enumerate(result["results"], 1):
        print(f"\n{number}. {resource['name']} — {resource['summary']}")
        print(f"   {resource['url']}")
        print(f"   用途：{', '.join(resource['kinds'])}；形式：{', '.join(resource['formats'])}")
        print(f"   访问/授权：{resource['access_note']}")
        print(f"   资料：{resource['reference']}；资源 ID：{resource['id']}")
        if resource["matched_keywords"]:
            print(f"   命中：{', '.join(resource['matched_keywords'])}")


if __name__ == "__main__":
    main()
