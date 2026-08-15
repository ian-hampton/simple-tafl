import heapq
from enum import Enum
from typing import List, Tuple

from app.core import board

class GameState(str, Enum):
    BLACK_TURN = "Black turn."
    WHITE_TURN = "White turn."
    BLACK_WIN = "Black player wins!" 
    WHITE_WIN = "White player wins!"

STATE = GameState.BLACK_TURN

def get_game_state() -> str:
    return STATE.value

def reset() -> None:
    global STATE
    STATE = GameState.BLACK_TURN

def white_victory() -> bool:
    king_index = board.get_board_state().find('K')
    return board.is_on_edge(str(king_index))

def black_victory_king() -> bool:
    return not 'K' in board.get_board_state()

def black_victory_encirclement() -> bool:
    """
    Using flood fill algorithm to test for encirclement.

    Returns:
        bool: True if white pieces are all encircled, false otherwise.
    """
    heap: List[Tuple[int, str]] = []
    visited = set()
    floodfill = ['0'] * 121

    # flood fill from all white pieces
    for index, char in enumerate(board.get_board_state()):
        tile_id = str(index)
        if not board.is_white(tile_id):
            continue
        heapq.heappush(heap, (0, tile_id))

    # dfs
    while heap:
        priority, tile_id = heapq.heappop(heap)

        visited.add(tile_id)
        floodfill[int(tile_id)] = '1'

        adjacent = board.get_adjacent(tile_id)
        up = adjacent[0]
        down = adjacent[1]
        left = adjacent[2]
        right = adjacent[3]

        if up[0] != 'N/A' and up[0] not in visited and not board.is_black(up[0]):
            heapq.heappush(heap, (priority + 1, up[0]))

        if down[0] != 'N/A' and down[0] not in visited and not board.is_black(down[0]):
            heapq.heappush(heap, (priority + 1, down[0]))

        if left[0] != 'N/A' and left[0] not in visited and not board.is_black(left[0]):
            heapq.heappush(heap, (priority + 1, left[0]))

        if right[0] != 'N/A' and right[0] not in visited and not board.is_black(right[0]):
            heapq.heappush(heap, (priority + 1, right[0]))

    # check edges for fill
    for index, char in enumerate(floodfill):
        if char != '1':
            continue
        if board.is_on_edge(index):
            return False

    return True

def set_game_state() -> None:
    global STATE

    if black_victory_king():
        STATE = GameState.BLACK_WIN
        return

    if white_victory():
        STATE = GameState.WHITE_WIN
        return

    if black_victory_encirclement():
        STATE = GameState.BLACK_WIN
        return

    # otherwise, move to next turn
    if STATE == GameState.BLACK_TURN:
        STATE = GameState.WHITE_TURN
    else:
        STATE = GameState.BLACK_TURN