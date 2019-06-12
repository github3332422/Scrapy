import pandas as pd

df = pd.DataFrame(pd.read_excel('../../data/allPositionCount.xls'))

provience = []
total = []
for x in df['省份']:
    provience.append(x)

for x in df['职位数']:
    total.append(x)
print(provience)
print(total)