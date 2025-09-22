import pandas as pd

input_csv = 'operations_2025_09_01.csv'
output_csv = 'KGSO_operations_output.csv'

target_airport = 'KGSO'

# Load CSV
df = pd.read_csv(input_csv)

# Clean flight IDs
df["flight"] = df["flight"].astype(str).str.strip()

# Build mapping dicts
takeoff_map = (
    df[df["operation"] == "takeoff"]
    .drop_duplicates("flight")
    .set_index("flight")["airport"]
    .to_dict()
)
landing_map = (
    df[df["operation"] == "landing"]
    .drop_duplicates("flight")
    .set_index("flight")["airport"]
    .to_dict()
)

# Create new columns
df["source"] = df["flight"].map(takeoff_map)
df["destination"] = df["flight"].map(landing_map)

# Clear irrelevant fields
df.loc[df["operation"] == "landing", "destination"] = None
df.loc[df["operation"] == "takeoff", "source"] = None

# Filter to target airport
matching_flights = df[df['airport'] == target_airport].copy()

# --- Reorder columns so source/destination are right after flight ---
cols = list(matching_flights.columns)
flight_index = cols.index("flight")

# Remove if already at the end
cols.remove("source")
cols.remove("destination")

# Insert next to flight
cols[flight_index+1:flight_index+1] = ["source", "destination"]

# Reorder dataframe
matching_flights = matching_flights[cols]

# Save result
matching_flights.to_csv(output_csv, index=False)
print(f"Flights info saved to {output_csv}")