import requests
import csv
import json

# Convert month numbers to month names for output
months_name = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

DATASET_ID = "pwn4-m3yp"
BASE_URL = f"https://data.cdc.gov/resource/{DATASET_ID}.json"

# Load state populations from states.csv
population = {}

with open("states.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        population[row[0]] = int(row[1])


def process_state(state):
    # Request weekly COVID-19 data for one state from the CDC API
    params = {
        "$where": f"state='{state}' AND end_date >= '2020-01-01' AND end_date <= '2023-12-31'",
        "$order": "end_date ASC"
    }

    req = requests.get(BASE_URL, params=params)

    # Convert the JSON response into Python data structures
    d = req.json()

    # Save the raw JSON data for this state
    with open(f"{state}.json", "w") as f:
        json.dump(d, f, indent=2)

    # Calculate the average weekly cases and find the week
    # with the highest number of new cases
    count = 0
    total = 0.0

    highest = {
        "date": "2019-01-01",
        "cases": 0.0
    }

    for row in d:
        cases = float(row["new_cases"])

        if highest["cases"] < cases:
            highest["date"] = row["end_date"]
            highest["cases"] = cases

        count += 1
        total += cases

    print("")
    print(f"State name: {state}")
    print(f"Average number of new weekly cases for the entire state dataset: {total / count:.2f}")
    print(
        f"Date with the highest new number of covid cases: "
        f"{highest['date'][:10]} ({int(highest['cases'])})"
    )

    # Group weekly cases by month and calculate monthly totals
    months = {}

    for row in d:
        month = row["end_date"][:7]
        cases = float(row["new_cases"])

        if month not in months:
            months[month] = 0

        months[month] += cases

    # Find the month with the highest total number of new cases
    my_highest = {
        "month": "2019-01",
        "cases": 0.0
    }

    for month, cases in months.items():
        if cases > my_highest["cases"]:
            my_highest["month"] = month
            my_highest["cases"] = cases

    month = my_highest["month"][5:7]

    # Calculate the percentage of the state's population
    # represented by cases during its highest month
    percentage = my_highest["cases"] / population[state] * 100

    print(
        f"Month and Year, with the highest new number of covid cases: "
        f"{months_name[month]} {my_highest['month'][:4]}"
        f"({int(my_highest['cases'])})"
    )

    print(
        f"Month and Year, with highest new number, percentage of population: "
        f"{percentage:.2f}% (Population: {population[state]})"
    )

    # Return the highest month information for comparison across states
    return {
        "state": state,
        "month": my_highest["month"],
        "cases": my_highest["cases"],
        "population": population[state],
        "percentage": percentage
    }


# Find the states with the highest and lowest population percentages
highest_population = {
    "state": "",
    "month": "",
    "cases": 0.0,
    "population": 0,
    "percentage": 0.0
}

lowest_population = {
    "state": "",
    "month": "",
    "cases": 0.0,
    "population": 0,
    "percentage": 100.0
}

for state in population:
    result = process_state(state)

    # Compare each state's highest-month percentage with the current highest
    if highest_population["percentage"] < result["percentage"]:
        highest_population = result

    # Compare each state's highest-month percentage with the current lowest
    if lowest_population["percentage"] > result["percentage"]:
        lowest_population = result


# Print the summary across all states
print("==================== SUMMARY ACROSS ALL STATES ====================")

month = highest_population["month"][5:7]

print("State with HIGHEST percentage of population during its highest month:")
print(
    f"{highest_population['state']} - "
    f"{highest_population['percentage']:.2f}% in "
    f"{months_name[month]} {highest_population['month'][:4]} "
    f"({int(highest_population['cases'])} cases; "
    f"Population: {highest_population['population']})"
)

month = lowest_population["month"][5:7]

print("State with LOWEST percentage of population during its highest month:")
print(
    f"{lowest_population['state']} - "
    f"{lowest_population['percentage']:.2f}% in "
    f"{months_name[month]} {lowest_population['month'][:4]} "
    f"({int(lowest_population['cases'])} cases; "
    f"Population: {lowest_population['population']})"
)