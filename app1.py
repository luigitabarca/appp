import urllib.request
import threading
from flask import Flask, render_template, jsonify
from GetTradesBinance import main, get_price_conversion_to_usd


#from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

# def sensor():
#     data = main()
#     print(data)

# sched = BackgroundScheduler(daemon=True)
# sched.add_job(sensor,'interval',seconds=15)
# sched.start()




app = Flask(__name__)

price=0.00090

@app.route('/')
def home():  
    data = main()
    return render_template('index.html', data=data, price=price)

@app.route('/data')
def load_data():
    data = main()
    return jsonify(data)





if __name__ == '__main__':
    app.run(debug=True)
