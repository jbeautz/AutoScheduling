class Shift:
    """
    Shift stuff
    """
    def __init__(self, day, start, needed, prefer=None, noway=None, available=None, assigned=None):
        self._day= day,
        self._start= start
        self._end= start+2
        self._needed = needed
        self._prefer= prefer
        self._noway= noway
        self._available = available
        self._assigned= assigned


    def assign(self):
        if len(self.getAssigned())<self.getNeeded():
            try:
                emp= bestAssign(self.getPrefer(), self.getAvail())
                emp.empAssign(this_shft)
            except:
                prefer.remove(emp)
                emp= bestAssign(self.getPrefer(), self.getAvail())
        else:
            assigned.remove(self.drop())
            emp.empUnassign(self)
            self.assign(self.getPrefer(), self.getAvail())

    def drop(self):
        """
        remove most easily removed
        """

    def bestAssign():
        """
        assign best possible employees
        """




    def getDay():
        return self._day

    def getStart():
        return self._start

    def getEnd():
        return self._end

    def getAssigned():
        return self._assigned

    def getAvail():
        return self._available

    def getPrefer():
        return self._prefer

    def getNoWay():
        return self._noway


def readShftTxt(filename):
    ShiftList = []
    file = open(filename, "r")
    for aline in file:
        values = aline.split()
        ShiftList.append(Shift(values))
    file.close()
    return ShiftList
