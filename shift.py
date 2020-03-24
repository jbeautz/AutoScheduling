class Shift:
    """
    Defines shift object to be worked.

    day: day of the week the shift falls on
    time: beginning and end time of the shift
    needed: number employees needed on shift
    available: list of employees free to work during shift
    assigned: list of employees assigned to shift
    """
    def __init__(self, day, time, needed=0, available=None, assigned=None):
        self._day= day
        self._time= time
        self._needed = needed
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

    def getTime():
        return self._time

    def getAssigned():
        return self._assigned

    def getAvail():
        return self._available

    def getPrefer():
        return self._prefer

    def getNoWay():
        return self._noway

    def getNeeded():
        return self._needed


def readShftTxt(filename):
    ShiftList = []
    file = open(filename, "r")
    for aline in file:
        values = aline.split()
        ShiftList.append(Shift(values[0],values[1],values[2]))
    file.close()
    return ShiftList

def txt2ShiftList(txt):
    txtlist= txt.split()
    shftlst= []
    for i in range(len(txtlist)/2):
        shftlst.append(Shift(txtlist[i],txtlist[i+1]))
    return shftlst
