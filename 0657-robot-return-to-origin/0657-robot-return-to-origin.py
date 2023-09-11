class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        cv = 0
        ch = 0
        for i in moves:
            if i == 'U':
                cv+=1
            elif i == 'D':
                cv-=1
            elif i == 'R':
                ch+=1
            elif i == 'L':
                ch-=1
            
        if cv == 0 and ch == 0:
            return True
        else:
            return False
        