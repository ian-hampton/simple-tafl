from app.core import board, move, state, validation

def get_game_state() -> dict:
    """
    Fetches all game state information.

    Returns:
        dict: JSON-ready dictionary containing board state and game turn.
    """
    data = {
        "board": board.get_board_state(),
        "turn": state.get_game_state()
    }
    return data

def get_legal_moves(location: str) -> dict:
    """
    Fetches all the legal moves for a piece at a specific location.

    Args:
        location (str): Coordinate pair.

    Returns:
        dict: JSON-ready dictionary containing list of legal destinations.
    """
    id = board.location_to_id(location)
    legal_moves = validation.get_legal_moves(id)

    legal_moves_final = []
    for id in legal_moves:
        legal_moves_final.append(board.id_to_location(id))

    data = {
        "moves": legal_moves_final
    }
    
    return data

def execute_move(start: str, dest: str) -> bool:
    """
    Attempts to move piece in start coordinate to destination coordinate.

    All moves that come in should have already been validated by a previous request.

    Just in case, we will verify by running the legal moves service again.

    Args:
        start (str): Coordinate pair.
        dest (str): Coordinate pair.

    Returns:
        bool: True if move successful, False otherwise.
    """
    start_id = board.location_to_id(start)
    dest_id = board.location_to_id(dest)

    # reject move if it is invalid - should not occur just in case
    legal_moves = validation.get_legal_moves(start_id)
    if dest_id not in legal_moves:
        return False

    # resolve move
    move.resolve(start_id, dest_id)

    return True

def reset() -> bool:
    """
    Resets a game back to the original state.

    Returns:
        bool: True if move successful, False otherwise.
    """
    board.reset()
    state.reset()
    return True