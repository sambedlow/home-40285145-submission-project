from flask import Flask, render_template
app = Flask(__name__)
import requests

@app.route("/trending/")
def trending():
    
    url = "https://uflixit.p.rapidapi.com/movies/wanted"
    headers = {'x-rapidapi-host': "uflixit.p.rapidapi.com",
               'x-rapidapi-key': "29d99ba68amshe199a4111698c64p1f8fbajsnb7cc4d6c79d8"
        }
    #response = requests.request("GET", url, headers=headers)
    
    ids = ["tt7131622","tt1206885","tt1025100","tt1302006","tt6189022",
              "tt7349950", "tt7286456", "tt5503686", "tt7798634","tt6324278"]
    titles = ["Once Upon a Time in Hollywood","Rambo: Last Blood","Gemini Man",
             "The Irishman","Angel Has Fallen","It Chapter Two","Joker","Hustlers",
             "Ready or Not","Abominable"]
    releasedyears = ["2019","2019","2019","2019","2019","2019","2019","2019","2019","2019"]
    ratingcounts = ["258165","31598","31519","85759","34595","124434","501877","25807",
                   "33313","8459"]
    ratings = ["7.9","6.4","5.7","8.3","6.5","6.8","8.7","6.5","6.9","7.0"]

    
    links = ["https://www.imdb.com/title/"+ids[0],
            "https://www.imdb.com/title/"+ids[1],
            "https://www.imdb.com/title/"+ids[2],
            "https://www.imdb.com/title/"+ids[3],
            "https://www.imdb.com/title/"+ids[4],
            "https://www.imdb.com/title/"+ids[5],
            "https://www.imdb.com/title/"+ids[6],
            "https://www.imdb.com/title/"+ids[7],
            "https://www.imdb.com/title/"+ids[8],
            "https://www.imdb.com/title/"+ids[9]
             ]
           
    i=0
    while i < len(ids):
		
        url = "https://imdb8.p.rapidapi.com/title/get-ratings"
        
        querystring = {"tconst":ids[i]}

        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': "29d99ba68amshe199a4111698c64p1f8fbajsnb7cc4d6c79d8"
            }

        #moviedict = requests.request("GET", url, headers=headers, params=querystring)

        i+=1

    return render_template('trendingfilms.html',ids=ids,titles=titles,
                           releasedyears=releasedyears,ratings=ratings,ratingcounts=ratingcounts,links=links)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


