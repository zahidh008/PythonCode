import pandas as pd
import numpy as np

df = pd.read_excel (r'K:\Backup\Python_Code\pythonCode\Exel\test.xlsx')
df2 = pd.read_excel (r'K:\Backup\Python_Code\pythonCode\Exel\test2.xlsx')


# print (df)
# print(df[2:3]) 
# df.replace(a, 100, inplace=True)
# # edit cell based on 0 based index b1=1,0
# df.ix(1,0) = ""
# # write output
# df.to_csv(r'K:\Backup\Python_Code\pythonCode\Exel\test.csv', index=False)
# df[1][2]=1
# print (df)

ar = df.to_numpy()
ar2 = df2.to_numpy()

# print( (pd.Series(list(ar[:,0])).value_counts()) > 1)
for a in range(len(ar)):  
    if ar[a][1]in ar2:
        y,x = np.where(ar2 == ar[a][1]) 
        print(a)
        print(y)
# print(len(ar2))
