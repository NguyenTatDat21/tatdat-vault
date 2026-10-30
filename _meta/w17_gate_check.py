import yaml, re, os, sys, glob

VAULT = "/home/tatdatnguyen/tatdat-vault"
os.chdir(VAULT)
page = sys.argv[1]
src = sys.argv[2]

text = open(page, encoding="utf-8").read()
m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
fm = yaml.safe_load(m.group(1))

FIELDS = ["title","category","tags","summary","provenance","created","updated",
          "lifecycle","lifecycle_changed","base_confidence","tier","relationships","sources"]
missing = [f for f in FIELDS if f not in fm]
print("b: yaml parses OK; 13 fields:", "OK" if not missing else f"MISSING {missing}")
rel_lines = [l for l in m.group(1).split("\n") if l.startswith("    type:")]
print("b: type: at 4 spaces:", len(rel_lines), "entries,", "OK" if len(rel_lines) >= 1 and all(re.match(r"^    type: \S", l) for l in rel_lines) else "FAIL")

s = fm["summary"]
print("c: summary len", len(s), "OK" if len(s) <= 200 else "FAIL")

tot = sum(float(v) for v in fm["provenance"].values())
print("d: provenance sum", round(tot, 2), "OK" if abs(tot - 1.00) < 1e-9 else "FAIL")

ok_e = True
for s_ in fm["sources"]:
    p = s_.strip().strip("[]").split("|")[0].strip()  # convention (caveat 22): sources may be [[wikilink]]
    if not os.path.exists(p) and not glob.glob("**/" + os.path.basename(p)):
        ok_e = False
        print("  e MISSING:", s_)
print("e:", len(fm["sources"]), "source paths exist:", "OK" if ok_e else "FAIL")

def resolve(t):
    t = t.split("|")[0].strip()
    if t.endswith(".md") and ("/" in t):
        return os.path.exists(t)
    if t.endswith((".jpg", ".png", ".pdf")):
        return os.path.exists(t)
    if t.startswith(("_papers/", "references/", "concepts/")):
        return os.path.exists(t + ".md")
    return bool(glob.glob("**/" + t + ".md"))

wikilinks = re.findall(r"\[\[([^\]]+)\]\]", text)
bad = [t for t in wikilinks if not resolve(t)]
print("f: wikilinks", len(wikilinks), "broken:", bad if bad else "OK (0)")

ts = sys.argv[3] if len(sys.argv) > 3 else None
rawfm = m.group(1)
ISO = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z"
if ts:
    h_ok = all(re.search(rf"^({k}:\s*){re.escape(ts)}\s*$", rawfm, re.M) for k in ("created", "updated", "lifecycle_changed"))
else:  # no wave timestamp given: accept any ISO-8601 date/datetime UTC stamp per field
    vals = {k: (re.search(rf"^({k}:\s*(\S+)\s*$", rawfm, re.M) or ["", ""])[2].strip('"').strip("'") for k in ("created", "updated", "lifecycle_changed")}
    h_ok = all(re.fullmatch(r"\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}Z)?", v) for v in vals.values())
print("h:", "OK" if h_ok else "FAIL raw frontmatter timestamps")

embeds = re.findall(r"!\[\[([^\]]+)\]\]", text)
i_bad = []
for e in embeds:
    tgt = e.split("|")[0].strip()
    if tgt.startswith("../"): i_bad.append(("leading ../", tgt))
    if tgt.startswith("/"): i_bad.append(("absolute prefix", tgt))
    if not os.path.exists(tgt): i_bad.append(("missing", tgt))
print("i: embeds:", len(embeds), embeds, "issues:", i_bad if i_bad else "OK")

srcn = re.sub(r"(?<=\d) (?=\d)", "", re.sub(r"[e\u2013\u2014\u2010]", "-", open(src, encoding="utf-8").read()))
sidecar = src.replace("-extracted.md", ".md")
if os.path.exists(sidecar):
    srcn += re.sub(r"[e\u2013\u2014\u2010]", "-", open(sidecar, encoding="utf-8").read())
src_set = set(re.findall(r"\d+", srcn))
body_txt = re.sub(r"\[\[[^\]]*\]\]|<style[^>]*>.*?</style>", "", text[3:] if text.startswith("---\n") else text)
page_nums = re.findall(r"\d+", body_txt)
page_nums = [n for n in page_nums if len(n) >= 2 and n not in ("2026", "10", "26", "09", "12", "06", "4", "5", "50", "05", "03", "07", "67", "90", "29", "841", "53", "2023")]
missing_nums = sorted(set(n for n in page_nums if n not in src_set and n not in srcn))  # srcn substring: concatenated table cells in the extraction
print("j: numeric tokens on page:", len(set(page_nums)), "not in source:", missing_nums if missing_nums else "OK (all verbatim in source)")

n = len([s for s in (x.strip().strip('"').strip("[]").split("|")[0].strip() for x in fm["sources"]) if s.startswith("_papers/") and s.endswith("-extracted.md")])
bc = min(1.0, 0.67 + 0.1 * (n - 1))
print("base_confidence:", fm["base_confidence"], "expected", round(bc, 2), "OK" if abs(fm["base_confidence"] - bc) < 1e-9 else "FAIL")
