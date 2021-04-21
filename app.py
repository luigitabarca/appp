from flask import Flask, render_template,jsonify
import json
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')


@app.route('/test.json')
def indexBinance():
    json_file=open('pretBinance.json',)
    data = json.load(json_file)
    return jsonify(data)




if __name__ == '__main__':
   app.run()