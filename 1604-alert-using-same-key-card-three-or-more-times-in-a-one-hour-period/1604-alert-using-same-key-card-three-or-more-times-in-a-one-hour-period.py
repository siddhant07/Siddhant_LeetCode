class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        mapp = defaultdict(list)
        names = []

        for (name, time) in zip(keyName, keyTime):
            mapp[name].append(time)

        diff = 61       
        for m in mapp:
            times = sorted(mapp[m])

            for i in range(2, len(times)):
                firstTime = times[i-2].split(":")
                lastTime = times[i].split(":")                

                
                diff = (int(lastTime[0]) * 60 + int(lastTime[1])) - (int(firstTime[0]) * 60 + int(firstTime[1]))
                if diff <= 60:
                    names.append(m)
                    

        return sorted(set(names))