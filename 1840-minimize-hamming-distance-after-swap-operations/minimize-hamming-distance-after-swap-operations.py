class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)
        parent = list(range(n))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(a, b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pa] = pb
        for a, b in allowedSwaps:
            union(a, b)
        m = {}
        for i in range(n):
            p = find(i)
            if p not in m:
                m[p] = []
            m[p].append(i)
        ans = 0
        
        for g in m.values():
            c = {}
            for i in g:
                v = source[i]
                if v not in c:
                    c[v] = 0
                c[v] += 1
            for i in g:
                v = target[i]
                if v in c and c[v] > 0:
                    c[v] -= 1
                else:
                    ans += 1
        
        return ans