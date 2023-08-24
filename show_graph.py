# どれほど混ざったかを確認する関数
# ケンドールの順位相関係数
import matplotlib.pyplot as plt
from scipy.stats import kendalltau


# ケンドールの順位相関係数を計算
def calculate_kendall_tau(deck_before, deck_after):
    correlation_coefficient, _ = kendalltau(deck_before, deck_after)
    return correlation_coefficient


# グラフを作成する関数
def make_graph(*args):
    x_data = range(len(args))
    y_data = args
    plt.plot(y_data, marker="o")
    plt.show()


# 受け取った数列群からケンドールの順位相関係数の水位のグラフを作成する関数
def show_graph(*args):
    result_list = []
    for i in range(len(args)):
        result_list.append(calculate_kendall_tau(args[0], args[i]))
    make_graph(*result_list)
    return result_list



if __name__ == "__main__":
    from shuffle import hindu_shuffle
    # テスト用のデッキ
    deck=[]
    for s in ["♠️", "♥️", "♦️", "♣️"]:
        for i in range(1, 13+1):
            deck.append(s+str(i))
    deck_dict={}
    deck_dict[0]=deck
    for i in range(1,10):
        deck_dict[i]=hindu_shuffle(deck_dict[i-1])
    show_graph(*[deck_dict[i] for i in range(len(deck_dict))])
    
        

