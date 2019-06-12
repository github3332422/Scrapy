import matplotlib as mpl
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8]
y = [3,1,4,5,6,9,7,2]
# plt.bar(x,y)
# plt.show()
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus']=False
plt.bar(x,y,align='center',tick_label=['q','a','c','e','r','j','b','p'], hatch='/')
#plt.bar:柱状图
#align:对齐方式  align : {'center', 'edge'}
#tick_label: 刻度标签
#hatch:填充
plt.xlabel('箱子编号')
plt.ylabel('箱子重量(kg)')
plt.show()
