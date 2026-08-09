from app.core import board

def get_legal_moves(id: str) -> list:
    """
    Fetches all legal destinations for a piece at a specific location.

    In Simple Tafl, all pieces move like a rook in chess, but can only move into empty spaces.

    Args:
        id (str): Numerical index.

    Returns:
        list: List of all legal destinations.
    """
    adjacent = board.get_adjacent(id)
    up = adjacent[0]
    down = adjacent[1]
    left = adjacent[2]
    right = adjacent[3]

    result = []

    while up[1] == '-':
        result.append(up[0])
        up = board.increment_up(up[0])

    while down[1] == '-':
        result.append(down[0])
        down = board.increment_down(down[0])

    while left[1] == '-':
        result.append(left[0])
        left = board.increment_left(left[0])

    while right[1] == '-':
        result.append(right[0])
        right = board.increment_right(right[0])

    return result