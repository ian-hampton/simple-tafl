<script setup>
import { ref, onMounted } from 'vue'
import * as api from './services/api'

const board = ref("")

onMounted(async () => {
  try {
    const data = await api.getBoardState()
    board.value = data.state
  } catch (err) {
    console.log("Failed to get board state.")
  }
})
</script>

<template>

  <div>

  <svg height="1000px" viewBox="0 0 277 277">
    <rect class="tile" x="1" y="1"/>
    <rect class="tile" x="26" y="1"/>
    <rect class="tile" x="51" y="1"/>
    <rect class="tile" x="76" y="1"/>
    <rect class="tile" x="101" y="1"/>
    <rect class="tile" x="126" y="1"/>
    <rect class="tile" x="151" y="1"/>
    <rect class="tile" x="176" y="1"/>
    <rect class="tile" x="201" y="1"/>
    <rect class="tile" x="226" y="1"/>
    <rect class="tile" x="251" y="1"/>
    
    <rect class="tile" x="1" y="26"/>
    <rect class="tile" x="26" y="26"/>
    <rect class="tile" x="51" y="26"/>
    <rect class="tile" x="76" y="26"/>
    <rect class="tile" x="101" y="26"/>
    <rect class="tile" x="126" y="26"/>
    <rect class="tile" x="151" y="26"/>
    <rect class="tile" x="176" y="26"/>
    <rect class="tile" x="201" y="26"/>
    <rect class="tile" x="226" y="26"/>
    <rect class="tile" x="251" y="26"/>

    <rect class="tile" x="1" y="51"/>
    <rect class="tile" x="26" y="51"/>
    <rect class="tile" x="51" y="51"/>
    <rect class="tile" x="76" y="51"/>
    <rect class="tile" x="101" y="51"/>
    <rect class="tile" x="126" y="51"/>
    <rect class="tile" x="151" y="51"/>
    <rect class="tile" x="176" y="51"/>
    <rect class="tile" x="201" y="51"/>
    <rect class="tile" x="226" y="51"/>
    <rect class="tile" x="251" y="51"/>

    <rect class="tile" x="1" y="76"/>
    <rect class="tile" x="26" y="76"/>
    <rect class="tile" x="51" y="76"/>
    <rect class="tile" x="76" y="76"/>
    <rect class="tile" x="101" y="76"/>
    <rect class="tile" x="126" y="76"/>
    <rect class="tile" x="151" y="76"/>
    <rect class="tile" x="176" y="76"/>
    <rect class="tile" x="201" y="76"/>
    <rect class="tile" x="226" y="76"/>
    <rect class="tile" x="251" y="76"/>

    <rect class="tile" x="1" y="101"/>
    <rect class="tile" x="26" y="101"/>
    <rect class="tile" x="51" y="101"/>
    <rect class="tile" x="76" y="101"/>
    <rect class="tile" x="101" y="101"/>
    <rect class="tile" x="126" y="101"/>
    <rect class="tile" x="151" y="101"/>
    <rect class="tile" x="176" y="101"/>
    <rect class="tile" x="201" y="101"/>
    <rect class="tile" x="226" y="101"/>
    <rect class="tile" x="251" y="101"/>

    <rect class="tile" x="1" y="126"/>
    <rect class="tile" x="26" y="126"/>
    <rect class="tile" x="51" y="126"/>
    <rect class="tile" x="76" y="126"/>
    <rect class="tile" x="101" y="126"/>
    <rect class="tile" x="126" y="126"/>
    <rect class="tile" x="151" y="126"/>
    <rect class="tile" x="176" y="126"/>
    <rect class="tile" x="201" y="126"/>
    <rect class="tile" x="226" y="126"/>
    <rect class="tile" x="251" y="126"/>

    <rect class="tile" x="1" y="151"/>
    <rect class="tile" x="26" y="151"/>
    <rect class="tile" x="51" y="151"/>
    <rect class="tile" x="76" y="151"/>
    <rect class="tile" x="101" y="151"/>
    <rect class="tile" x="126" y="151"/>
    <rect class="tile" x="151" y="151"/>
    <rect class="tile" x="176" y="151"/>
    <rect class="tile" x="201" y="151"/>
    <rect class="tile" x="226" y="151"/>
    <rect class="tile" x="251" y="151"/>

    <rect class="tile" x="1" y="176"/>
    <rect class="tile" x="26" y="176"/>
    <rect class="tile" x="51" y="176"/>
    <rect class="tile" x="76" y="176"/>
    <rect class="tile" x="101" y="176"/>
    <rect class="tile" x="126" y="176"/>
    <rect class="tile" x="151" y="176"/>
    <rect class="tile" x="176" y="176"/>
    <rect class="tile" x="201" y="176"/>
    <rect class="tile" x="226" y="176"/>
    <rect class="tile" x="251" y="176"/>

    <rect class="tile" x="1" y="201"/>
    <rect class="tile" x="26" y="201"/>
    <rect class="tile" x="51" y="201"/>
    <rect class="tile" x="76" y="201"/>
    <rect class="tile" x="101" y="201"/>
    <rect class="tile" x="126" y="201"/>
    <rect class="tile" x="151" y="201"/>
    <rect class="tile" x="176" y="201"/>
    <rect class="tile" x="201" y="201"/>
    <rect class="tile" x="226" y="201"/>
    <rect class="tile" x="251" y="201"/>

    <rect class="tile" x="1" y="226"/>
    <rect class="tile" x="26" y="226"/>
    <rect class="tile" x="51" y="226"/>
    <rect class="tile" x="76" y="226"/>
    <rect class="tile" x="101" y="226"/>
    <rect class="tile" x="126" y="226"/>
    <rect class="tile" x="151" y="226"/>
    <rect class="tile" x="176" y="226"/>
    <rect class="tile" x="201" y="226"/>
    <rect class="tile" x="226" y="226"/>
    <rect class="tile" x="251" y="226"/>

    <rect class="tile" x="1" y="251"/>
    <rect class="tile" x="26" y="251"/>
    <rect class="tile" x="51" y="251"/>
    <rect class="tile" x="76" y="251"/>
    <rect class="tile" x="101" y="251"/>
    <rect class="tile" x="126" y="251"/>
    <rect class="tile" x="151" y="251"/>
    <rect class="tile" x="176" y="251"/>
    <rect class="tile" x="201" y="251"/>
    <rect class="tile" x="226" y="251"/>
    <rect class="tile" x="251" y="251"/>
  </svg>

  <p>{{ board }}</p>

  </div>

</template>