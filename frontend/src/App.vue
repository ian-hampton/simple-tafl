<script setup>
import { ref, onMounted } from 'vue'
import * as api from './services/api'

const message = ref("Loading...")

onMounted(async () => {
  try {
    const data = await api.test()
    message.value = data.message
  } catch (err) {
    message.value = "Failed to connect to backend."
  }
})
</script>

<template>
  <div style="text-align: center; margin-top: 100px;">
    <h1>Test</h1>
    <p>{{ message }}</p>
  </div>
</template>