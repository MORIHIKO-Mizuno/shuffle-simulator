# リフルシャッフルする関数
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


# 元に戻すために必要なリフルシャッフルの回数を求める回数
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


# テスト用の例
if __name__ == "__main__":

    deck = []
    for s in ["♠️", "♥️", "♦️", "♣️"]:
        for i in range(1, 13+1):
            deck.append(s+str(i))
    card_count=len(deck)

    for i in range(return_to_original_count(card_count)):
        deck=riffle_shuffle(deck)
        print(deck)

