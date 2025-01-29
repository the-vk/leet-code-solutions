class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graphs = []
        for f, t in edges:
            if len(graphs) == 0:
                graphs.append(set([f, t]))
                continue
            f_i = None
            t_i = None
            for i, g in enumerate(graphs):
                if f in g and t in g:
                    return [f, t]
                if f in g:
                    f_i = i
                if t in g:
                    t_i = i
            if f_i == None and t_i == None:
                graphs.append(set([f, t]))
                continue
            if f_i != None and t_i != None:
                graphs[f_i].update(graphs[t_i])
                graphs.pop(t_i)
                continue
            if f_i != None:
                graphs[f_i].add(t)
            if t_i != None:
                graphs[t_i].add(f)
            
            
                
