import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

provience = []
total = []
def get_message():
    df = pd.DataFrame(pd.read_excel('../../data/allPositionCount.xls'))
    for x in df['省份']:
        provience.append(x)
    for x in df['职位数']:
        total.append(int(x)/1718)

def draw():
    get_message()
    mpl.rcParams["font.sans-serif"]=["SimHei"]
    mpl.rcParams["axes.unicode_minus"]=False
    plt.pie(total,
            labels=provience,
            autopct="%3.1f%%",
            startangle=60
            )

    plt.title("不同省份职位数的比例")
    plt.show()

draw()
