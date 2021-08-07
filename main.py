from flask import Flask, render_template
import requests, schedule

app = Flask(__name__)

def indo():
    api_url = "https://api.kawalcorona.com/indonesia/"
    result = requests.get(api_url).json()
    return result

#untuk membuat real time apabila website api kawalcorona terupdate
rt_indo = schedule.every(2).seconds.do(indo)

# while True:
#     schedule.run_pending()

data_indo = indo()


@app.route('/')
def index():
    return render_template("index.html", data_indo = data_indo)

if __name__ == "__main__":
    app.run(debug=True)