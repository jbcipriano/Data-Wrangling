import pandas as pd
data = {"Box":["Box1","Box1","Box1","Box2","Box2","Box2"],"Dimension":["Length","Width","Height","Length","Width","Height"],'Value': [6,4,2,5,3,4]}
messy = pd.DataFrame(data,columns=["Box","Dimension","Value"])
tidy = messy.pivot(index ="Box",columns="Dimension",values="Value").reset_index()
Volume = tidy["Length"]*tidy["Width"]*tidy["Height"]
tidy["Volume"]=Volume
switch= list(tidy)
switch[1],switch[2]=switch[2],switch[1]
switch[2],switch[3]=switch[3],switch[2]
tidy = tidy.reindex(columns=switch)
print(tidy)