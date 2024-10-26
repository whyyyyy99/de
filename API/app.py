import os

from flask import Flask, request

from housing_predict import HousingPredictor

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/housing_predict/', methods=['POST']) # path of the endpoint. Except only HTTP POST request
def predict_str():
    # the prediction input data in the message body as a JSON payload
    prediction_input = request.get_json()
    print(prediction_input)
    return dp.predict_single_record(prediction_input)


dp = HousingPredictor()
# The code within this conditional block will only run the python file is executed as a
# script. See https://realpython.com/if-name-main-python/
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)

