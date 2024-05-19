# MineProxy
MineProxy is python script it does more than just check proxies are working.
It can gather proxies from your computer or mine from online and test them to see if they're active, and then save the ones that work best into a new file.

### Features

  - Proxy Type Identification:<br>Reads a list of proxies and identifies the different types based on their scheme (e.g., http, https, socks4).
  - Proxy Scraping:<br>Scrapes proxies from external sources.
  - Proxy Status Check:<br>Tests each proxy to determine if it is online.
  - Filtering:<br>Filters proxies based on their type.
  - Saving Online Proxies:<br>Saves only the online proxies of a specified type to a new file.
  - Support Bulk Scale Proxies:<br>Deterrmine a large amount of proxies from a file or online
### Installation

  1. Clone the repository or download the script files.
     ```sh
     git clone https://github.com/yourusername/MineProxy.git
     ```
     ```sh
     cd MineProxy
     ```
  2. Install the required Python packages.
     ```sh
     pip install requirements.txt
     ```

### Usage

  1. Use own proxy list file (optional):<br>If you have a list of proxies in a text file with each proxy in the following format:<br>
     ```arduino
     http://123.123.123.123:8080
     https://234.234.234.234:8080
     socks4://345.345.345.345:1080
     ```
  2. test host URLs file:<br>Ensure you have a text file (host.txt) containing URLs to be used for proxy testing.if you need more add there<br>
  3. Run the script:
     ```sh
     python main.py
     ```
  4. Follow the prompts:<br>
       - The script will ask if you want to scrape proxies from external sources. Enter 1 or 2.
       - If you choose to scrape proxies, the script will then ask you to select a source.
       - Next, the script will display the available types of proxies found in the file or scraped.
       - Enter the number corresponding to the proxy type you wish to filter.
       - Enter the name of the file (without extension) to save the filtered proxies.


### Issues 

[Submit Issues](https://github.com/riz4d/MineProxy/issues)

### License

This project is licensed under MIT license, [MIT](LICENSE) file for details.

