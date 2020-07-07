# Paladins_hero_rec
Python package to recommend which hero one should select while drafting.
Author: Calvin M. Schmidt
Contact: calvinschmdt@gmail.com
Required programs: Python 3, Jupyter notebook to get past matches - can be installed here: https://jupyter.org/. 
Required packages: pyrez, numpy, pickle - All can be installed using "pip install pyrez", etc. in the command line.

Uses the Paladins API, the great work done by paladins.guru, and the awesome pyrez package developed by luissilva1044894 to pull down data on the player's past matches. During the draft portion of a casual or ranked match, the get_rec.py program can use this information to generate a recommendation based on the map, teammate heroes, and enemy heroes as to which hero the player should select based on their historical record encountering these conditions.

## To get information on a players past matches:
1. Use this form to request a developer key: https://fs12.formsite.com/HiRez/form48/secure_index.html
2. Enter the required information into first cell of the "Get user data from API" notebook and run either the initial pull or update pull cells. Remember to make copies of the resulting match_list.pkl file!
### or
1. Send me an email with the title "Get new Paladins match list". Include in the body your player name and a picture of a receipt for a charity of your choice and I will send you a match_list.pkl file to use with the get_rec.py program. Please give me a few days to respond in case I am busy.
2. To update a list with new matches, send me an email with the title "Update Paladins match list". Include in the body your player name and a picture of a charity receipt, and attach your current match_list.pkl file for me to update. Remember that I can only pull down the 50 latest matches, so keep that in mind for how frequently it should be updated so as to not miss a match.

## To generate a recommendation:
1. Edit the designated section of the get_rec.py file to include your player name and your list of available heroes.
2. Run "python get_rec.py" from the command prompt.
3. Enter the information on your match, adding one hero or map at a time.
  - Capitalization and spacing is important. Generally the first letter of each word. Examples: Brightmarsh, Jaguar Falls, Tyra, Mal'Damba.
4. After a hero or map is added, the current hero and map status is returned, along with the scores for each available hero. Higher scores mean more highly recommended based on past performance.
  - Recommendation does not take into account bans and other player picks to give available heroes.
  - Also does not take into account missing positions on the current team, so you may have to look down the list to find one that fits your current team composition. Don't use this as an excuse to leave your team without a healer or a tank!
  - Example on Brightmarsh with Tyra as a teammate and Moji as an enemy, recommending Ying and Ash: 
    - Brightmarsh ['Tyra'] ['Moji']
    - {'Grover': 0.2, 'Cassie': 0.25, 'Jenos': 0.3333333333333333, 'Seris': 0.3333333333333333, 'Talus': 0.3333333333333333, 'Moji': 0.35, 'Barik': 0.5, 'Grohk': 0.5, 'Lex': 0.5, 'Pip': 0.5, 'Ruckus': 0.5, 'Tyra': 0.5, 'Viktor': 0.5, "Mal'Damba": 0.5, 'Tiberius': 0.5, 'Torvald': 0.5, 'Ash': 0.75, 'Ying': 0.7692307692307693}

## Other tips:
1. You can use on a phone by downloading an app to run Python - good for those who play on the computer.
2. Tools for analyzing your past performance coming soon.
3. Machine learning-based recommendation tool coming soon.
