import pandas as pd
wbbm = {"Student":["Ice Bear","Panda","Grizzly"], "Math":[80,95,79]}
math = pd.DataFrame(wbbm, columns=["Student","Math"])
wbbe = {"Student":["Ice Bear","Panda","Grizzly"], "Electronics":[85,81,83]}
electronics = pd.DataFrame(wbbe, columns=["Student","Electronics"])
wbbg = {"Student":["Ice Bear","Panda","Grizzly"], "GEAS":[90,79,93]}
geas = pd.DataFrame(wbbg, columns=["Student","GEAS"])
wbbe = {"Student":["Ice Bear","Panda","Grizzly"], "ESAT":[93,89,88]}
esat = pd.DataFrame(wbbe, columns=["Student","ESAT"])
merge= pd.merge(pd.merge(math,electronics, on ="Student"),pd.merge(geas, esat, on="Student"), on="Student")
melt= pd.melt(merge, id_vars=["Student"], var_name="Subject", value_name="Grades")
print(merge)
print(melt)