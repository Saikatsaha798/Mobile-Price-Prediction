from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('mobile_price_model.pkl')

@app.route('/predict', methods=['post'])
def predict():
	try:
		# Get the JSON data from the POST request
		data = request.get_json()

		# Convert the JSON data to a pandas DataFrame
		input_data = pd.DataFrame([data])

		# print([data])

		# Make predictions using the trained model
		prediction = model.predict(input_data)

		price_range = {
			0 : 'Low cost',
			1 : 'Medium cost',
			2 : 'High cost',
			3 : 'Very high cost'
		}

		# Return the predictions as a JSON response
		return jsonify({'prediction' : price_range[int(prediction[0])]})

	except Exception as e:
		return jsonify({'error' : str(e)})

if __name__ == '__main__':
	app.run(debug=True)