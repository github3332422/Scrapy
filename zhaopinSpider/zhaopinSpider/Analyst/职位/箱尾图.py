import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_message():
    df = pd.DataFrame(pd.read_excel('../../data/allPositionCount.xls'))
    total = []
    for x in df['职位数']:
        total.append(int(x))
    return total

def draw(total):
    mpl.rcParams["font.sans-serif"]=["FangSong"]
    #为了能够显示中文
    mpl.rcParams["axes.unicode_minus"]=False
    #为了能够合理地显示刻度标签是负数的情况
    plt.boxplot(total)
    plt.xlabel('随机数生成器')
    plt.ylabel('随机数值')
    plt.title('随机数生成器抗干扰能力的稳定性')
    plt.grid(axis='y', ls=':', lw=2, c='gray', alpha=0.6)
    plt.show()

def main():
    total = get_message()
    draw(total)

if __name__ == '__main__':
    main()
