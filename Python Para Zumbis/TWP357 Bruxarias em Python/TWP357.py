class int42(int):
    def __init__(self, n):
        int.__init__(n)

    def __add__(a, b):
        return 42

    def __str__(n):
        return '42'


# X
a = int42(7)

b = int42(13)

print a + b
