const API_BASE = "http://localhost:3001/api"

export async function getBoardState() {
  const response = await fetch(`${API_BASE}/state`)
  
  if (!response.ok) {
    throw new Error("API request failed")
  }
  
  return response.json()
}