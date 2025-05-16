import mmh3


class BloomFilter_k:
    def __init__(self, k, n):
        self.k = k  # Количество хеш-функций
        self.n = n
        self.bit_array = 0
        self.bit_size = 0

    def put(self, s):
        for i in range(self.k):
            hash_value = mmh3.hash(s, i) % self.n
            bit_value = 1 << hash_value

            if (self.bit_array & bit_value) == 0:
                self.bit_size += 1
            self.bit_array |= bit_value

    def get(self, s):
        for i in range(self.k):
            hash_value = mmh3.hash(s, i) % self.n
            if (self.bit_array & (1 << hash_value)) == 0:
                return False  # Если хотя бы один бит не установлен, возвращаем False
        return True

    def size(self):
        return self.bit_size / self.k