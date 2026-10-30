import yaml, re, os, sys, glob, collections

VAULT = "/home/tatdatnguyen/tatdat-vault"
os.chdir(VAULT)

def key(s):
    s = str(s).strip().strip('"').strip("'").strip("[]").split("|")[0].strip().strip("]")
    return s.removesuffix(".md")

def parts(t):
    if not t.startswith("---\n"): return "", t
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    return (m.group(1), t[m.end():]) if m else ("", t)

def vocab():
    v = set()
    for line in open("_meta/taxonomy.md"):
        s = line.strip()
        if s.startswith("- ") and ":" in s:
            v.update(x.strip().strip("`") for x in s.split(":", 1)[1].split(","))
        elif s.startswith("|") and not s.startswith("|-"):
            c = [x.strip().strip("`") for x in s.strip("|").split("|")]
            if len(c) >= 2: v.update(c[:2])
    return v

V = vocab()
CAN = {"related_to", "derived_from", "sees_also", "extends", "source_of", "duplicate_of", "conflicts_with"}
ALI = {}
for line in open("_meta/taxonomy.md"):
    s = line.strip()
    if s.startswith("|") and not s.startswith("|-"):
        c = [x.strip().strip("`") for x in s.strip("|").split("|")]
        if len(c) >= 2: ALI[c[0]] = c[1]

pages = [p.removesuffix(".md") for p in glob.glob("references/*.md") + glob.glob("concepts/*.md")]
P, ENT, TAG, TIER, SRC = {}, {}, {}, {}, {}
for p in pages:
    t = open(p + ".md", encoding="utf-8").read()
    f, b = parts(t)
    P[p] = t
    d = yaml.safe_load(f) or {}
    TAG[p] = d.get("tags") or []
    if isinstance(TAG[p], str): TAG[p] = [TAG[p]]
    ENT[p] = [(key(e.get("target", "")), str(e.get("type", "")).strip()) for e in (d.get("relationships") or []) if isinstance(e, dict)]
    SRC[p] = [str(x).strip().strip('"').strip("'").strip("[]").split("|")[0].strip() for x in (d.get("sources") or [])]
    TIER[p] = d.get("tier")

INC = collections.defaultdict(set)
for p in pages:
    for t, _ in ENT[p]: INC[t].add(p)
    for l in re.findall(r"\[\[([^\]]+)\]\]", parts(P[p])[1]): INC[key(l)].add(p)

res = collections.Counter()
tier_mis, alias_mis, taglist_mis, sidecar_mis, sources_hdr, nocal, nosec, pref, recip = [], [], [], [], [], [], [], [], []
for p in pages:
    b = parts(P[p])[1]
    inc = len(INC.get(key(p), set()))
    exp = "core" if inc >= 5 else ("peripheral" if inc == 1 else "supporting")
    if TIER[p] != exp: tier_mis.append((p, TIER[p], exp, inc)); res["tier"] += 1
    tg = TAG[p]
    raw = re.search(r"(?m)^tags:(?:[^\n]*(?:\n[ \t]+[^\n]*)*)", parts(P[p])[0])
    if not raw or not (raw.group(0) or "").strip().split(":", 1)[-1].strip().startswith("["): taglist_mis.append(p); res["tags-list"] += 1
    for x in tg:
        if x != x.lower() or x in ALI: alias_mis.append((p, x)); res["alias-case"] += 1
        if x not in V: res["tag-vocab"] += 1
    if len(tg) > 5: res["over-5-tags"] += 1
    ex = [s for s in SRC[p] if s.endswith("-extracted.md")]
    if ex and not any(s.endswith(".md") and not s.endswith("-extracted.md") and s.startswith("_papers/") for s in SRC[p]):
        sidecar_mis.append(p); res["sidecar-pair"] += 1
    if not re.search(r"^## Sources", b, re.M): sources_hdr.append(p); res["sources-header"] += 1
    if "[!tldr]" not in b: nocal.append(p); res["tldr-callout"] += 1
    d0 = yaml.safe_load(parts(P[p])[0]) or {}
    pr = d0.get("provenance_score") or {}
    dom = max(pr, key=lambda k: pr[k]) if pr else None
    amb = (d0.get("confidence_tiers") or {}).get("ambiguous") == max((d0.get("confidence_tiers") or {0:0}).values())
    mk = re.search(r"\^\[(extracted|inferred|ambiguous)\]", b)
    exp_mk = amb and "ambiguous" or dom or (mk.group(1) if (mk := re.search(r"\^\[(extracted|inferred|ambiguous)\]", b)) else "extracted")
    if not mk or mk.group(1) != exp_mk: nosec.append(p); res["marker-consistency"] += 1
    exp_call = {"extracted": "[!tldr]", "inferred": "[!note]", "ambiguous": "[!warning]"}[exp_mk]
    if exp_call not in b: nocal.append(p); res["callout"] += 1
    for t, ty in ENT[p]:
        if "/" not in t or t.split("/")[0] not in ("concepts", "references"): pref.append((p, t)); res["prefix-rule"] += 1
        if ty not in CAN: res["type"] += 1
        if t in ENT:
            back = [e for e in ENT[t] if e[0] == key(p)]
            if not back: recip.append((p, t, ty)); res["reciprocal"] += 1
    n = len([s for s in SRC[p] if s.endswith("-extracted.md")])
    expbc = min(1.0, 0.67 + 0.1 * (n - 1))
    if abs(float(yaml.safe_load(parts(P[p])[0])["base_confidence"]) - expbc) > 1e-9: res["base_confidence"] += 1

