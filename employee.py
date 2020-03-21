

class Employee:
    """
    Employee Stuff
    """
    def __init__(self, attributes):
        self._timestamp= attributes[1]
        self._netid= attributes[2]
        self._name= attributes[3]
        self._weekhours= attributes[4]
        self._dayhours= attributes[5]
        self._prefer= attributes[6].split()
        self._noway = attributes[7].split()

        self._shifts= None
        #self._available= attributes[7]
        #self._misc= attributes[7]

        #self._picky= len(self.available)

    def empAssign(self, this_shft):
        if len(self.getShifts())<self.getWeekHours() & len(self.getShiftToday())<self.getDayHours():
            self._shifts.append(this_shift)
        else:
            raise InputError('Too many shifts for this employee')

    def empUnassign(self, this_shft):
        if this_shft in self._shifts:
            self._shifts.remove(this_shft)
        else:
            raise InputError('Cannot remove shift not assigned')

    def getTime(self):
        return self._timestamp

    def getNetID(self):
        return self._netid

    def getName(self):
        return self._name

    def getWeekHours(self):
        return self._weekhours

    def getDayHours(self):
        return self._dayhours

    def getPrefer(self):
        return self._prefer

    def getNoWay(self):
        return self._noway

    def getAvail(self):
        return self._available

    def getMisc(self):
        return self._misc

    def getPicky(self):
        return self._picky

    def getShifts(self):
        return self._shifts
