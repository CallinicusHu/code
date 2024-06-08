import parser


def test_parse_verb():
    # ('verb', 'go')
    word_list = [('verb', 'go')]
    result = parser.parse_verb(word_list)
    assert (result == ('verb', 'go'))


def test_parse_verb_exception():
    # ('verb', 'go')
    word_list = [('noun', 'bear')]
    try:
        parser.parse_verb(word_list)
        assert False
    except parser.ParserError:
        assert True

def test_parse_verb_typerror():
    # ('verb', 'go')
    word_list = 46546
    try:
        parser.parse_verb(word_list)
        assert False
    except parser.ParserError:
        assert False
    except TypeError:
        assert True

def test_peek():
    word_list = (("corgi", "panda"), ("mókus", "capibara"))
    result = parser.peek(word_list)
    assert (result == "corgi")

def test_parse_sentence():
    #[('verb', 'Kill'), ('stop', 'the'), ('noun', 'bear')]

    word_list = [('verb', 'kill'), ('stop', 'the'), ('noun', 'bear')]

    result = parser.parse_sentence(word_list)

    assert (result == parser.Sentence(('noun', 'player'), ('verb', 'kill'), ('noun', 'bear')))


def test_parse_sentence_fail():
    #[('verb', 'Kill'), ('stop', 'the'), ('noun', 'bear')]

    word_list = [('verb', 'go'), ('verb', 'go'), ('verb', 'go')]

    try:
        result = parser.parse_sentence(word_list)
        assert False

    except parser.ParserError:
        assert True

