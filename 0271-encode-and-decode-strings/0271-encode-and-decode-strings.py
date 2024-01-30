class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        s = ''
        for i in strs:
            a = ' '.join(str(ord(c)) for c in i)
            s = s + '_' + a
        
        return s

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        buffer = s.split('_')
        strs = [''] * (len(buffer) - 1)
        
        
        for i in range(1, len(buffer)):
            buffer2 = buffer[i].split(' ')
            
            if len(buffer2)==1 and buffer2[0] == '':
                strs[i-1] = ''
            else:
                strs[i-1] = ''.join(chr(int(j)) for j in buffer2)
            
        return strs
            
        
        
        
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))