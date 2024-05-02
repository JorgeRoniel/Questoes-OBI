def comp(a, b):
    return a['w'] - b['w']

e = []

def makeset(a):
    set[a] = a

def find(a):
    return set[a]

def unite(a, b):
    bs = set[b]
    as_ = set[a]
    for i in range(1, N + 1):
        if set[i] == bs:
            set[i] = as_

N, F, R = map(int, input().split())

for i in range(F + R):
    p, q, w = map(int, input().split())
    if i < F:
        e.append({'p': p, 'q': q, 'w': w})
    else:
        e.append({'p': p, 'q': q, 'w': w + 1000})

e.sort(key=lambda x: x['w'])

set = [0] * (N + 1)
for i in range(1, N + 1):
    makeset(i)

ans = i = j = 0

while j < N - 1:
    p = e[i]['p']
    q = e[i]['q']
    if find(p) != find(q):
        ans += e[i]['w'] if e[i]['w'] < 1001 else e[i]['w'] - 1000
        unite(p, q)
        j += 1
    i += 1

print(ans)
