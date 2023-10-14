class NBT:
    def __init__(self, value, string_format: str):
        self.value = value
        self.string_format = string_format

    def __str__(self):
        return self.string_format.format(self.value)

    @classmethod
    def byte(cls, value: int) -> "NBT":
        return NBT(value, "{}b")

    @classmethod
    def short(cls, value: int) -> "NBT":
        return NBT(value, "{}s")

    @classmethod
    def long(cls, value: int) -> "NBT":
        return NBT(value, "{}L")

    @classmethod
    def double(cls, value: int) -> "NBT":
        return NBT(value, "{}d")

    @classmethod
    def string(cls, value: str) -> "NBT":
        return NBT(value, '"{}"')
