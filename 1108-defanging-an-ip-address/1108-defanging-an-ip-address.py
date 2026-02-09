class Solution:
    def defangIPaddr(self, address: str) -> str:
        summer = address.split(".")
        print (summer)

        return summer[0]+"[.]"+summer[1]+"[.]"+summer[2]+"[.]"+summer[3]
        