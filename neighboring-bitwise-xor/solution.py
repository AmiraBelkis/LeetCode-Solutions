class Solution:        
    def doesValidArrayExist(self, derived: List[int]):
        original = None
        for bit in derived:
            if bit is not 1 and bit is not 0:
                return False
            if original is None:
                original = [0,1] if bit is 1 else [0,0] 
            else:
                original.append(original[-1] if bit is 0 else abs(original[-1]-1))
        return (original[-1] is original[0])
