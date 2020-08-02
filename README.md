# Paladins_hero_rec
Python package to recommend which hero a player should select while drafting.

Author: Calvin M. Schmidt

Contact: calvinschmdt@gmail.com

Required programs: Python 3, Jupyter notebook to get past matches - can be installed here: https://jupyter.org/. 

Required packages: pyrez, numpy, pickle - All can be installed using "pip install pyrez", etc. in the command line.

Uses the Paladins API, the great work done by paladins.guru, and the awesome pyrez package developed by luissilva1044894 to pull down data on the player's past matches. During the draft portion of a casual or ranked match, the get_rec.py program can use this information to generate a recommendation based on the map, teammate heroes, and enemy heroes as to which hero the player should select based on their historical record encountering these conditions.

## To generate a recommendation:
1. Download the get_rec.py file and generate a match_list.pkl file. My match_list.pkl file is included as an example.
2. Edit the designated section of the get_rec.py file to include your player name and your list of available heroes.
3. Run "python get_rec.py" from the command prompt from the same directory that contains get_rec.py and match_list.pkl.
4. Enter the information on your match, adding one hero or map at a time.
  - Capitalization and spacing is important. Generally the first letter of each word. Examples: Brightmarsh, Jaguar Falls, Tyra, Mal'Damba.
5. After a hero or map is added, the current hero and map status is returned, along with the scores for each available hero. Higher scores mean more highly recommended based on past performance.
  - Recommendation does not take into account bans and other player picks to give available heroes.
  - Also does not take into account missing positions on the current team, so you may have to look down the list to find one that fits your current team composition. Don't use this as an excuse to leave your team without a healer or a tank!
  - Example on Brightmarsh with Tyra as a teammate and Moji as an enemy, recommending Ying and Lian: 
    - Brightmarsh ['Tyra'] ['Moji']
    - {'Seris': -1.3, 'Cassie': -0.5, 'Moji': -0.3, 'Jenos': -0.2, 'Ash': 0.0, 'Barik': 0.0, 'Grohk': 0.0, 'Lex': 0.0, 'Pip': 0.0, 'Ruckus': 0.0, 'Viktor': 0.0, "Mal'Damba": 0.0, 'Torvald': 0.0, 'Koga': 0.0, 'Grover': 0.5, 'Tyra': 0.5, 'Lian': 2.3, 'Ying': 2.3}
    
## To generate or update a match_list.pkl file:
1. Use this form to request a developer key: https://fs12.formsite.com/HiRez/form48/secure_index.html
2. Enter the required information into first cell of the "Get user data from API" notebook and run either the initial pull or update pull cells. Remember to make copies of the resulting match_list.pkl file!
### or
1. To get your list of past matches, fill out this form: https://docs.google.com/forms/d/e/1FAIpQLSfTg_As2BVXH3fhcN7S5DDJWYmgutjuHAU5xa5JT1WHUZNrAA/viewform?usp=sf_link. Please give me a few days to respond in case I am busy.
2. To update a list with new matches, send me an email with the title "Update Paladins match list". Include in the body your player name and a picture of a charity receipt, and attach your current match_list.pkl file for me to update. Remember that I can only pull down the 50 latest matches, so keep that in mind for how frequently it should be updated so as to not miss a match.

## Other tips:
1. You can use on a phone by downloading an app to run Python - good for those who play on the computer. I use Pydroid 3, but anything with a command line should work.
2. Tools for analyzing your past performance coming soon.
3. Machine learning-based recommendation tool coming soon.

## Common error messages when generating a recommendation:
1. python: can't open file 'get_rec.py': [Errno 2] No such file or directory
  - Make sure you are running the command while sitting in the folder that contains get_rec.py.
  - Can use the command "cd folder_name" to move to the folder_name subfolder from where you currently are.
2. FileNotFoundError: [Errno 2] No such file or directory: 'match_list.pkl'
  - Make sure you have a match_list.pkl file and it is in the same folder you are in.
3. ModuleNotFoundError: No module named 'pyrez.models'
  - Make sure you have installed all the required packages.
  - Use the command "pip install package_name" to automatically install.
