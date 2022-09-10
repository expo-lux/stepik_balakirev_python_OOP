class StringDigit(str):
    def __init__(self, string: str):
        if all(map(str.isdigit, string)):
            super().__init__()
        else:
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        x = super().__add__(other)
        return StringDigit(x)

    def __radd__(self, other):
        return StringDigit(other) + self


sd = StringDigit("123")
print(sd)  # 123
sd = sd + "456"  # StringDigit: 123456
sd = "789" + sd  # StringDigit: 789123456
sd = sd + "12f"  # ValueError
