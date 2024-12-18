from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    """战斗者"""

    # slot 魔法限定绑定的base类成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        """
        攻击
        :param other: 被攻击的对象
        """
        pass


class Ultraman(Fighter):
    """奥特曼"""

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        """初始化方法

        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        """
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        # other 被攻击的对象
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        """究极必杀技(打掉对方至少50点或四分之三的血)

        :param other: 被攻击的对象

        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            # 魔法值不足, 普通攻击
            self.attack(other)
            return False

    def magic_attack(self, others):
        """魔法攻击, 范围攻击

        :param others: 被攻击的群体

        :return: 使用成功返回True否则返回False
        """
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            # 魔法值不足, 普通攻击
            return False

    def resume(self):
        """恢复魔法值"""
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return (f'~~~{self._name}奥特曼~~~'
                f'生命值:{self._hp}'
                f'魔法值:{self._mp}')


class Monster(Fighter):
    """小怪兽, 没有蓝"""

    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return (f'~~~{self._name}小怪兽~~~'
                f'生命值:{self._hp}')


def is_any_alive(monsters):
    """判断有没有小怪兽是活着的"""
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    """选择一个活着的小怪兽"""
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    """显示奥特曼和小怪兽的信息"""
    print(ultraman)
    for monsters in monsters:
        print(monsters, end='')
    print('\n')


def main():
    u = Ultraman('奥特曼', 1000, 120)
    m1 = Monster('小怪兽1', 250)
    m2 = Monster('小怪兽2', 300)
    m3 = Monster('小怪兽3', 350)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print(f'第{fight_round}回合开始')
        m = select_alive_one(ms) # 选中一只小怪兽
        skill = randint(1, 10)   # 通过随机数选择使用哪种技能
        if skill <= 6:  # 60%的概率使用普通攻击
            print(f'{u.name}使用普通攻击打了{m.name}')
            u.attack(m)
            # u.resume() 恢复mp的时候, 函数返回了恢复的值
            print(f'{u.name}的魔法值恢复了{u.resume()}点')
        elif skill <= 9:  # 30%的概率使用魔法攻击
            if u.magic_attack(ms):
                print(f'{u.name}使用了魔法攻击')
            else:
                print(f'{u.name}使用魔法失败')
                print(f'{u.name}使用普通攻击打了{m.name}')
                u.attack(m)
        else:  # 10%的概率使用究极必杀技
            if u.huge_attack(m):
                print(f'{u.name}使用究极必杀技虐了{m.name}')
            else:
                # mp不足, 返回False, 使用huge_attack中使用了普通攻击
                print(f'{u.name}使用普通攻击打了{m.name}')
                print(f'{u.name}的魔法值恢复了{u.resume()}点')

        # 如果选中的小怪兽没有在本回合被打死就回击奥特曼
        if m.alive:
            print(f'{m.name}回击了{u.name}')
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('战斗结束')
    if u.alive:
        print(f'{u.name}赢了')
    else:
        print(f'小怪兽赢了')


if __name__ == '__main__':
    main()



