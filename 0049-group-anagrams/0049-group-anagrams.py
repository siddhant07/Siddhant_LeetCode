class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = {}
        
        for i in strs:
            ss = ''.join(sorted(i))
            
            if ss not in solution:
                solution[ss] = [i]
            else:
                solution[ss].append(i)
        
        return solution.values()