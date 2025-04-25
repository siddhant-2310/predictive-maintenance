# Predictive Maintenance System

This project predicts when industrial machines are likely to fail, allowing for better maintenance scheduling and reduced downtime.

## Features:
- **Data Preprocessing**: Includes feature scaling, missing value imputation, and categorical encoding.
- **Modeling**: A deep learning model is built using **TensorFlow**.
- **Web Application**: A **Flask** web app is built to allow users to upload data and get predictions.

## How to run:
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Train the model:
    ```bash
    python main.py
    ```
3. Run the Flask app:
    ```bash
    python app/app.py
    ```

