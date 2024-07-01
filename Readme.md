# Restaurant Cuisine Classifier

This project classifies restaurants based on their cuisines using a machine learning model. The model is trained using a dataset of restaurant information and is deployed using a Streamlit app.

## Table of Contents:

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [Streamlit App](#streamlit-app)
- [Contributing](#contributing)
- [License](#license)

## Project Structure:


restaurant-cuisine-classifier/
├── app.py
├── ML_Model.py
├── requirements.txt
├── README.md
├── dataset.csv



## Dataset Information

The predictive model was trained on the [Restaurant Rating Dataset](https://www.kaggle.com/datasets/uciml/restaurant-data-with-consumer-ratings) from Kaggle. This dataset contains various features of restaurants, such as average cost for two, price range, and votes, alongside their respective ratings. The dataset was preprocessed to handle missing values, categorical features, and normalization for better model performance.



## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/restaurant-cuisine-classifier.git
    cd restaurant-cuisine-classifier
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage:

1.) For Food Quality prediction in Food e-commerce

2.) small segements of the food serving websites can be improved so customers can decide which resto to choose thus this helps to improve customer acquasition cost.

### Model Training

1. **Prepare your dataset**:
    - Place your dataset CSV file in the project directory and update the `file_path` in `train_model.py`.

2. **Train the model**:
    ```bash
    python train_model.py
    ```
    - This script will preprocess the data, train a RandomForestClassifier, perform hyperparameter tuning, and save the best model as `restaurant_cuisine_model.pkl` and the label encoder as `label_encoder.pkl`.

### Streamlit App

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Interact with the app**:
    - Open your browser and go to the local URL provided by Streamlit.
    - Input the city, price range, aggregate rating, and votes to classify the restaurant's cuisine.

## Contributing:

Feel free to open issues or submit pull requests if you have suggestions or improvements.

## License:

This project is licensed under the MIT License.

