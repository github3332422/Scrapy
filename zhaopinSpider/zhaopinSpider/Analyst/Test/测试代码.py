prov = ['河南','河南','山西','北京']
city = ['郑州','信阳','大同','朝阳']

provice = dict(zip(prov,city))

# for pro,city in provice.items():
#     print(pro," ",city)
for pro,city in zip(prov,city):
    print(pro, " ", city)
