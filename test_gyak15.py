import gyak15

def test_delivery_time_a():

    a = gyak15.delivery_timer("A")

    assert a == 5

def test_delivery_time_aa():

    aa = gyak15.delivery_timer("AA")

    assert aa == 13


def test_delivery_time_b():

    b = gyak15.delivery_timer("B")

    assert b == 5

def test_delivery_time_bb():

    bb = gyak15.delivery_timer("BB")

    assert bb == 5

def test_delivery_time_bbb():

    bbb = gyak15.delivery_timer("BBB")

    assert bbb == 15


def test_delivery_time_ab():

    ab = gyak15.delivery_timer("AB")

    assert ab == 5

def test_delivery_time_abb():

    abb = gyak15.delivery_timer("ABB")

    assert abb == 7

"""def test_delivery_time_rest():

    aababbab = gyak15.delivery_timer("AABABBAB")
    abbbabaaabbb = gyak15.delivery_timer("ABBBABAAABBB")"""