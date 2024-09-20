import time
from datetime import datetime
from datetime import timedelta
import pandas as pd
import subprocess

twitter_auth_token = '5a8f9aa92d21c015f493f2ae923e2d0a7126005f'
data = 'rockstar.csv'
# search_keyword = '#RockstarGames until:2023-12-01 since:2023-11-28 lang:en'
limit = 100

#Latest = RockstarGames until:2023-10-02 since:2023-10-01
start_date = datetime.strptime("2023-01-26", "%Y-%m-%d")
end_date = datetime.strptime("2023-01-27", "%Y-%m-%d")

# The following loop sends requests for Twitter data via a command line tool found here: https://github.com/helmisatria/tweet-harvest

for i in range(1):

  search_keyword = f'#RockstarGames until:{str(end_date.date())} since:{(start_date.date())} lang:en'
  cmd = f'npx --yes tweet-harvest@2.6.1 -o "{data}" -s "{search_keyword}" --tab "TOP"  -l {limit} --token {twitter_auth_token}'
  subprocess.run(cmd, shell=True)

  try:
    df = pd.concat(map(pd.read_csv, ['C:\\Users\\Hunts\\OneDrive\\Desktop\\Tweets Sept-Nov 2023.csv', 'C:\\Users\\Hunts\\OneDrive\\Desktop\\tweets-data\\rockstar.csv']), ignore_index=True)
    df.to_csv('C:\\Users\\Hunts\\OneDrive\\Desktop\\Tweets Sept-Nov 2023.csv')
  except:
    pass

  start_date = start_date - timedelta(days=1)
  end_date = end_date - timedelta(days=1)
  time.sleep(10)


