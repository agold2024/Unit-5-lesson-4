import pandas as pd
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/Minnesota"
dfs= pd.read_html(
    #df stands for data frame
    url, 
    match= "Historical population"
    )
df = dfs[0]
df = df.iloc[0:-2]
df=df[["Census", "Pop."]].astype("int")
print(df.info())
df.plot(x= "Census", y= "Pop.")
plt.show()
#plt.show lets use see the output
