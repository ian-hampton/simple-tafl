<script setup>
import { computed, onMounted, ref } from 'vue'
import * as api from './services/api'

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

    objects.push({
      id: count,
      type: char,
      x: xInit + col * diff,
      y: yInit + row * diff
    });
  }

  return objects;
}

const board = ref("");

const tiles = computed(() => parseBoard(board.value));

onMounted(async () => {
  const data = await api.getBoardState();
  board.value = data.state;
})
</script>

<template>

  <svg height="1000px" viewBox="0 0 277 277">

    <template v-for="tile in tiles" :key="tile.id">

      <rect
        class="tile"
        :x="tile.x"
        :y="tile.y"
      />

      <circle
        v-if="tile.type === 'B'"
        fill="#000000"
        :cx="tile.x + tileSize / 2"
        :cy="tile.y + tileSize / 2"
        r="10"
      />

      <circle
        v-else-if="tile.type === 'W'"
        fill="#FFFFFF"
        :cx="tile.x + tileSize / 2"
        :cy="tile.y + tileSize / 2"
        r="10"
      />

      <rect
        v-else-if="tile.type === 'K'"
        class="king"
        :x="tile.x + 2"
        :y="tile.y + 2"
      />

    </template>

  </svg>

</template>