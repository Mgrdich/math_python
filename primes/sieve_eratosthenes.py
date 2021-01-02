class SIEVE_ERATOSTHENES:
    range = 0
    primes_array = []  # True will be indexes that are prime
    __p = 2  # prime Index

    def __init__(self, number_range: int, split_print=None):
        self.primes_array = [True for i in range(number_range + 1)]
        self.range = number_range
        self.primes_array[0] = False  # 0 is not a prime
        self.primes_array[1] = False  # 1 is not a prime
        if split_print:
            self.print_stop = split_print  # todo check this

    def run(self):
        while self.__p * self.__p <= self.range:
            # if number index is not changed then it is prime
            if self.primes_array[self.__p]:

                # Update all the prime multiplies if 2 then 4 , 6, 8, ....
                for i in range(self.__p * 2, self.range + 1, self.__p):
                    self.primes_array[i] = False

            self.__p += 1

        # Print all prime numbers
        for p in range(self.range + 1):
            if self.primes_array[p]:
                print(p)


ob = SIEVE_ERATOSTHENES(100)
ob.run()
