import pandas as pd


# 1. Load the NYC Taxi dataset
print("Loading dataset...")
dataset = pd.read_parquet("yellow_tripdata_2025-01.parquet")

print(f"Dataset shape: {dataset.shape}")


# 2. Load the taxi zone lookup dataset
print("\nLoading taxi zone lookup...")
zones = pd.read_csv("taxi_zone_lookup.csv")


# 3. Add borough names to taxi trip records
print("\nMapping pickup locations to boroughs...")
dataset = dataset.merge(
    zones[["LocationID", "Borough"]],
    left_on="PULocationID",
    right_on="LocationID",
    how="left"
)

print(dataset[["PULocationID", "Borough", "fare_amount"]].head())


# 4. Extract the pickup hour
print("\nExtracting pickup hours...")
dataset["hour"] = dataset["tpep_pickup_datetime"].dt.hour

print(
    dataset[
        ["tpep_pickup_datetime", "Borough", "fare_amount", "hour"]
    ].head()
)


# 5. Calculate average fare per borough per hour
print("\nCalculating average fare...")
average_fare = (
    dataset.groupby(["Borough", "hour"])["fare_amount"]
    .mean()
    .reset_index()
)

print(average_fare.head(20))


# 6. Save the results to a CSV file
output_file = "average_fare_csv.csv"

average_fare.to_csv(output_file, index=False)

print(f"\nResults saved to {output_file}")
