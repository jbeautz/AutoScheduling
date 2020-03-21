import pandas as pd
import numpy as np

def mkdat(emps, shfts):
    df = pd.DataFrame(('EMP', 'SHIFT'), ('yes','no'))

    yes = np.zeros((len(emps), len(shfts)))
    no = yes

    print(emps[0].getPrefer())

    for i in range(len(emps)):
        for j in range(len(shfts)):
            if shfts[j] in emps[i].getPrefer():
                yes[i][j] = 1
            if shfts[j] in emps[i].getNoWay():
                no[i][j] = 1

    df.set_value({
        (emps, shfts): (yes[i][j], no[i][j])
        for i, emp in enumerate(emps)
        for j, shft in enumerate(shfts)
    })

    return df
