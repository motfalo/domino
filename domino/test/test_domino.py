from domino.domino import move

def test_move():
    straight = '||||||||'
    right = '/|||/|||'
    left = '|||\\|||\\'

    moves = 2
    assert move(straight, moves) == '||||||||'
    assert move(right, moves) == '///|///|'
    assert move(left, moves) == '|\\\\\\|\\\\\\'
