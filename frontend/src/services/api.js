const API_BASE = "http://localhost:3001/api";

export async function getBoardState() {
  const response = await fetch(`${API_BASE}/state`);
  
  if (!response.ok) {
    throw new Error("API request failed!");
  }
  
  return response.json();
}

export async function getLegalMoves(location) {
  const response = await fetch(`${API_BASE}/moves`, {
    method: 'POST',
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      move: location
    })
  });
  
  if (!response.ok) {
    throw new Error("API request failed!");
  }

  return response.json();
}