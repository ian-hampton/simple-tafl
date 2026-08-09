from enum import Enum

class GameState(str, Enum):
    BLACK_TURN = "Black turn."
    WHITE_TURN = "White turn."
    BLACK_WIN = "Black player wins!" 
    WHITE_WIN = "White player wins!"

STATE = GameState.BLACK_TURN

def get_game_state() -> str:
    return STATE.value

def set_game_state() -> None:
    global STATE

    # TODO - check if White has won the game

    # TODO - check if Black has won via king capture

    # TODO - check if Black has won via encirclement

    # otherwise, move to next turn
    if STATE == GameState.BLACK_TURN:
        STATE = GameState.WHITE_TURN
    else:
        STATE = GameState.BLACK_TURN