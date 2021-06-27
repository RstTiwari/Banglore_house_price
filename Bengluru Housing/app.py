from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('banglore.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        area_type = int(request.form['area_type'])
        available= float(request.form['availabiltity'])
        size= int(request.form['size'])
        bath = int(request.form['bath'])
        balcony = int(request.form['balcony'])
        total_sqft_int = int(request.form['total_sqft.form'])

        prediction = model.predict([[area_type, available, size, bath, balcony, total_sqft_int]])
        output = round(prediction[0], 2)
        if output < 0:
            return render_template('index.html', prediction_texts="Sorry you cannot sell this flat")
        else:
            return render_template('index.html', prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)







