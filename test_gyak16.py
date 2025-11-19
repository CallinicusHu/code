import gyak16


def test_steamdrift_irondale():
    assert (gyak16.map_distance("Steamdrift","Irondale") ==
            "from Steamdrift to Irondale the shortest distance is 2303 km")

def test_leverstorm_steamdrift():
    assert (gyak16.map_distance("Leverstorm","Steamdrift") ==
            "from Leverstorm to Steamdrift the shortest distance is 2885 km")

def test_irondale_steamdrift():
    assert (gyak16.map_distance("Irondale","Steamdrift") ==
            "from Irondale to Steamdrift the shortest distance is 2303 km")

def test_cogburg_gizbourne():
    assert (gyak16.map_distance("Cogburg","Gizbourne") ==
            "from Cogburg to Gizbourne the shortest distance is 1560 km")

def test_steamdrift_gizbourne():
    assert (gyak16.map_distance("Steamdrift","Gizbourne") ==
            "from Steamdrift to Gizbourne the shortest distance is 2829 km")
