class MoneyBox:
    def __init__(self, capacity):
         # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.our_capacity = 0

    def can_add(self, v):
        # True, если можно добавить v монет, False иначе
        if self.our_capacity + v <= self.capacity:
            return True
        else:
            return False
    def add(self, v):
        if self.can_add(v):
        # положить v монет в копилку
            self.our_capacity += v
            print(self.our_capacity)