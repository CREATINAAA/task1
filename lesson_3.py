class Buffer:
    def __init__(self):
        self.memory = []
    def add(self, *a):
        # добавить следующую часть последовательности
        # if len(self.memory) <= 5:
        self.memory += a
        if len(self.memory) < 5:
            pass
        while len(self.memory) >= 5:
            summ = 0
            count = 0
            while count != 5:
                summ += self.memory.pop(0)
                count += 1
            print(summ)
    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        print(self.memory)

a = Buffer()

a.add(1,1,1,1,1, 1,1,1,1,1)
a.add(1,2,3)
a.add(4,5,6)
a.get_current_part()