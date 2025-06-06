from flask import Flask, request, jsonify
from flask_cors import CORS
import utils
app = Flask(__name__)
CORS(app)

utils.load_saved_artifacts()


@app.route('/get_location_names',methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': utils.get_location_names()
    })
    response.headers.add('Acess-Control-Allow-Origin','*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = request.form['bhk']
    bath = request.form['bath']

    response = jsonify({
        'estimated_price': utils.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == "__main__":
    print('Starting python flask for price prediction')
    app.run()