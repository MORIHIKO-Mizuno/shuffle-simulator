from  shuffle import *
from scipy.stats import kendalltau


# 元に戻すために必要なパーフェクトシャッフルの回数を求める回数
def return_to_original_count(card_count):
    if card_count <= 0:
        raise ValueError("CardCount must be a positive integer.")
    if card_count == 1:
        return 0
    # 枚数が偶数
    if card_count % 2 == 0:
        exp = 2
        count = 1
        while (exp - 1) % (card_count - 1) != 0:
            exp *= 2
            count += 1
        return count
    # 枚数が奇数
    else:
        card_count += 1
        return return_to_original_count(card_count)

# どれほど混ざったかを確認する関数
# ケンドールの順位相関係数 
def calculate_kendall_tau(deck_before, deck_after):
    correlation_coefficient, _ = kendalltau(deck_before, deck_after)
    return correlation_coefficient


# テスト用の例
if __name__ == "__main__":
    deck = []
    for s in ["♠️", "♥️", "♦️", "♣️"]:
        for i in range(1, 13+1):
            deck.append(s+str(i))
    card_count = len(deck)

    for i in range(return_to_original_count(card_count)):
        deck = riffle_shuffle(deck)
        print(deck)
    print(hindu_shuffle(deck))