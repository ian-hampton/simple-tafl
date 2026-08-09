from app.core import board

def resolve(start_id: str, dest_id: str) -> None:

    start_tile = board.get_tile_info(start_id)
    board.set_tile(dest_id, start_tile[1])
    board.set_tile(start_id, '-')

    # TODO - piece capture

    # TODO - update turn (and check for victory)

    return