STARTING_BOARD = (
    "----BBB----"
    "----BBB----"
    "-----W-----"
    "-----W-----"
    "BB---W---BB"
    "BBWWWKWWWBB"
    "BB---W---BB"
    "-----W-----"
    "-----W-----"
    "----BBB----"
    "----BBB----"
)

BOARD_STATE = STARTING_BOARD

def get_board_state() -> str:
    return BOARD_STATE

def reset() -> None:
    global BOARD_STATE
    BOARD_STATE = STARTING_BOARD

def location_to_id(location: str) -> str:
    """
    Convert from coordinate pair (used by frontend) to numerical index (used by backend).

    Args:
        location (str): Coordinate pair.

    Returns:
        str: Numerical index (as a string!!).
    """
    col = ord(location[0]) - 97
    row = 11 - int(location[1:])
    return str((row * 11) + col)

def id_to_location(id: str) -> str:
    """
    Convert from numerical index to coordinate pair.

    Args:
        id (str): Numerical index.

    Returns:
        str: Coordinate pair.
    """
    id = int(id)
    col = id % 11
    row = id // 11
    col_letter = chr(ord('a') + col)
    return(f"{col_letter}{11 - row}")

def get_tile_info(id: str) -> list:
    id = int(id)
    if id not in range(0, 121):
        return ['N/A', 'N/A']
    return [f"{int(id)}", BOARD_STATE[id]]

def set_tile(id: str, state: str) -> None:
    global BOARD_STATE
    id = int(id)
    if id not in range(0, 121):
        return
    BOARD_STATE = BOARD_STATE[:id] + state + BOARD_STATE[id + 1:]    # now I remember why I don't use python strings for anything dynamic :(

def is_white(id: str) -> bool:
    tile = get_tile_info(id)
    if tile[1] in ['W', 'K']:
        return True
    return False

def is_black(id: str) -> bool:
    tile = get_tile_info(id)
    if tile[1] == 'B':
        return True
    return False

def is_hostile(id_1: str, id_2: str) -> bool:
    if id_1 == 'N/A' or id_2 == 'N/A':
        return False
    if is_white(id_1) and is_black(id_2):
        return True
    if is_black(id_1) and is_white(id_2):
        return True
    return False

def is_on_edge(id: str) -> bool:
    id = int(id)
    col = id % 11
    row = id // 11
    if col in [0, 10]:
        return True
    if row in [0, 10]:
        return True
    return False

def increment_up(id: str) -> list:
    id = int(id)
    col = id % 11
    row = id // 11
    return get_tile_info(str(id - 11)) if row != 0 else ['N/A', 'N/A']

def increment_down(id: str) -> list:
    id = int(id)
    col = id % 11
    row = id // 11
    return get_tile_info(str(id + 11)) if row != 10 else ['N/A', 'N/A']

def increment_left(id: str) -> list:
    id = int(id)
    col = id % 11
    row = id // 11
    return get_tile_info(str(id - 1)) if col != 0 else ['N/A', 'N/A']

def increment_right(id: str) -> list:
    id = int(id)
    col = id % 11
    row = id // 11
    return get_tile_info(str(id + 1)) if col != 10 else ['N/A', 'N/A']

def get_adjacent(id: str) -> list:
    """
    Gets information of all adjacent tiles given a location.

    For any tiles that do not exist, its list entry will be ['N/A', 'N/A'].
    This is an easy way for the other game code to know that we have reached the edge of the board.

    Args:
        id (str): _description_

    Returns:
        list: Will ALWAYS return a list of lists of length four.
    """
    data = [
        increment_up(id),
        increment_down(id),
        increment_left(id),
        increment_right(id)
    ]
    return data