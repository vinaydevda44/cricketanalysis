from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Initialize Flask app
app = Flask(__name__)

# Load model and encoders
model = tf.keras.models.load_model('model.h5')
scaler = MinMaxScaler()
venue_encoder = LabelEncoder()
batting_team_encoder = LabelEncoder()
bowling_team_encoder = LabelEncoder()
striker_encoder = LabelEncoder()
bowler_encoder = LabelEncoder()

# Sample encoders and scaler loading
# Replace with your actual encoding logic
# Assume you have saved and reloaded LabelEncoder mappings
venues = ["Venue1", "Venue2", "Venue3"]
teams = ["Team1", "Team2", "Team3"]
players = ["Player1", "Player2", "Player3"]

venue_encoder.fit(venues)
batting_team_encoder.fit(teams)
bowling_team_encoder.fit(teams)
striker_encoder.fit(players)
bowler_encoder.fit(players)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Transform input data
    input_data = np.array([
        venue_encoder.transform([data['venue']])[0],
        batting_team_encoder.transform([data['battingTeam']])[0],
        bowling_team_encoder.transform([data['bowlingTeam']])[0],
        striker_encoder.transform([data['striker']])[0],
        bowler_encoder.transform([data['bowler']])[0]
    ]).reshape(1, -1)

    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)

    return jsonify({'score': int(prediction[0][0])})

if __name__ == '__main__':
    app.run(debug=True)
