const API_BASE = "http://localhost:3001/api";

export async function getBoardState() {
  const response = await fetch(`${API_BASE}/state`);
  
  if (!response.ok) {
    throw new Error("API request failed! Failed to fetch board state.");
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
    throw new Error("API request failed! Failed to fetch legal moves.");
  }

  return response.json();
}

export async function resolveMove(select1, select2) {
  const response = await fetch(`${API_BASE}/move`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      start: select1,
      end: select2
    })
  });

  if (!response.ok) {
    return false;
  }

  return true;
}