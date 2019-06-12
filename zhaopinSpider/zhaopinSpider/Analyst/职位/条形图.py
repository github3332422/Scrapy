import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

provience = []
total = []
def get_message():
    df = pd.DataFrame(pd.read_excel('../../data/allPositionCount.xls'))
    for x in df['省份']:
        provience.append(x)
    for x in df['职位数']:
        total.append(x)

def draw():
    get_message()
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    # tick_label: 刻度标签
    plt.barh(provience, total, hatch='/',alpha=0.8)
    # plt.xticks(provience,provience, rotation=60)
    plt.xlabel('职位数(个)')
    plt.ylabel('省份')
    plt.title("省份和职位数")
    plt.show()

def main():
    draw()

if __name__ == '__main__':
    main()
