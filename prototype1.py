import sys

def get_directions(start_location, destination_code):
    """
    Provides directions from a fixed start location to a chosen destination.

    Args:
        start_location (str): The starting building and room.
        destination_code (str): The code for the desired destination (JKB, RB, HC).

    Returns:
        list: A list of strings, where each string is a step in the directions.
              Returns None if the destination code is invalid.
    """
    directions_db = {
        "CTB250_TO_JKB": [
            "Exit CTB 250 and head towards the main South exit of the Clyde Building (CTB).",
            "Once outside, walk West along the main pathway.",
            "You will pass the Joseph Smith Building (JSB) on your right.",
            "Continue West towards the Wilkinson Student Center (WSC).",
            "The Joseph Knight Building (JKB) is directly West of the WSC.",
            "Look for the main East entrance of the JKB facing the WSC.",
            "You have arrived at the JKB."
        ],
        "CTB250_TO_RB": [
            "Exit CTB 250 and head towards the main South exit of the Clyde Building (CTB).",
            "Once outside, turn slightly left (South-East) and walk across the open area.",
            "You should see the Marriott School of Business (TNRB / Tanner Building) ahead.",
            "Walk South, keeping the TNRB on your left.",
            "Continue South past the Jesse Knight Building (JKB - different from Joseph Knight!).",
            "Follow the main pathway downhill towards the large athletics complex.",
            "The Richards Building (RB) is the main athletic building, located South of the Smith Fieldhouse.",
            "Look for entrances facing North or West.",
            "You have arrived at the RB."
        ],
        "CTB250_TO_HH": [
            "Exit CTB 250 and head towards the main North exit of the Clyde Building (CTB) - near the elevators.",
            "Once outside, walk North towards the Museum of Art (MOA).",
            "When you reach the plaza area near the MOA, turn West (left).",
            "Walk along the North side of the MOA.",
            "The Hinckley Alumni and Visitors Center (HC) is the prominent building directly West of the MOA.",
            "Enter through the main East-facing doors.",
            "You have arrived at the HC."
        ]
    }

    lookup_key = f"{start_location.replace(' ','')}_TO_{destination_code.upper()}" # Format key for lookup

    return directions_db.get(lookup_key) # Returns the list of steps or None if key doesn't exist

# --- Main Program ---
if __name__ == "__main__":
    current_location = "CTB250" # Fixed starting location
    valid_destinations = {
        "JKB": "Joseph Knight Building",
        "RB": "Richards Building (Athletics)",
        "HC": "Hinckley Center (Alumni/Visitors)"
    }

    print("-" * 40)
    print("Welcome to the Simple Campus Navigator!")
    print(f"Current Location: {current_location}")
    print("-" * 40)
    print("Available Destinations:")
    for code, name in valid_destinations.items():
        print(f"  - {code}: {name}")
    print("-" * 40)

    while True:
        destination_choice = input("Enter the code for your destination (JKB, RB, or HC): ").strip().upper()

        if destination_choice in valid_destinations:
            directions = get_directions(current_location, destination_choice)
            if directions:
                print(f"\n--- Directions from {current_location} to {valid_destinations[destination_choice]} ({destination_choice}) ---")
                for i, step in enumerate(directions):
                    print(f"{i + 1}. {step}")
                print("----------------------------------------")
                break # Exit the loop after successful directions
            else:
                # This case should technically not be hit if validation is correct, but good practice
                print("Error: Could not retrieve directions for a valid choice. Please contact support.")
                sys.exit(1) # Exit with an error code
        else:
            print(f"Invalid destination code '{destination_choice}'. Please enter one of {', '.join(valid_destinations.keys())}.")
            # Loop continues to ask again

    print("\nNavigation complete. Have a great day!")
