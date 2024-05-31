from gyak12 import Junior, Senior, Boss

def test_daddy():
    #arrange
    aba = Junior("aba", None)
    bob = Senior("bob", None, aba)
    cad = Senior("cad", None, bob)
    dud = Boss("dud", cad)

    aba.set_daddy(bob)
    bob.set_daddy(cad)
    cad.set_daddy(dud)

    expected = aba # "aba"

    #act
    result = dud.who_is_your_serf().who_is_your_serf().who_is_your_serf()

    #assert
    assert result ==  expected
