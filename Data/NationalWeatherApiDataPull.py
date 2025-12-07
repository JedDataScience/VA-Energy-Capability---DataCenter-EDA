import requests
import pandas as pd

api_key = "DQJkrOIBKfhw6IDCRaDzEufdY1S0Xn2CuRCHWuhk"

url = (
    "https://api.eia.gov/v2/electricity/state-electricity-profiles/capability/data/"
    "?frequency=annual"
    "&data[0]=capability"
    "&facets[stateId][]=VA"
    "&start=1990"
    "&end=2024"
    "&sort[0][column]=period"
    "&sort[0][direction]=desc"
    "&offset=0"
    "&length=5000"
    f"&api_key={api_key}"
)

# Fetch from API
print("Fetching data from API...")
response = requests.get(url)
response.raise_for_status()

# Parse JSON
data = response.json()
print(f"API Response Keys: {data.keys()}")

# Convert to DataFrame
df = pd.json_normalize(data["response"]["data"])
print(f"DataFrame shape: {df.shape}")

# Save to CSV
df.to_csv("va_electricity_capability.csv", index=False)
print("CSV file saved successfully!")

print("\nFirst few rows:")
print(df.head())