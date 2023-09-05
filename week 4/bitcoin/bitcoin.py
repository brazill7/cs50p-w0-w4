import requests
import sys
#import json

def main():
    #only except int / check for value
    try:
        q = float(sys.argv[1])
    except:
        if len(sys.argv) == 2:
            print("Command-line argument is not a number")
        else:
            print("Missing command-line argument")
        sys.exit()

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        rsp = response.json()

        #print(json.dumps(rsp, indent=2))
    except:
        print("Error getting price")
        sys.exit()

    price = rsp["bpi"]["USD"]["rate_float"]

    output = q * price

    print(f"${output:,.4f}")


main()