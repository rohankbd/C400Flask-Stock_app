from flask import *
import templates
import requests
from datetime import date

app = Flask("app")

API_KEY = 'VXBa0hBIQMgmRuzXUEvydOUx95YTRhrcuYlxyxbS'
API_URL = 'https://api.stockdata.org/v1/data/quote'
NEWS_API_URL = 'https://api.stockdata.org/v1/news/all'

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_data = None
    news_data = None

    if request.method == 'POST':
        symbol = request.form['symbol']
        params = {
            'symbols': symbol,
            'api_token': API_KEY
        }
        today = date.today()
        formatted_date = today.strftime("%Y-%m-%d")
        news_params = {
            'symbols': symbol,
            'api_token': API_KEY,
            'published_on': formatted_date
        }
        stock_response = requests.get(API_URL, params=params)
        news_response = requests.get(NEWS_API_URL, params=news_params)

        if stock_response.status_code == 200:
            stock_data = stock_response.json()
        else:
            stock_data = {'error': 'Failed to fetch stock data'}

        if news_response.status_code == 200:
            news_data = news_response.json()
        else:
            news_data = {'error': 'Failed to fetch news data'}

    return render_template('index.html', stock_data=stock_data, news_data=news_data)

app.run(debug=True)
