from enum import Enum

class GameState(str, Enum):
    BLACK_TURN = "Black turn."
    WHITE_TURN = "White turn."
    BLACK_WIN = "Black player wins!" 
    WHITE_WIN = "White player wins!"

STATE = GameState.BLACK_TURN

def get_game_state() -> str:
    return STATE.value