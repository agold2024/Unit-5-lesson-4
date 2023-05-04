import pandas as pd
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/Minnesota"
dfs= pd.read_html(
    #df stands for data frame
    url, 
    match= "Religious affiliation in Minnesota by movement"
    )
df = dfs[0]
print(df.info())
# df = df.iloc[0:-1]
# df=df[["Affiliation", "% of population"]].astype("int")
# print(df.info())
df.plot(x= "Affiliation", y= "% of population")
plt.show()
# #plt.show lets use see the output

#a float is a decimal
