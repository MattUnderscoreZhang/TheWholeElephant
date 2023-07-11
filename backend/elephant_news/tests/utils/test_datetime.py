from elephant_news.utils.datetime import today


def test_today():
    val = today()
    assert len(val) == 10
    year = val[:4]
    month = val[5:7]
    day = val[8:]
    assert int(year) >= 2023
    assert int(month) >= 1
    assert int(month) <= 12
    assert int(day) >= 1
    assert int(day) <= 31
