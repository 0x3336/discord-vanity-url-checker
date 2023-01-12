# discord-vanity-url-checker

This script is used to check the validity of a list of Discord invite URLs. The script reads a list of URLs from a text file named "urls.txt" and checks each URL against the Discord API to determine if it is a valid, taken, or invalid URL.

## Usage

1. In the same directory as the script, create a text file named "urls.txt" and add each Discord invite URL that you want to check on a new line.
2. Run the script by executing the command `python scriptname.py`.
3. The script will output the status of each URL in the form of:
  * `{Fore.GREEN}{url}{Style.RESET_ALL} - Valid URL` : URL is valid
  * `{Fore.YELLOW}{url}{Style.RESET_ALL} - Taken URL` : URL is already used
  * `{Fore.RED}{url}{Style.RESET_ALL} - Invalid URL` : URL is invalid
4. If script receive 429 status code, it will be sleep for the amount of seconds specified in the `retry-after` header in the json.
5. The script will also write a list of invalid URLs to a text file named "invalid.txt".

## Dependencies

The script requires the following libraries:
- `requests` : for making HTTP requests to the Discord API
- `colorama` : for providing terminal colors
- `json` : for parsing the JSON response from the Discord API
- `time` : for pausing the script if it receives a rate limit status code.
