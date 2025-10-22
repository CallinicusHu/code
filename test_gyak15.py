import gyak15


def test_delivery_time_a():
    a = gyak15.delivery_timer("A")

    assert a == 5


def test_delivery_time_aa():
    aa = gyak15.delivery_timer("AA")

    assert aa == 13


def test_delivery_time_aaa():
    aaa = gyak15.delivery_timer("AAA")

    assert aaa == 21


def test_delivery_time_aaaa():
    aaaa = gyak15.delivery_timer("AAAA")

    assert aaaa == 29


def test_delivery_time_b():
    b = gyak15.delivery_timer("B")

    assert b == 5


def test_delivery_time_bb():
    bb = gyak15.delivery_timer("BB")

    assert bb == 5


def test_delivery_time_bbb():
    bbb = gyak15.delivery_timer("BBB")

    assert bbb == 15


def test_delivery_time_bbbbbbb():  # 7b

    bbbbbbb = gyak15.delivery_timer("BBBBBBB")

    assert bbbbbbb == 35


def test_wrongpack():
    wrong = gyak15.delivery_timer("BBBMBB5")

    assert wrong == "error at worktime 11 invalid package in MBB5"


def test_delivery_time_ab():
    ab = gyak15.delivery_timer("AB")

    assert ab == 5


def test_delivery_time_abb():
    abb = gyak15.delivery_timer("ABB")

    assert abb == 7


def test_delivery_time_aab():
    aab = gyak15.delivery_timer("AAB")

    assert aab == 13


def test_delivery_time_aba():
    aba = gyak15.delivery_timer("ABA")

    assert aba == 13


def test_delivery_time_bab():
    bab = gyak15.delivery_timer("BAB")

    assert bab == 7


def test_delivery_time_aababbab():
    aababbab = gyak15.delivery_timer("AABABBAB")

    assert aababbab != "faszsetudja"


def test_delivery_time_abbbabaaabbb():
    abbbabaaabbb = gyak15.delivery_timer("ABBBABAAABBB")

    assert abbbabaaabbb != "faszsetudja"


def test_a_log():
    gyak15.delivery_timer("A")
    good = open("deliver_a_good.txt").readlines()
    print(good)
    maybe = open("truck_log").readlines()
    print(maybe)
    assert good == maybe


def test_a_log():
    gyak15.delivery_timer("A")
    good = open("deliver_a_good.txt").readlines()
    maybe = open("truck_log").readlines()
    assert good == maybe


def test_to_fail_log():
    gyak15.delivery_timer("AB")
    good = open("deliver_a_good.txt").readlines()
    maybe = open("truck_log").readlines()
    assert good != maybe


def test_b_log():
    gyak15.delivery_timer("B")
    good = open("deliver_b_good.txt").readlines()
    maybe = open("truck_log").readlines()
    assert good == maybe

def test_ab_log():
    gyak15.delivery_timer("AB")
    good = open("deliver_ab_good.txt").readlines()
    maybe = open("truck_log").readlines()
    assert good == maybe


def test_baba_log():
    gyak15.delivery_timer("BABA")
    good = open("deliver_baba_good.txt").readlines()
    maybe = open("truck_log").readlines()
    assert good == maybe

def test_long_log():
    gyak15.delivery_timer("BABAABBBAAAAAAAA")
    good = open("deliver_long_good.txt").readlines()
    maybe = open("truck_log").readlines()
    assert good == maybe