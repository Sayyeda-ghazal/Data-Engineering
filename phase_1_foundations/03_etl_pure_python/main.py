import json
import csv
from dataclasses import dataclass, asdict


# 1. Define data schema
@dataclass
class Customer:
    id: int
    city: str
    name: str
    country: str
    email: str
    age: int
    is_active: bool
    postal_code: str
    total_spent: float
    total_orders: int


# 2. Extract: Read JSON data
with open("data.json", "r") as file:
    data = json.load(file)


# 3. Transform: Flatten nested fields
cleaned_data = []

for customer in data:
    cleaned_data.append({
        "id": customer["id"],
        "name": customer["name"],
        "email": customer["email"],
        "age": customer["age"],
        "is_active": customer["is_active"],
        "city": customer["address"]["city"],
        "country": customer["address"]["country"],
        "postal_code": customer["address"]["postal_code"],
        "total_spent": customer["orders"]["total_spent"],
        "total_orders": customer["orders"]["total_orders"],
    })


# 4. Validate: Check data types
def validate_customer(record):
    expected_types = {
        "id": int,
        "name": str,
        "email": str,
        "age": int,
        "is_active": bool,
        "city": str,
        "country": str,
        "postal_code": str,
        "total_spent": float,
        "total_orders": int,
    }

    for field, expected_type in expected_types.items():
        if type(record[field]) is not expected_type:
            return False

    return True


valid_records = []
invalid_records = []

for record in cleaned_data:
    if validate_customer(record):
        valid_records.append(Customer(**record))
    else:
        invalid_records.append(record)


# 5. Load: Write valid records to CSV
valid_clean = [asdict(customer) for customer in valid_records]

if valid_clean:
    with open("cleaned_data.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=valid_clean[0].keys()
        )
        writer.writeheader()
        writer.writerows(valid_clean)


# 6. Print summary
print(f"Total records: {len(cleaned_data)}")
print(f"Valid records: {len(valid_records)}")
print(f"Invalid records: {len(invalid_records)}")
print("Invalid customers:", [record["name"] for record in invalid_records])
print("CSV export completed.")
