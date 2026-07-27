BOARD_STATE = (
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

def get_board_state() -> str:
    return BOARD_STATE

def location_to_id(location: str) -> str:
    col = ord(location[0]) - 97
    row = 11 - int(location[1:])
    return str((row * 11) + col)

def id_to_location(id: str) -> str:
    id = int(id)
    col = id % 11
    row = id // 11
    col_letter = chr(ord('a') + col)
    return(f"{col_letter}{11 - row}")

def get_tile_info(id: str) -> list:
    id = int(id)
    if id not in range(0, 121):
        return ["N/A", "N/A"]
    return [f"{id}", BOARD_STATE[id]]

def increment_up(id: str) -> list:
    id = int(id)
    col = id % 11
    row = id // 11
    return get_tile_info(str(id - 11)) if row != 0 else ["N/A", "N/A"]

def increment_down(id: str) -> list:
    id = int(id)
    col = id % 11
    row = id // 11
    return get_tile_info(str(id + 11)) if row != 10 else ["N/A", "N/A"]

def increment_left(id: str) -> list:
    id = int(id)
    col = id % 11
    row = id // 11
    return get_tile_info(str(id - 1)) if col != 0 else ["N/A", "N/A"]

def increment_right(id: str) -> list:
    id = int(id)
    col = id % 11
    row = id // 11
    return get_tile_info(str(id + 1)) if col != 10 else ["N/A", "N/A"]

def get_adjacent(id: str) -> list:
    data = [
        increment_up(id),
        increment_down(id),
        increment_left(id),
        increment_right(id)
    ]
    return data