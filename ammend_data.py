import pandas as pd

# Sample data for testing
data = {
    'itemName': [
        'XXXXXXXXX001',
        'XXXXXXXXX002',
        'XXXXXXXXX003',
        'YYYYYYYYY001',
        'YYYYYYYYY002',
        'ZZZZZZZZZ001'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group items by the first 9 characters of 'itemName'
grouped_items = {}
for item in df['itemName']:
    prefix = item[:9]
    suffix = item[9:]
    if prefix not in grouped_items:
        grouped_items[prefix] = []
    grouped_items[prefix].append(suffix)

# Construct new item names
new_item_names = []
for item in df['itemName']:
    prefix = item[:9]
    suffixes = grouped_items[prefix]
    combined_suffixes = "/".join(sorted(suffixes))
    new_item_name = f"{prefix} {combined_suffixes}"
    new_item_names.append(new_item_name)

# Update the DataFrame
df['itemName'] = new_item_names

# Save the updated DataFrame to a new CSV file
df.to_csv('output.csv', index=False)

print("The 'itemName' column has been updated and saved to 'output.csv'.")

# Print the updated DataFrame for verification
print(df)
