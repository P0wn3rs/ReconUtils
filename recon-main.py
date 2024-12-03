import json

options = {
    "domain-discovery": {
        "security-trails": {
            "command": "python3 security_trails.py <domain-name> <api-key>",
            "hint": "check the site for change logs, updates and new features"
        },
        "security-trails-just-sub": "python3 security_trails_just_sub.py <domain-name> <api-key>",
        "crt.sh": {
            "command": "python3 get_crt_sub.py <domain-name>",
            "hint": "check the site"
        },
        "certificate check": {
            "command": "cat range_ips.txt | xargs -I ip echo ip | mapcidr -silent | /home/kali/go/bin/httpx -silent | xargs -I inp ./get_certificate_nuclei.sh inp",
            "hint": "range ip file should contain <ip>/<cidr> in each line"
        },
        "checking urls in js file": "echo <domain-name> | waybackurls",
        "assetfinder": "TODO: add example",
    }
}


def main():
    print("##############################################################")
    print("# Owner: P0wn3rs                                             #")
    print("# github: github.com/P0wn3rs                                 #")
    print("##############################################################")
    print("# this is recon phase                                        #")
    print("# for better results save them in maltego or xmind           #")
    print("##############################################################")
    while True:
        print("please enter what you wanna do?")
        print("0. exit")
        for i, key in zip(range(1,options.keys().__len__()+1), options.keys()):
            print(f"{i}. {key}")
        action = input("> ")
        if action == "0":
            exit()
        print(json.dumps(options[list(options.keys())[int(action)-1]], indent=4))


if __name__ == "__main__":
    main()