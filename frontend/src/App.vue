<script setup>
import { computed, onMounted, ref } from 'vue'
import * as api from './services/api'

const board = ref("");
const tileSize = 25

function parseBoard(state) {
  const xInit = 1;
  const yInit = 1;
  const diff = 25;

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

const onTileClick = (tile) => {
  console.log("User clicked on a tile. ID:", tile.id, "Location:", tile.location);
};

const tiles = computed(() => parseBoard(board.value));

onMounted(async () => {
  const data = await api.getBoardState();
  board.value = data.state;
})
</script>

<template>

  <svg height="1000px" viewBox="0 0 277 277">

    <template v-for="tile in tiles" :key="tile.id">

      <g :transform="`translate(${tile.x}, ${tile.y})`" @click="onTileClick(tile)">
    
        <rect
          class="tile"
          :tile_id="tile.id"
          :tile_location="tile.location"
          :width="tileSize" 
          :height="tileSize"
        />

        <circle
          v-if="tile.type === 'B'"
          fill="#000000"
          :cx="tileSize / 2"
          :cy="tileSize / 2"
          r="10"
        />

        <circle
          v-else-if="tile.type === 'W'"
          fill="#FFFFFF"
          :cx="tileSize / 2"
          :cy="tileSize / 2"
          r="10"
        />

        <rect
          v-else-if="tile.type === 'K'"
          class="king"
          x="2"
          y="2"
          :width="tileSize - 4"
          :height="tileSize - 4"
        />

      </g>

    </template>

  </svg>

</template>