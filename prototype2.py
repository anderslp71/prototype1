import sys
import textwrap # Used for potentially nicer formatting of long descriptions

# --- Data Store for Building/Service Information ---
# Keys are the codes/names users will type (converted to uppercase)
# Values are dictionaries containing details.
campus_data = {
    "JKB": {
        "Full Name": "Joseph Knight Building",
        "Services/Departments": [
            "BYU Testing Center (main location)",
            "Information Technology (IT) Department Offices",
            "Various Computer Labs",
            "Some Business School Classrooms/Offices"
        ],
        "Location Description": "Located directly West of the Wilkinson Student Center (WSC) and South of the Harold B. Lee Library (HBLL)."
    },
    "RB": {
        "Full Name": "Stephen L Richards Building",
        "Services/Departments": [
            "Main Athletics Facility",
            "Multiple Gymnasiums and Courts",
            "Swimming Pools",
            "Dance Studios",
            "Exercise Science Labs",
            "Athletic Department Offices"
        ],
        "Location Description": "Large athletics complex on South Campus, South of the Smith Fieldhouse (SFH) and West of the Indoor Practice Facility (IPF)."
    },
    "HH": {
        "Full Name": "Gordon B. Hinckley Alumni and Visitors Center",
        "Services/Departments": [
            "Alumni Association Offices",
            "Visitor Information Desk",
            "Event Spaces",
            "Small Cafe/Dining Area"
        ],
        "Location Description": "Prominent building located West of the Museum of Art (MOA) and North-West of the Wilkinson Student Center (WSC)."
    },
    "CTB": {
        "Full Name": "W. W. Clyde Engineering Building",
        "Services/Departments": [
            "College of Engineering Dean's Office",
            "Civil, Chemical, Electrical, Computer, Mechanical Engineering Departments",
            "Engineering Labs and Classrooms",
            "Small Engineering Library Branch"
        ],
        "Location Description": "Located on the East side of Campus Drive, North of the Tanner Building (TNRB) and South of the Eyring Science Center (ESC)."
    },
    "HBLL": {
        "Full Name": "Harold B. Lee Library",
        "Services/Departments": [
            "Main University Library",
            "Research Consultation",
            "Special Collections",
            "Family History Library",
            "Computer Labs / Printing Services",
            "Auditorium",
            "Study Areas"
        ],
        "Location Description": "Large central building located East of the Wilkinson Student Center (WSC) and North of the Joseph Smith Building (JSB)."
    },
    "WSC": {
        "Full Name": "Ernest L. Wilkinson Student Center",
        "Services/Departments": [
            "BYU Bookstore",
            "Cougareat Food Court",
            "Bowling Alley & Games Center",
            "Ballroom and Event Spaces",
            "Information Desk",
            "US Post Office",
            "BYUSA Offices",
            "Barber Shop"
        ],
        "Location Description": "Central hub of campus, located West of the Harold B. Lee Library (HBLL) and East of the Joseph Knight Building (JKB)."
    },
    "TESTING CENTER": { # Example of looking up a service directly
        "Full Name": "BYU Testing Center (Main Location)",
        "Services/Departments": [
            "Proctored Exams for various courses"
        ],
        "Location Description": "Located primarily within the Joseph Knight Building (JKB). Enter the JKB and follow signs."
    }
    # Add more buildings and services here as needed
}

def display_info(code):
    """Looks up and prints information for a given building/service code."""
    if code in campus_data:
        info = campus_data[code]
        full_name = info.get("Full Name", "N/A")
        services = info.get("Services/Departments", [])
        location = info.get("Location Description", "N/A")

        print("-" * 40)
        print(f"Information for: {code} ({full_name})")
        print("-" * 40)

        # Placeholder for where an image would appear
        print(f"\n--- Picture of: {full_name} ---\n")

        print("Key Services/Departments:")
        if services:
            for item in services:
                print(f"  - {item}")
        else:
            print("  - N/A")

        print("\nLocation:")
        # Use textwrap for potentially long location descriptions
        print(textwrap.fill(location, width=70, initial_indent="  ", subsequent_indent="  "))

        print("-" * 40)
    else:
        print(f"\n--- Sorry, information for '{code}' not found. ---")
        print("--- Please check the list or try a different code. ---")

# --- Main Kiosk Loop ---
if __name__ == "__main__":
    print("=" * 50)
    print(" Welcome to the BYU Building Information Kiosk!")
    print("=" * 50)

    while True:
        print("\nAvailable Building/Service Codes:")
        # Display available keys in columns for better readability
        codes = sorted(list(campus_data.keys()))
        cols = 3
        col_width = 20 # Adjust as needed
        for i in range(0, len(codes), cols):
            line_codes = codes[i:i+cols]
            print("".join(code.ljust(col_width) for code in line_codes))

        print("\nEnter a code from the list above to get information.")
        user_input = input("Enter code (or type 'QUIT' to exit): ").strip().upper()

        if user_input == "QUIT":
            break
        elif not user_input: # Handle empty input
            continue
        else:
            display_info(user_input)

        input("\nPress Enter to continue...") # Pause screen

    print("\nThank you for using the Kiosk. Goodbye!")
