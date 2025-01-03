class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            minLen = min(len(w1),len(w2))
            if(len(w1) > len(w2) and w1[0:minLen] == w2[0:minLen]):
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        res = []
        print(adj)
        def dfs(k):
            if k in visit:
                return visit[k]
            print(visit)
            visit[k] = True
            for nri in adj[k]:
                if dfs(nri):
                    return True
            res.append(k)
            visit[k] = False
        for c in adj:
            print(c)
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)      

