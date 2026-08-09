from app.core import board
from app.core import state

def capture(dest_tile: list, target_tile: list, dir: int) -> None:

    if not board.is_hostile(dest_tile[0], target_tile[0]):
        # No capture. Checked tile and adjacent tile not hostile.
        return

    flank_tile = board.get_adjacent(target_tile[0])[dir]
    if not board.is_hostile(target_tile[0], flank_tile[0]):
        # No capture. Adjacent tile and flank tile not hostile.
        return
    
    board.set_tile(target_tile[0], '-')

def check_captures(location_id: str):

    dest_tile = board.get_tile_info(location_id)

    adjacent = board.get_adjacent(location_id)
    up = adjacent[0]
    down = adjacent[1]
    left = adjacent[2]
    right = adjacent[3]

    capture(dest_tile, up, 0)
    capture(dest_tile, down, 1)
    capture(dest_tile, left, 2)
    capture(dest_tile, right, 3)

def resolve(start_id: str, dest_id: str) -> None:

    # execute move
    start_tile = board.get_tile_info(start_id)
    board.set_tile(dest_id, start_tile[1])
    board.set_tile(start_id, '-')

    # piece capture
    check_captures(dest_id)

    # update turn (and check for victory)
    state.set_game_state()