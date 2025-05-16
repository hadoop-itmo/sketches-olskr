class BloomFilter:
    def __init__(self, n):
        self.n = n
        self.bit_array = 0
        self.bit_size = 0

    def put(self, s):
        # Генерируем хеш и устанавливаем соответствующий бит в 1
        hash_value = mmh3.hash(s) % self.n
        bit_value = 1 << hash_value

        if (self.bit_array & bit_value) == 0:
            self.bit_size += 1
        self.bit_array |= bit_value

    def get(self, s):
        # Проверяем, установлен ли соответствующий бит
        hash_value = mmh3.hash(s) % self.n
        return (self.bit_array & (1 << hash_value)) != 0

    def size(self):
        return self.bit_size