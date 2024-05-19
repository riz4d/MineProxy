def count_proxy_types(file_path):
    proxy_types = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if '://' in line:
                    proxy_type = line.split('://')[0]
                    if proxy_type not in proxy_types:
                        proxy_types.append(proxy_type)

        print("Types of Proxies Available:\n")
        for idx, proxy_type in enumerate(proxy_types, start=1):
            print(f"{idx}. {proxy_type}")

        return proxy_types

    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None