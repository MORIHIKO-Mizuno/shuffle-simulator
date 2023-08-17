from scipy.stats import kendalltau
import random

# パーフェクトシャッフルする関数
def riffle_shuffle(deck):
    half_size = len(deck)//2
    first_half = deck[:half_size]
    second_half = deck[half_size:]
    shuffled_deck = []
    for i in range(half_size):
        shuffled_deck.append(first_half[i])
        shuffled_deck.append(second_half[i])
    # カードの枚数が奇数だった場合
    if len(first_half) > len(second_half):
        shuffled_deck.append(first_half[-1])
    return shuffled_deck


# ファローシャッフル(リフルシャッフル)する関数、パーフェクトではない
def faro_shuffle(deck):
    middle = len(deck) // 2
    first_half = deck[:middle]
    second_half = deck[middle:]
    
    shuffled_deck = []
    while True:
        try:
            if random.random()<0.5:
                shuffled_deck.append(first_half[0])
                first_half.pop(0)
            else:
                shuffled_deck.append(second_half[0])
                second_half.pop(0)
        except IndexError:
            shuffled_deck=shuffled_deck+first_half+second_half
            break

    
    return shuffled_deck


# ヒンドゥーシャッフルする関数
def hindu_shuffle(deck):

    # カットの位置を決める
    cut_positions = sorted([random.randint(1, len(deck) - 1)
                           for i in range(5)])
    # シャッフルの処理
    shuffled_deck = []
    start = 0
    for cut_position in cut_positions:
        end = cut_position
        shuffled_deck = deck[start:end]+shuffled_deck
        start = end
    else:
        shuffled_deck = deck[start:]+shuffled_deck
    return shuffled_deck


# ランダムシャッフルを行う関数(現実ではできない、順番を完全に混ぜる関数)
def random_shuffle(deck):
    random.shuffle(deck)
    return deck


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
