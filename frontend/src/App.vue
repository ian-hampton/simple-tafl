<script setup>
import { computed, onMounted, ref, reactive } from 'vue'
import * as api from './services/api'

const board = ref("");
const tileSize = 50
const select1 = ref("");
const select2 = ref("");
const selected = reactive(new Set())

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

const onTileClick = async (tile) => {
  console.log("User clicked on a tile. ID:", tile.id, "Location:", tile.location);
  
  // select start
  if (!select1.value) {
    if (tile.type !== '-') {
      // if piece present on tile save start location
      select1.value = tile.location;
      console.log("Saved", select1.value, "as select1.");
      // fetch all locations this piece could move to and highlight board
      const response = await api.getLegalMoves(tile.location);
      selected.clear()
      selected.add(tile.location)
      for (const location of response.moves) {
        selected.add(location)
      }
    }
    return;
  }

  // select end
  if (tile.location === select1.value) {
    // deselect if same piece selected twice
    select1.value = null;
    select2.value = null;
    selected.clear()
  } else if (!selected.has(tile.location)) {
    // deselect if not valid move
    select1.value = null;
    select2.value = null;
    selected.clear()
  } else {
    // otherwise save destination location
    select2.value = tile.location;
    console.log("Saved", select2.value, "as select2.");
  }

  // TODO: prompt user to confirm move
  // TODO: validate and execute move

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
  board.value = response.state;
})
</script>

<template>

  <body>

    <svg viewBox="0 0 552 552" width="750px" height="750px">

      <template v-for="tile in tiles" :key="tile.id">

        <g :transform="`translate(${tile.x}, ${tile.y})`" @click="onTileClick(tile)">

          <rect
            class="tile"
            :tile_id="tile.id"
            :tile_location="tile.location"
            :fill="selected.has(tile.location) ? '#555' : 'transparent'"
            :width="tileSize"
            :height="tileSize"
          />

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

          <circle
            v-if="tile.type === 'B'"
            fill="#000000"
            :cx="tileSize / 2"
            :cy="tileSize / 2"
            r="16"
          />

          <circle
            v-else-if="tile.type === 'W'"
            fill="#FFFFFF"
            :cx="tileSize / 2"
            :cy="tileSize / 2"
            r="16"
          />

          <circle
            v-else-if="tile.type === 'K'"
            fill="#FFFFFF"
            :cx="tileSize / 2"
            :cy="tileSize / 2"
            r="20"
          />

        </g>

      </template>

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

    <h2>Black turn.</h2>

  </body>

</template>