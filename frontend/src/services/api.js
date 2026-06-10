const API_BASE = "http://localhost:3001/api"

export async function test() {
  const response = await fetch(`${API_BASE}/test`)
  
  if (!response.ok) {
    throw new Error("API request failed")
  }
  
  return response.json()
}