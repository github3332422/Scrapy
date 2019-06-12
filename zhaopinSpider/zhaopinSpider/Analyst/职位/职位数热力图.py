import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.colors import rgb2hex
import numpy as np
import pandas as pd

'''
生成国内省界图片
'''
plt.figure(figsize=(16, 8))
m = Basemap(
    llcrnrlon=77,
    llcrnrlat=14,
    urcrnrlon=140,
    urcrnrlat=51,
    projection='lcc',
    lat_1=33,
    lat_2=45,
    lon_0=100
)
m.drawcountries(linewidth=1.5)
m.drawcoastlines()
m.readshapefile('../Test/gadm36_CHN_shp/gadm36_CHN_1', 'states', drawbounds=True)

'''
读取数据，储存为dataframe格式，删去地名之中的空格，并设置地名为dataframe的index。
'''
df = pd.read_excel('../../data/allPositionCount.xls',encoding='UTF-8')
new_index_list = []
for i in df["省份"]:
    i = i.replace(" ", "")
    new_index_list.append(i)
new_index = {"region": new_index_list}
new_index = pd.DataFrame(new_index)
df = pd.concat([df, new_index], axis=1)
df = df.drop(["省份"], axis=1)
df.set_index("region", inplace=True)


'''

'''
provinces = m.states_info
statenames = []
colors = {}
cmap = plt.cm.YlOrRd
vmax = 200
vmin = 2

for each_province in provinces:
    print(each_province,end=' ')
    province_name = each_province['NL_NAME_1']
    p = province_name.split('|')
    print(province_name)
    print("*"*50)
    if len(p) > 1:
        s = p[1]
    else:
        s = p[0]
    s = s[:2]
    if s == '黑龍':
        s = '黑龙江'
    if s == '内蒙':
        s = '内蒙古'
    statenames.append(s)
    pop = df['职位数'][s]
    colors[s] = cmap(np.sqrt((pop - vmin) / (vmax - vmin)))[:3]

# print(new_index_list,'\n',colors)

'''
画图
'''
ax = plt.gca()
for nshape, seg in enumerate(m.states):
    color = rgb2hex(colors[statenames[nshape]])
    poly = Polygon(seg, facecolor=color, edgecolor=color)
    ax.add_patch(poly)

plt.show()