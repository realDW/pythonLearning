# 定义一个类


class Player:
    __doc__ = '玩家类'

    def __init__(self, name, hp, occu):
        self.__name = name  # __ 封装  private in java
        self.hp = hp
        self.occu = occu

    def print_role(self):
        print('role {name: %s, hp: %s, occu: %s}' % (self.__name, self.hp, self.occu))

    def update_name(self, name):
        self.__name = name


user1 = Player('dw', 999, 'warrior')
user2 = Player('cjx', 111, 'master')

# user1.__name = 'rs'

# user1.updateName('rs')

# user1.print_role()
# user2.print_role()


class Monster:
    __doc__ = '怪物类'

    def __init__(self, hp=100):
        self.hp = hp

    def move(self):
        print('怪物移动, 当前血量 %s' % self.hp)

    def who_am_i(self):
        print('这是一个怪物, 血量 %s' % self.hp)


monster = Monster()
monster.move()
monster.who_am_i()


class Animal(Monster):
    __doc__ = '小怪（继承自Monster）'

    def __init__(self, hp=50):
        super(Animal, self).__init__(50)

    def who_am_i(self):
        print('这是一个小怪')


animal = Animal()
animal.move()
animal.who_am_i()


class Boss(Monster):
    __doc__ = 'boss （继承自怪物类）'
    pass

