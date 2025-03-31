# Processing Map Data with Metadata
 
 📌 Overview

This project processes and analyzes location data by merging two JSON files: one containing location coordinates and another with metadata like type, rating, and reviews. The script performs various analytical tasks, such as counting valid locations per type, calculating average ratings, and identifying the most reviewed location.

📂 Project Structure

📦 map-data-processing
├── locations.json       # JSON file with location coordinates
├── metadata.json        # JSON file with metadata (type, rating, reviews)
├── process_data.py      # Main script for data processing
├── requirements.txt     # Dependencies for the project
└── README.md            # Project documentation

🚀 Features

Merges location data with metadata based on id.

Counts the number of valid points per type (e.g., restaurants, hotels, cafes).

Calculates the average rating per type.

Identifies the location with the highest number of reviews.

Detects locations with missing or incomplete data (Bonus Task).


⚙️ Installation & Setup

1. Clone the repository
   
   git clone https://github.com/your-username/map-data-processing.git
   cd map-data-processing
   
2. Install dependencies

   pip install -r requirements.txt

3. Run the script

   python process_data.py

🌍 Deployment

The application is hosted at: 

📊 Example Output

{
  "valid_points_per_type": {
    "restaurant": 3,
    "hotel": 3,
    "cafe": 2
  },
  "average_ratings": {
    "restaurant": 4.1,
    "hotel": 3.4,
    "cafe": 4.6
  },
  "most_reviewed_location": {
    "id": "loc_07",
    "reviews": 900
  },
  "incomplete_data": []
}

🛠 Tech Stack

Python (for data processing)

Flask/FastAPI (for API deployment - if applicable)

JSON (for data storage)


✍️ Created by Lopamudra Sahoo
