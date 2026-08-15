<script setup>
import { computed, onMounted, ref, reactive } from 'vue'
import * as api from './services/api'

const board = ref("");
const turn = ref("");

const select1 = ref("");
const select2 = ref("");
const selected = reactive(new Set());

const tileSize = 50;

const playerPieces = {
  "Black turn.": ['B'],
  "White turn.": ['W', 'K']
};

function parseBoard(state) {
  const xInit = 1;
  const yInit = 1;
  const diff = tileSize;

  const objects = [];

  for (let count = 0; count < state.length; count++) {
    const char = state[count];

    const col = count % 11;
    const row = Math.floor(count / 11);
    const colLetter = String.fromCharCode(col + 97);

    objects.push({
      id: count,
      location: `${colLetter}${11 - row}`,
      type: char,
      x: xInit + col * diff,
      y: yInit + row * diff
    });
  }

  return objects;
}

const handleReset = async () => {
  await api.resetGame();
  const response = await api.getBoardState();
  board.value = response.board;
  turn.value = response.turn;
}

function clearSelection() {
  select1.value = null;
  select2.value = null;
  selected.clear();
}

const onTileClick = async (tile) => {
  console.log("User clicked on a tile. ID:", tile.id, "Location:", tile.location);

  // disable selection if game is over
  if (["Black player wins!", "White player wins!"].includes(turn.value)) return;
  
  // select start
  if (!select1.value) {
    
    // check that piece belongs to active player
    const validTypes = playerPieces[turn.value];
    if (!validTypes.includes(tile.type)) return;

    // save start location
    select1.value = tile.location;
    console.log("select1 =", select1.value);
    
    // fetch all locations this piece could move to and highlight board
    const response = await api.getLegalMoves(tile.location);
    selected.clear();
    selected.add(tile.location);
    for (const location of response.moves) {
      selected.add(location)
    }

    return;
  }

  // select destination
  if (tile.location === select1.value) {
    // deselect if same piece selected twice
    clearSelection();
    return;
  } else if (!selected.has(tile.location)) {
    // deselect if not valid move
    clearSelection();
    return;
  } else {
    // otherwise save destination location
    select2.value = tile.location;
    console.log("select2 =", select2.value);
  }

  // execute move
  const move = await api.resolveMove(select1.value, select2.value);
  if (!move) return;
  
  // update board after successful move
  const response = await api.getBoardState();
  board.value = response.board;
  turn.value = response.turn;
  clearSelection();

  return;
};

const tiles = computed(() => parseBoard(board.value));

const gridLines = computed(() => {
  const lines = [];
  const size = 11;
  const spacing = tileSize;

  // vertical lines
  for (let i = 0; i <= size; i++) {
    lines.push({
      x1: i * spacing + 1,
      y1: 1,
      x2: i * spacing + 1,
      y2: size * spacing + 1
    });
  }

  // horizontal lines
  for (let i = 0; i <= size; i++) {
    lines.push({
      x1: 1,
      y1: i * spacing + 1,
      x2: size * spacing + 1,
      y2: i * spacing + 1
    });
  }

  return lines;
});

onMounted(async () => {
  const response = await api.getBoardState();
  board.value = response.board;
  turn.value = response.turn;
})
</script>

<template>

  <body>

    <svg viewBox="0 0 552 552" width="750px" height="750px">

      <!-- template for board generation -->
      <template v-for="tile in tiles" :key="tile.id">

        <!-- 
        leveraging svg groups and translating it so that placement calculations are easier
        onTileClick() handles all board interaction
        -->
        <g :transform="`translate(${tile.x}, ${tile.y})`" @click="onTileClick(tile)">
          
          <!-- tile -->
          <rect
            class="tile"
            :tile_id="tile.id"
            :tile_location="tile.location"
            :fill="selected.has(tile.location) ? '#555' : 'transparent'"
            :width="tileSize"
            :height="tileSize"
          />

          <!-- selection highlight -->
          <rect
            v-if="selected.has(tile.location)"
            fill="none"
            stroke="white"
            stroke-width="2"
            :x="1"
            :y="1"
            :width="tileSize - 2"
            :height="tileSize - 2"
          />

          <!-- black piece -->
          <circle
            v-if="tile.type === 'B'"
            fill="#000000"
            :cx="tileSize / 2"
            :cy="tileSize / 2"
            r="16"
          />

          <!-- white piece -->
          <circle
            v-else-if="tile.type === 'W'"
            fill="#FFFFFF"
            :cx="tileSize / 2"
            :cy="tileSize / 2"
            r="16"
          />

          <!-- white king -->
          <g v-else-if="tile.type === 'K'">
            <circle
              fill="#FFFFFF"
              :cx="tileSize / 2"
              :cy="tileSize / 2"
              r="20"
            />
            <text
              :x="tileSize / 2"
              :y="tileSize / 2"
              text-anchor="middle"
              dominant-baseline="central"
              fill="#D6D6D6"
              font-family="Arial, sans-serif"
              font-weight="bold"
              font-size="24"
            >K</text>
          </g>

        </g>

      </template>

      <!-- draw grid lines -->
      <g stroke="#332419" stroke-width="2">
        <line
          v-for="(line, index) in gridLines"
          :key="index"
          :x1="line.x1"
          :y1="line.y1"
          :x2="line.x2"
          :y2="line.y2"
        />
      </g>

    </svg>

    <h2>{{ turn }}</h2>

    <button v-if="turn.includes('win')" @click="handleReset()">
      Reset
    </button>

  </body>

</template>