class Header:
    def __init__(self, key: str):
        self._key = key

    @property
    def key(self) -> str:
        return self._key

    def __repr__(self) -> str:
        return f"Header({self._key!r})"
