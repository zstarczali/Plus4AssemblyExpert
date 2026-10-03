import re, sys, collections
def offsets(path):
    t = open(path, encoding='utf-8').read()
    parts = re.split(r'^--- PAGE (\d+) ---$', t, flags=re.M)
    c = collections.Counter(); per = {}
    for i in range(1, len(parts), 2):
        n = int(parts[i]); lines = [l.strip() for l in parts[i+1].strip().splitlines() if l.strip()]
        cand = lines[:2] + lines[-2:]
        for l in cand:
            for m in re.findall(r'(?:^|\s)(\d{1,3})(?:\s|$)', l):
                v = int(m)
                if 0 < v <= n:
                    c[n - v] += 1
    return c.most_common(4)
for p in sys.argv[1:]:
    print(p, offsets(p))
