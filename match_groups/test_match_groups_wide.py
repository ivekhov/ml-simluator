import match_groups_wide

data = [
    [
        [(5, 3, 4, 8), (1, 2), (7, 2)],
        [(1, 2, 7), (3, 4, 5, 8)]
    ],
    [
        [(1, 2), (2, 3), (3, 4)],
        [(1, 2, 3, 4)]
    ],
    [
        [(1, 2), (2, 3), (5, 3), (4, 6), (6, 7), (8, 9)],
        [(1, 2, 3, 5), (4, 6, 7), (8, 9)],
    ],
]


def test_basic() -> None:
    """."""
    assert match_groups_wide.extend_matches(data[0][0]) == data[0][-1]


def test_three_pairs() -> None:
    """."""
    assert match_groups_wide.extend_matches(data[1][0]) == data[1][-1]


def test_three_clusters() -> None:
    """."""
    assert match_groups_wide.extend_matches(data[2][0]) == data[2][-1]
