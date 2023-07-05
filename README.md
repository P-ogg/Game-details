# Game-details
Get list of video games and details from mobygames.com
This code calls mobygames API, gets a list of games in json, parses the json, prints as pandas DataFrame, and saves to CSV.

The code contains two parts:
The first part prints one game (and its details) as a DataFrame. This can be modified to print more than 1 game.
The second part saves 5000 games (and their details) to a CSV in chunks.
