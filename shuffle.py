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