print("knowledge pages:", len(pages))
print("checks:", dict(res))
print("tier mismatches:", len(tier_mis))
for x in tier_mis[:12]: print("  ", x)
print("tags not a YAML list:", len(taglist_mis), taglist_mis[:6])
print("alias/case violations:", len(alias_mis), alias_mis[:10])
print("sidecar pairing missing:", len(sidecar_mis), sidecar_mis[:6])
print("missing ## Sources:", len(sources_hdr), sources_hdr[:6])
print("missing tldr callout:", len(nocal), nocal[:6])
print("missing inline marker:", len(nosec), nosec[:6])
print("prefix-rule violations:", len(pref), pref[:8])
print("unreciprocated:", len(recip), recip[:8])
print("distinct tags:", len(TAG) and len({t for v in TAG.values() for t in v}))

# tracker rules the gate misses
import datetime
single = collections.Counter(t for v in TAG.values() for t in v)
multi = {t for t, c in single.items() if c > 1 and t not in V}
print("tags in use but outside vocabulary:", len(multi), "| single-page tags needing alias:", sum(1 for t, c in single.items() if c == 1 and t not in V))
hot = open("hot.md").read()
secs = [s for s in re.split(r"(?m)^## ", hot)[1:]]
print("hot sections:", len(secs), "sections without a link (non-placeholder):", sum(1 for s in secs if not re.search(r"\[\[", s) and not s.strip().startswith("*")))
log = open("log.md").read()
ts = [m.group(1) for m in re.finditer(r"(?m)^-? ?\[(\d{4}-\d{2}-\d{2})", log)]
print("log entries:", len(ts), "out-of-order:", sum(1 for a, b in zip(ts, ts[1:]) if a > b))
idx = open("index.md").read()
print("hot sections:", len(secs), "sections without a link:", sum(1 for s in secs if not re.search(r"\[\[", s)))
print("index top-by-incoming section:", "Top pages by incoming links" in idx or "top by incoming" in idx.lower())
tax = open("_meta/taxonomy.md").read()
print("taxonomy sources field present:", bool(re.search(r"(?m)^sources:", tax)))
tier_counts = collections.Counter(TIER.values())
declared = yaml.safe_load(parts(tax)[0]).get("confidence_tiers")
print("tier counts actual:", dict(tier_counts), "declared:", declared)
idx_t = {key(m.group(1)) for m in re.finditer(r"(?m)^- ?\[\[([^\]|]+)", idx, re.M)}
topsec = (re.split(r"(?m)^## ", idx)[1:])
base = [s for s in topsec if s.startswith("Top by incoming")]
print("index entries:", len(idx_t), "| top-by-incoming baseline:", len(re.findall(r"(?m)^- \[\[", base[0])) if base else 0)
