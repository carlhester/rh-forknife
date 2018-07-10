import requests
import json
from flask import Flask, render_template, request
import requests_cache
import configparser

requests_cache.install_cache(backend='memory', expire_after=180)

config = configparser.RawConfigParser()
config.read('config')

player = config['API']['playername']
apikey = config['API']['apikey']

URL = 'https://api.fortnitetracker.com/v1/profile/pc/' + player
headers = { "TRN-Api-Key" : apikey } 

app = Flask(__name__)

@app.route('/')
def index():
    stats = get_stats_from_data()
    return render_template('index.html', stats=stats)

def get_stats_from_data():
    temp_dict = {} 
    try:
        r = requests.get(URL, headers=headers)
        results = r.json()['lifeTimeStats']
        for r in results:
            if r['key'] == "Kills": temp_dict['kills'] = r['value']
            if r['key'] == "Matches Played": temp_dict['matches'] = r['value']
            if r['key'] == "Wins": temp_dict['wins'] = r['value']
            if r['key'] == "Top 3s": temp_dict['top3'] = r['value']
            if r['key'] == "Top 12s": temp_dict['top12'] = r['value']
            if r['key'] == "Top 25s": temp_dict['top25'] = r['value']
    except:
        return False

    return temp_dict

if __name__ == '__main__':
    app.run(debug=True)
