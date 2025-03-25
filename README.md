# 🌴 Vacation Decision Tree Planner

A Streamlit app that helps you plan your ideal vacation based on your preferences and budget! Answer a series of questions to get personalized vacation recommendations.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://vacation-decision-tree.streamlit.app/)

## Features

- **Budget-Based Recommendations**: Choose your budget and get tailored vacation suggestions.
- **Vacation Types**: Options for family trips, romantic getaways, adventure holidays, and more.
- **Destination Preferences**: Select between beaches, mountains, cultural experiences, and more.
- **Booking Preferences**: Decide whether to self-book, use a travel agent, or stay with friends/family.
- **Interactive Decision Tree**: Navigate through a series of questions to find your perfect vacation.

## How to Run the App Locally

1. **Install the requirements**:

   ```bash
   $ pip install -r requirements.txt
   ```

2. **Run the app**:

   ```bash
   $ streamlit run streamlit_app.py
   ```

3. **Open the app**:
   The app will open in your default web browser. If it doesn't, navigate to the URL displayed in your terminal (e.g., `http://localhost:8501`).

## How It Works

The app uses a JSON-based decision tree to guide you through a series of questions, such as:
- What is your budget?
- Do you prefer beaches or mountains?
- Is this a family trip or a romantic trip?
- Do you want to travel internationally?
- What type of holiday are you interested in (e.g., beach, culture, adventure)?

Based on your answers, the app provides personalized vacation recommendations.

## Example Use Case

1. Select your budget (e.g., "Under $1000").
2. Choose your preference (e.g., "Beaches").
3. Specify the type of trip (e.g., "Family Trip").
4. Get a recommendation (e.g., "Consider a local family-friendly beach vacation.").

## Contributing

Feel free to fork this repository and submit pull requests to improve the app or add new features!

## License

This project is licensed under the MIT License.
