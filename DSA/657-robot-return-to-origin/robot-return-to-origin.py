class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hmap = {"L":0, "R":0, "U":0, "D":0}
        for i in moves:
            if i == "L" and hmap["R"]==0:
                hmap[i]+=1
            elif i =="L" and hmap["R"]>0:
                hmap["R"]-=1
            elif i == "R" and hmap["L"]==0:
                hmap[i] +=1
            elif i == "R" and hmap["L"]>0:
                hmap["L"] -=1
            elif i == "U" and hmap["D"]==0:
                hmap[i]+=1
            elif i =="U" and hmap["D"]>0:
                hmap["D"]-=1
            elif i == "D" and hmap["U"]==0:
                hmap[i] +=1
            elif i == "D" and hmap["U"]>0:
                hmap["U"] -=1
        print(hmap)
        for i in hmap.values():
            if i is not 0:
                return False
        return True