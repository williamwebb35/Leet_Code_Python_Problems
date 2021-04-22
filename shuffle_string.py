class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = tuple(zip(s,indices))
        t = list(t)
        t_sorted = sorted(t,key = lambda x: x[1]) 
        new_order = ''.join([i[0] for i in t_sorted])
        return(new_order)
        
