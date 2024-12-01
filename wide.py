import requests
import sys

input_domain = sys.argv[1]


# URL to fetch the data from
url = f"https://crt.sh/?q={input_domain}&output=json"

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract common_name values
    common_names = []
    for cert in data:
        common_name = cert.get('common_name')
        if common_name:
            common_names.append(common_name)

    # Print the common names
    print("Common Name values:")
    for cn in common_names:
        print(cn)

    # Save the common names to a file
    with open(f"{input_domain}.txt", "w") as file:
        for cn in common_names:
            file.write(f"{cn}\n")
    
    print(f"Common names saved to {input_domain}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
