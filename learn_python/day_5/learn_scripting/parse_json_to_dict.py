import json

# Step 1. Use 'with' to open the 'servers.json' file
with open('servers.json', 'r') as original_json_file:
    # Step 2. Parse the contents of the JSON file into a Python dictionary named "servers'
    servers = json.load(original_json_file)

# Step 3. Print out the type of 'servers'
print("\n[Step 3.]")
print(f"The type of 'servers' is: {type(servers)}.")

# Step 4. Print out the dictionary record with the key "server1"
print("\n[Step 4.]")
print(f"The dictionary record with the key 'server1' is:\n{servers["server1"]}")

# Step 5. Print out the dictionary record with the key "server2"
print("\n[Step 5.]")
print(f"The dictionary record with the key 'server2' is:\n{servers["server2"]}")

print("\n===============================================================================================\n")

# Step 6. Print out all the keys and values.
print("[Step 6.]")
for server in servers:
    for key, value in servers.items():
        if key == server:
            key_pairs = value
            print(f"Key and value: '{server}' = '{key_pairs}'")
            for individual_key, individual_value in key_pairs.items():
                print(f"Record key and sub value: '{individual_key}' = '{individual_value}'")


