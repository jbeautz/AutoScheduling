from ReadForm import readForm
from opt_mkdat import mkdat
from employee import Employee
from shift import Shift, readShftTxt
from w2wtest import getW2W
import pandas as pd
from amplpy import AMPL, DataFrame, Environment

employees = readForm().to_records()
employeeList = []

for emp in employees:
    employeeList.append(Employee(emp))

#print(example.getDayHours())
ampl = AMPL(Environment('//home//jack//ampl//'))

#EMPdf = pd.DataFrame.from_records(employees)
#print(EMPdf)

df = mkdat(employeeList, readShftTxt('//home//jack//Programs//AutoScheduling//shiftlist.txt'))
ampl.setData(df)

ampl.eval('model opt_algo.mod')

"""
def cleanName(name):
    idx = name.index('<')
    return(idx)


w2w= getW2W()
names = []

for idx in range(len(w2w)):
    if w2w[idx:idx+5]=='false':
        name= w2w[idx+14:idx+34]
        names.append(name[:cleanName(name)])

df= pd.DataFrame(names)

cnts = []
htmls = []
i = 1
for name_idx in range(len(names)):
    name= names[name_idx]
    idx1= w2w.find(name)+len(name)
    try:
        idx2= w2w[idx1:].find(names[name_idx+1])
        emp_html= w2w[idx1+35:idx1+idx2-125]
        cnt= emp_html.count('/td')
    except:
        idx2= len(w2w)
        emp_html= w2w[idx1+35:idx2-30]
        cnt= emp_html.count('/td')
    cnts.append(cnt)
    htmls.append(emp_html)

df['Counts'] = cnts
df['HTMLS'] = htmls

#bdd always 24 probably dark outline

def decodeHTML(html):
    print(html.count("bdd3"))
    hours = []
    for x in range(12):
        start= html.index('class="')
        end= html[start:].find('"')
        hours.append(html[start+7:end])
        for y in range(4):
            html= html[html.find('/td'):]

test = df.HTMLS[0]
print(test)
decodeHTML(test)
"""
