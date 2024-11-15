document.addEventListener('DOMContentLoaded', () => {
    // Populate dropdowns dynamically
    const venues = ["Venue1", "Venue2", "Venue3"]; // Replace with actual data
    const teams = ["Team1", "Team2", "Team3"];
    const players = ["Player1", "Player2", "Player3"];
    
    populateDropdown('venue', venues);
    populateDropdown('battingTeam', teams);
    populateDropdown('bowlingTeam', teams);
    populateDropdown('striker', players);
    populateDropdown('bowler', players);
  
    document.getElementById('predictButton').addEventListener('click', predictScore);
  });
  
  function populateDropdown(id, options) {
    const dropdown = document.getElementById(id);
    options.forEach(option => {
      const opt = document.createElement('option');
      opt.value = option;
      opt.textContent = option;
      dropdown.appendChild(opt);
    });
  }
  
  function predictScore() {
    const data = {
      venue: document.getElementById('venue').value,
      battingTeam: document.getElementById('battingTeam').value,
      bowlingTeam: document.getElementById('bowlingTeam').value,
      striker: document.getElementById('striker').value,
      bowler: document.getElementById('bowler').value,
    };
  
    fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    })
      .then(response => response.json())
      .then(result => {
        document.getElementById('output').textContent = `Predicted Score: ${result.score}`;
      })
      .catch(error => console.error('Error:', error));
  }
  