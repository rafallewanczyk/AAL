class HashTable:

    def __init__(self, size):
        self.K = size
        self.array = ["1"] * size
        self.reserved = 0

    def insert(self, value):
        index = self.getHashValue(value)
        #print(index)
        first_index = index

        i = 0
        while True:
            if self.array[int(index)] == "1" or self.array[int(index)] == "2" or self.array[
                int(index)] == value:
                self.array[int(index)] = value
                self.reserved += 1
                break

            else:
                i += 1
                index = index + 0.5 * i + 0.5 * i * i
                index %= self.K
                #print("nowy index wynosi : %d" % index)

            if index == first_index:
                print(f"nie mozna umiescic elementu {value} w tablicy")
                return

    def find(self, value):
        index = self.getHashValue(value)
        first_index = index

        i = 0
        while True:
            if self.array[int(index)] == value:
                return int(index)
            elif self.array[int(index)] == "1":
                return -1
            else:
                i += 1
                index = index + 0.5 * i + 0.5 * i * i
                index %= self.K
                if index == first_index:
                    return -1

    def delete(self, value):
        index = self.find(value)
        if index != -1:
            self.array[int(index)] = "2"
            self.reserved -= 1

    def getall(self):
        return self.array

    def getSize(self):
        return self.reserved

    def powerMod(self, a, n, mod):
        b = bin(n)[2:]
        m = len(b)
        r = 1
        x = a % mod

        for i in range(m - 1, -1, -1):
            if b[i] == '1':
                r = r * x % mod

            x **= 2
            x %= mod
        return r

    def getHashValue(self, text):
        array = [ord(ch) for ch in text[::-1]]
        # print(text)
        # print(text[::-1])
        # print(array)

        value = 0
        for i in range(0, len(array)):
            value += array[i] * self.powerMod(380, i, self.K)
            value %= self.K

        return value


