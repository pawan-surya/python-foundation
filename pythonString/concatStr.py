
store_address = "130 Dowanmark noraway"
state = "NY"
city = "Mount"

# full_address = store_address + " " + state + " " + city
full_address = f'{store_address} {city}'
# print(full_address)

campain_data = [
    {
        "campaignName": "Paint Bogo",
        "campaignId": "1",
        "startDate": "2025-12-01",
        "endDate": "2025-12-31"
    },
    {
        "campaignName": "Paint Sogo",
        "campaignId": "2",
        "startDate": "2025-12-01",
        "endDate": "2025-12-31"
    } 
]

for i in campain_data:
    if(i['campaignId'] == 1):
        i["is_active"] = True
    else:
        i['is_active'] = False

print(campain_data[0])