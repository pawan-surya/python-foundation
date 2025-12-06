# Generate the Campain List Using various data type 

input_data = input("What is your name:")
print(f"Good moring {input_data} Your Json is being prepare")

for i in range(5):
    print(f"Generating Json file {i+1}/5")
    campaign = {
        "id": i + 1,
        "name": f"Campaign_{i + 1}",
        "active": True if i % 2 == 0 else False,
        "budget": 1000 + (i * 500),
        "tags": ["tag1", "tag2", f"tag{i + 1}"],
        "metadata": {
            "created_by": input_data,
            "priority": "high" if i % 2 == 0 else "low"
        },
        "start_date": f"2023-0{i + 1}-01",
        "end_date": f"2023-0{i + 2}-01",
        "locationData": [{
            "country": "Country_" + str(i + 1),
            "city": "City_" + str(i + 1),
            "coordinates": {
                "lat": 10.0 + i,
                "long": 20.0 + i
            },
            "location_name":  f"Lantern Model {chr(65 + i)}",
            "location_id": f" {chr(65 + i)}{chr(65 + i + 12)}"
        }]
    }
    print(campaign)
