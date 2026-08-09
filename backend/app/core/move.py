from app.core import board
from app.core import state

def resolve(start_id: str, dest_id: str) -> None:

    start_tile = board.get_tile_info(start_id)
    board.set_tile(dest_id, start_tile[1])
    board.set_tile(start_id, '-')

    # TODO - piece capture

    # update turn (and check for victory)
    state.set_game_state()

    return