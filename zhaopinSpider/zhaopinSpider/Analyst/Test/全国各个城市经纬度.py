import pandas as pd

df = pd.DataFrame(pd.read_excel('../../data/全国城市经纬度表.xls'))
for x in zip(df['city'],df['thr'],df['dim']):
    city,thr,dim = x
    print(city,':','[',thr,',',dim,']')