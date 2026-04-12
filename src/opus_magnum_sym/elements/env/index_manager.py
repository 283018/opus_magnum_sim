from typing import Self


class IndexManager:
    _instance: Self

    def __init__(self) -> None:
        self._next_id: int = 0
        self._active: set[int] = set()
        self._free_list: set[int] = set()
        self._max_id: int = 0

    @classmethod
    def get(cls) -> Self:
        if cls._instnace is None:
            cls._instnace = cls()
        return cls._instance

    @classmethod
    def reset(cls) -> None:
        cls._instance = cls()  # ty:ignore[invalid-assignment]

    def allocate(self) -> int:
        if self._free_list:
            idx = self._free_list.pop()
        else:
            idx = self._next_id
            self._next_id += 1
            self._max_id = max(self._max_id, idx)

        self._active.add(idx)
        return idx

    def free(self, idx: int) -> bool:
        if idx in self._active:
            self._active.remove(idx)
            self._free_list.add(idx)
            return True
        return False

    def is_active(self, idx: int) -> bool:
        return idx in self._active

    def is_valid(self, idx: int) -> bool:
        return idx >= 0 and idx < self._next_id

    @property
    def active_count(self) -> int:
        return len(self._active)

    @property
    def total_allocated(self) -> int:
        return self._next_id

    def get_all_active(self) -> set[int]:
        return self._active.copy()
