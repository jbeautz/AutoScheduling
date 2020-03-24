from shift import txt2ShiftList

class Employee:
    """
    Defines an employee object.

    timestamp: when employee filled out preference form
    netid: cornell netid of employee
    name: name of employee
    weekhours: requested number of hours per week
    dayhours: requested max number of hours per day
    prefer: requested shifts
    noway: shifts employee cannot work
    shifts: assigned shifts
    """
    def __init__(self, attributes):
        self._timestamp= attributes[1]
        self._netid= attributes[2]
        self._name= attributes[3]
        self._weekhours= attributes[4]
        self._dayhours= attributes[5]
        self._prefer= txt2ShiftList(attributes[6])
        self._noway = txt2ShiftList(attributes[7])

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
