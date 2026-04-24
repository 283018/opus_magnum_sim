# TODO: simple version for now, up to re-write if multithreading if needed

_next_id: int = 0
_active: set[int] = set()
_free: set[int] = set()


def allocate() -> int:
    global _next_id  # noqa: PLW0603
    idx = _free.pop() if _free else _next_id
    if idx == _next_id:
        _next_id += 1
    _active.add(idx)
    return idx


def free(idx: int) -> None:
    if idx not in _active:
        msg = f"Index {idx} is not currently active."
        raise ValueError(msg)
    _active.remove(idx)
    _free.add(idx)


def is_active(idx: int) -> bool:
    return idx in _active


def is_valid(idx: int) -> bool:
    return idx >= 0 and idx < _next_id


def active_count() -> int:
    return len(_active)


def total_allocated() -> int:
    return _next_id


def get_all_active() -> set[int]:
    return _active.copy()


def reset() -> None:
    global _next_id, _active, _free  # noqa: PLW0602, PLW0603
    _next_id = 0
    _active.clear()
    _free.clear()
