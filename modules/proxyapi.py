import requests

def proxyfromapi(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        proxies = response.text
        output_file = "proxies.txt"
        with open(output_file, "w") as file:
            file.write(proxies)
        print(f"Proxies have been saved to {output_file}")
    else:
        print(f"Failed to fetch proxies. Status code: {response.status_code}")
