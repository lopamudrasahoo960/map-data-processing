import json

# Function to load JSON data
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Function to merge location and metadata
def merge_data(locations, metadata):
    metadata_dict = {item["id"]: item for item in metadata}
    merged_data = []
    incomplete_data = []

    for location in locations:
        loc_id = location["id"]
        if loc_id in metadata_dict:
            merged_data.append({**location, **metadata_dict[loc_id]})
        else:
            incomplete_data.append(location)  # Missing metadata

    return merged_data, incomplete_data

# Function to analyze data
def analyze_data(merged_data):
    type_counts = {}
    type_ratings = {}
    highest_reviews = {"id": None, "reviews": 0}

    for data in merged_data:
        loc_type = data["type"]
        rating = data.get("rating")
        reviews = data.get("reviews", 0)

        # Count locations per type
        type_counts[loc_type] = type_counts.get(loc_type, 0) + 1

        # Sum ratings per type
        if loc_type in type_ratings:
            type_ratings[loc_type].append(rating)
        else:
            type_ratings[loc_type] = [rating]

        # Check for highest reviews
        if reviews > highest_reviews["reviews"]:
            highest_reviews = {"id": data["id"], "reviews": reviews}

    # Calculate average ratings
    avg_ratings = {key: round(sum(vals) / len(vals), 1) for key, vals in type_ratings.items()}

    return {
        "valid_points_per_type": type_counts,
        "average_ratings": avg_ratings,
        "most_reviewed_location": highest_reviews,
    }

if __name__ == "__main__":
    # Load data
    locations = load_json("locations.json")
    metadata = load_json("metadata.json")

    # Merge data
    merged_data, incomplete_data = merge_data(locations, metadata)

    # Analyze data
    analysis_results = analyze_data(merged_data)

    # Include incomplete data information
    analysis_results["incomplete_data"] = incomplete_data

    # Print output
    print(json.dumps(analysis_results, indent=4))
