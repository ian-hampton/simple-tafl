from enum import Enum

from app.core import board

class GameState(str, Enum):
    BLACK_TURN = "Black turn."
    WHITE_TURN = "White turn."
    BLACK_WIN = "Black player wins!" 
    WHITE_WIN = "White player wins!"

STATE = GameState.BLACK_TURN

def get_game_state() -> str:
    return STATE.value

def white_victory() -> bool:
    king_index = board.get_board_state().find('K')
    return board.is_on_edge(str(king_index))

def black_victory_king() -> bool:
    return not 'K' in board.get_board_state()

def set_game_state() -> None:
    global STATE

    if black_victory_king():
        STATE = GameState.BLACK_WIN
        return

    if white_victory():
        STATE = GameState.WHITE_WIN
        return

    # TODO - check if Black has won via encirclement

    # otherwise, move to next turn
    if STATE == GameState.BLACK_TURN:
        STATE = GameState.WHITE_TURN
    else:
        STATE = GameState.BLACK_TURN