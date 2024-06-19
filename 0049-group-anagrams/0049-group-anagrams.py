class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        
        for i in strs:
            gl = ''.join(sorted(i))
            if gl in answer:
                answer[gl].append(i)
            else:
                answer[gl] = [i]
        
        return answer.values()