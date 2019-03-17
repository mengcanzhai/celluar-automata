class Cell(object):
    def __init__(self,location,rule,value,vision):
        self.location = location
        self.rule = rule
        self.value = value
        self.vision = vision
        self.visionInput = 0 if((self.location-self.vision)>=0) else 1

    #传入有端点的一维元胞数组，获得视野内元胞状态
    def getVision(self,cellList):
        cellVision = []
        _min = self.location - self.vision
        _l = self.vision * 2 + 1
        for i in range(_l):
            if (_min + i) < 0 or (_min + i) >= len(cellList):
                cellVision.append(-1)
            else:
                cellVision.append(cellList[_min + i])
        return cellVision
    #计算元胞值
    def calculate(self,visionList,inputInfo,ignoreEdge=1):
        if ignoreEdge == 1:
            _str = ''
            for i in visionList:
                if i == -1:
                    _str += '0'
                else:
                    _str += str(i)
            self.value = rule[_str][self.visionInput*inputInfo]
        else:
            _str = ''
            for i in visionList:
                _str += str(i)
            self.value = rule[_str][self.visionInput*inputInfo]

#class CellRule(object):
