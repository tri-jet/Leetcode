class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # dict for values and powers
        # get keys, then sort key list
        # then get value associated with key value at k
        powerDict = {}
        for i in range(lo, hi+1):
            current = i
            steps = 0
            while(i != 1):
                if i%2==0:
                    i /= 2
                else: i = 3*i + 1
                steps += 1
            powerDict[current] = steps
          
        keysList = list(powerDict.keys())
        keysList.sort()
        return powerDict.get(keysList[k])
