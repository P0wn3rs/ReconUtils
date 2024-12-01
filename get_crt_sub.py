#!/usr/bin/python3

import requests
import sys
import json
import io
from contextlib import redirect_stdout
import os

def get_domains(domain):
    url = f"https://crt.sh/?q={domain}&output=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open('out.txt', 'w') as f:
            # Extract and print only the 'name_value' field from each entry
            for item in data:
                name_value = item.get("name_value", "")
                if name_value:
                    # Print the 'name_value' (this may contain multiple domains separated by commas)
                    print(name_value, file=f)
        f.close()
    else:
        print(f"Failed to retrieve data from crt.sh. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: script.py domain.tld")
        sys.exit(1)

    domain = sys.argv[1]
    get_domains(domain)
    f = open("out.txt", "r")
    lines = set(f.readlines())
    f.close()
    lines = list(lines)
    unique_domains = set(line.strip().replace("www.", "") for line in lines if line.strip())
    final_list = sorted(unique_domains)    
    print("\n".join(final_list))
    os.remove("out.txt") 
