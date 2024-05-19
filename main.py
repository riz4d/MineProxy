import requests
import random
from Configs.config import api_url,host_urls_filenme
from modules.proxyapi import proxyfromapi
from modules.count import count_proxy_types

def print_proxy_status(proxy, status):
    if status:
        print(f"Proxy : {proxy}\nStatus : online.\n")
    else:
        print(f"Proxy : {proxy}\nStatus : offline.\n")

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.read().splitlines()
    return random.choice(urls)
    
def check_proxy(proxy,test_host_file):
    try:
        urls = read_urls_from_file(test_host_file)
        print(f"Host : {urls}")
        response = requests.get(f"http://{urls}", proxies={"http": proxy, "https": proxy}, timeout=5)
        
        if response.status_code == 200:
            return True
    except Exception as e:
        pass
    return False




def filter_and_save_proxy_type(file_path, proxy_type, save_as,host_file):
    filtered_proxies = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith(proxy_type):
                    filtered_proxies.append(line)

        if filtered_proxies:
            print(f"Proxies of type '{proxy_type}':")
            with open(save_as, 'a') as rfile:
                for proxy in filtered_proxies:
                    status = check_proxy(proxy,host_file)
                    print_proxy_status(proxy, status)
                    if status == True:
                        rfile.write(proxy + '\n')
                else:
                    print(f"No proxies of type '{proxy_type}' found in the file.")

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    print("Choose an option:")
    print("1. Scrape proxies from API")
    print("2. Enter your proxy file for checking\n")
    choice = input("Enter 1 or 2 : ")
    
    if choice == "1":
        proxyfromapi(api_url)
        file_path = "proxies.txt"
    else:
        file_path = input("Enter the text filename containing Proxies : ")
    proxy_types = count_proxy_types(file_path)
    if proxy_types:
        try:
            proxy_choice = int(input("Enter the number corresponding to the type of proxy you want to filter: ").strip())
            host_file = host_urls_filenme
            if 1 <= proxy_choice <= len(proxy_types):
                proxy_type = proxy_types[proxy_choice - 1]
                save_as = input("Enter the name to save filtered proxies (without extension): ").strip() + '.txt'
                print("\n\n")
                filter_and_save_proxy_type(file_path, proxy_type, save_as,host_file)
            else:
                print("Invalid proxy type number entered.")
        except ValueError:
            print("Invalid input. Please enter a number.")
