import pandas as pd

df = pd.DataFrame(pd.read_excel('../../data/全国城市经纬度表.xls'))
prov = list(set([i for i in df['provience']]))
print(prov)
list = []
for pro in prov:
    li = []
    for provience,city in zip(df['provience'],df['city']):
        # print(prov.index(provience),prov[prov.index(provience)],city)
        if provience == pro:
            li.append(city)
    item = {
        'provience': pro,
        'city':li
    }
    list.append(item)
for lis in list:
    print(lis)