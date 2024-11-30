import random


class Card(object):
    """一张牌"""

    def __init__(self, suite, face):
        self._suite = suite
        self._face = face

    @property
    def face(self):
        return self._face

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = "A"
        elif self._face == 11:
            face_str = "J"
        elif self._face == 12:
            face_str = "Q"
        elif self._face == 13:
            face_str = "K"
        else:
            face_str = str(self._face)
        return (self._suite + face_str)

    # 返回用于调试, 日志记录的字符串, 更准确表示对象状态
    def __repr__(self):
        return self.__str__()


class Poker(object):
    """一副牌"""

    def __init__(self):
        """
        :param cards: 一整副牌的列表
        :param current: 乱序的牌中, 牌组的index
        """
        self._cards = [Card(suite, face)
                       for suite in "♠♥♣♦"
                       for face in range(1, 14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        """洗牌(随机乱序), random 库的 shuffle 方法"""
        self._current = 0
        random.shuffle(self._cards)

    def next(self):
        """发牌"""
        card = self._cards[self._current]
        self._current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self._current < len(self._cards)


class Player(object):
    """玩家"""

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_on_hand(self):
        return self._cards_on_hand

    def get(self, card):
        """摸牌"""
        self._cards_on_hand.append(card)

    def arrange(self, card_key):
        """整理手上的牌"""
        self._cards_on_hand.sort(key=card_key)


def get_key(card):
    # 获得每张牌(对象)的花色和数字
    return (card.suite, card.face)


def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝')]
    # 抓牌
    # for _ in range(13):
    #     for player in players:
    #         player.get(p.next)

    # 抓牌直到抓完牌
    while p.has_next:
        for player in players:
            if p.has_next:
                player.get(p.next())
            else:
                break
    for player in players:
        print(player.name + ':', end=' ')
        # get_key 得到 card
        player.arrange(get_key)
        print(player.cards_on_hand)


if __name__ == '__main__':
    main()
















