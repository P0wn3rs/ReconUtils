#!/bin/bash

#get_certificate_nuclei () {
 #   input="${1:-/dev/stdin}"  # Use file argument or read from stdin
 #   cat "$input" | nuclei -t ~/Desktop/Tools/ssl.yaml -silent -j | jq -r '.["extracted-results"][]'
#}
#!/bin/bash

#get_certificate_nuclei () {
    # Read input from stdin or file
 #   input="${1:-/dev/stdin}"
  #  cat "$input" | nuclei -t ~/Desktop/Tools/ssl.yaml -silent -j | jq -r '.["extracted-results"][]'
#}

# Allow the function to run directly if script is called
#get_certificate_nuclei "$@"
#!/bin/bash

get_certificate_nuclei () {
    if [[ -f "$1" ]]; then
        # If the argument is a file, read its content
        cat "$1" | nuclei -t ./ssl.yaml
 -silent -j | jq -r '.["extracted-results"][]'
    else
        # If the argument is not a file, treat it as plain text input
        echo "$1" | nuclei -t ./ssl.yaml -silent -j | jq -r '.["extracted-results"][]'
    fi
}

# Allow the function to run directly when the script is executed
get_certificate_nuclei "$@"

