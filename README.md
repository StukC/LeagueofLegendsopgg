League of Legends Champion Guide Opener

This is a simple Python script that helps League of Legends players automatically open a champion guide on OP.GG for the champion they are currently playing in a live game. The script uses Riot Games API to fetch the required information.
Prerequisites

To use this script, you will need Python 3.x installed on your system. You can download the latest version of Python from the official website.
Installation

    Clone the repository or download the script.
    Install the required Python packages by running the following command:

pip install -r requirements.txt

Usage

    Replace the API_KEY in the script with your own Riot Games API key. If you don't have an API key, you can get one by signing up at the Riot Developer Portal.

python

API_KEY = "YOUR_API_KEY_HERE"

    Replace the summoner_name variable in the main() function with your League of Legends summoner name.

python

summoner_name = "YOUR_SUMMONER_NAME_HERE"

    Save the changes and run the script using the following command:

python league_champion_guide_opener.py

    The script will keep running in the background, and when you are in a live game, it will automatically open the champion guide for the champion you are playing in your default web browser.

Note

The script is set to check for a live game every 5 seconds. If you wish to change this interval, modify the value in the time.sleep() function in the main() function.

python

time.sleep(5)  # Change the value '5' to the desired number of seconds

License

This project is licensed under the MIT License. See the LICENSE file for details.
