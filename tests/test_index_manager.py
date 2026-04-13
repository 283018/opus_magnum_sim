import pytest  # noqa: INP001

import opus_magnum_sym.elements.env.index_manager as im


@pytest.fixture(autouse=True)
def clean_state():
    im.reset()
    yield  # noqa: PT022


def test_init_state():
    assert im.active_count() == 0
    assert im.total_allocated() == 0


def test_sequential_alloc():
    assert im.allocate() == 0
    assert im.allocate() == 1
    assert im.allocate() == 2
    assert im.total_allocated() == 3
    assert im.active_count() == 3


def test_reuse_freed():
    idx0 = im.allocate()
    _idx1 = im.allocate()
    im.free(idx0)

    assert im.is_active(idx0) is False
    assert im.active_count() == 1

    reused = im.allocate()
    assert reused == idx0
    assert im.is_active(reused) is True
    assert im.active_count() == 2


def test_free():
    idx = im.allocate()
    im.free(idx)
    assert not im.is_active(idx)

    with pytest.raises(ValueError, match="not currently active"):
        im.free(idx)

    with pytest.raises(ValueError, match="not currently active"):
        im.free(999)


def test_is_valid():
    assert im.is_valid(-1) is False
    assert im.is_valid(0) is False

    im.allocate()
    assert im.is_valid(0) is True
    assert im.is_valid(1) is False


def test_get_all_active_copy():
    idx = im.allocate()
    snapshot = im.get_all_active()
    assert idx in snapshot

    snapshot.add(999)
    assert 999 not in im.get_all_active()


def test_reset():
    im.allocate()
    im.allocate()
    im.reset()

    assert im.total_allocated() == 0
    assert im.active_count() == 0
    assert im.allocate() == 0
