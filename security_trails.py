import requests
import sys
import socket


def get_ip_address(domain):
    try:
        # Get the IP address for the given domain
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        return f"Error: {e}"

input_domain = sys.argv[1]
input_apikey = sys.argv[2]

print(f"[+] starting working on {input_domain}")
# Define the URL and headers

url = f"https://api.securitytrails.com/v1/domain/{input_domain}/subdomains"

headers = {
    'apikey': f'{input_apikey}'
}

# Make the GET request
response = requests.get(url, headers=headers)
response.json()

f = open(f"{input_domain}.txt", "w")

res = []

for sub in response.json()["subdomains"]:
    domainName = sub + "." + input_domain 
    res.append(f"{domainName}\t\t{get_ip_address(domainName)}")

f.writelines("\n".join(res))
f.close()
print(f"[+] file write finished for {input_domain}")