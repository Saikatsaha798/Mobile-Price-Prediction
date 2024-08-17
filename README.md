# Mobile-Price-Prediction

Here’s a comprehensive `README.md` template for your project that includes all the necessary details about deploying a Flask API for the Mobile Price Prediction model on Azure, troubleshooting, and usage instructions.

markdown
# Mobile Price Prediction API

This repository contains a Flask-based API for predicting mobile phone price ranges using a machine learning model. The API is deployed on Azure Web Apps.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
  - [Azure Deployment](#azure-deployment)
  - [Troubleshooting Deployment](#troubleshooting-deployment)
- [API Usage](#api-usage)
  - [Endpoints](#endpoints)
  - [Sample Request](#sample-request)
- [Common Issues](#common-issues)
- [License](#license)

## Overview

This project provides an API for predicting the price range of mobile phones using a machine learning model trained on the [Mobile Price Classification dataset](https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification). The model predicts one of four price ranges for a mobile phone based on various features.

The API is deployed on Azure Web Apps and is accessible at `https://mobilepriceprediction.azurewebsites.net/predict`.

## Getting Started

### Prerequisites

- Python 3.8+
- Flask
- Azure CLI
- Postman or `curl` for testing

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/mobile-price-prediction-api.git
   cd mobile-price-prediction-api
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app locally:**
   ```bash
   python app.py
   ```
   The app should now be running on `http://127.0.0.1:5000/`.

## Project Structure

```
mobile-price-prediction-api/
│
├── app.py                 # Main Flask app
├── mobile_price_model.pkl # Trained machine learning model
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Deployment

### Azure Deployment

To deploy this API to Azure, follow these steps:

1. **Create a ZIP file for deployment:**
   ```bash
   zip -r app.zip *
   ```

2. **Deploy to Azure using the Azure CLI:**
   ```bash
   az webapp deployment source config-zip --resource-group <YourResourceGroup> --name <YourAppServiceName> --src app.zip
   ```

3. **Set the Python runtime on Azure (for Linux-based App Service):**
   ```bash
   az webapp config set --resource-group <YourResourceGroup> --name <YourAppServiceName> --linux-fx-version "PYTHON|3.8"
   ```

### Troubleshooting Deployment

- **Virtual Environment Warnings:** These warnings can be ignored if your app runs correctly.
- **Missing `/predict` Endpoint:** Ensure you are using the correct HTTP method (`POST`) and check the logs using:
  ```bash
  az webapp log tail --resource-group <YourResourceGroup> --name <YourAppServiceName>
  ```
- **App Service Plan Issues:** If you encounter errors related to the service plan, consider upgrading to a plan that supports the required features (e.g., VNET integration).

## API Usage

### Endpoints

- **`/predict`** (POST): Predicts the price range of a mobile phone based on input features.

### Sample Request

Use Postman or `curl` to send a request to the `/predict` endpoint:

**Request:**
```bash
curl -X POST https://mobilepriceprediction.azurewebsites.net/predict \
-H "Content-Type: application/json" \
-d '{
  "battery_power": 842,
  "blue": 0,
  "clock_speed": 2.2,
  ...
}'
```

**Response:**
```json
{
  "prediction": "Medium cost"
}
```

## Common Issues

- **405 Method Not Allowed:** Ensure you are sending a `POST` request to the `/predict` endpoint.
- **Unsupported Python Version:** Ensure the correct Python version is set in your Azure Web App configuration.
- **Network Injection Warnings:** These are related to your Azure App Service plan and can be resolved by upgrading to a plan that supports advanced networking features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Summary

- **Customize**: Update the repository URL, resource group names, and app service names according to your setup.
- **Test the README**: Ensure all commands and steps work as expected in your environment.
- **Deploy and Verify**: After making any changes, redeploy and verify everything is functioning correctly.

This `README.md` file should serve as a comprehensive guide for anyone who wants to understand, run, or deploy the Mobile Price Prediction API.
