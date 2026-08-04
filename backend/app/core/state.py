from enum import Enum

class GameState(str, Enum):
    BLACK_TURN = "Black"
    WHITE_TURN = "White"
    BLACK_WIN = "Black Win"
    WHITE_WIN = "White Win"

STATE = GameState.BLACK_TURN

def get_game_state() -> str:
    return STATE.value