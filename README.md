# **Student Performance Prediction - Machine Learning Project**

This project predicts students' performance based on multiple factors such as **gender**, **race/ethnicity**, **parental level of education**, **lunch**, **test preparation course**, and scores in **math**, **reading**, and **writing**. It is an end-to-end machine learning pipeline, from data preprocessing to model evaluation.

---

## **Table of Contents**

- [Installation](#installation)
- [Project Structure](#project-structure)
- [How to Run the Project](#how-to-run-the-project)
- [Features](#features)
- [Modeling](#modeling)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## **Installation**

Follow these steps to install and run the project:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Rahul-404/mlproject.git
    cd mlproject
    ```

2. **Create and activate a virtual environment** (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables** (if required for external APIs, etc.).

---

## **Project Structure**

The project is organized as follows:

```
mlproject/
│
├── src/
│   └── mlproject/
│       ├── __init__.py                      # Initialization of the project package
│       ├── components/
│       │   ├── __init__.py                  # Component initialization
│       │   ├── data_ingestion.py           # Data ingestion logic
│       │   ├── data_transformation.py      # Data transformation/feature engineering
│       │   ├── model_trainer.py            # Model training pipeline
│       │   └── model_monitoring.py         # Model monitoring and evaluation
│       ├── pipeline/
│       │   ├── __init__.py                 # Pipeline initialization
│       │   ├── training_pipeline.py        # Training pipeline logic
│       │   └── prediction_pipeline.py      # Prediction pipeline logic
│       ├── exception.py                    # Custom exceptions
│       ├── logger.py                       # Logging utilities
│       ├── utils.py                        # Utility functions
├── app.py                                  # Main script for running the app
├── Dockerfile                              # Docker configuration
├── requirements.txt                        # Python dependencies
├── setup.py                                # Setup script for packaging
├── artifacts/                              # Directory for saving trained models and outputs
└── README.md                               # Project documentation
```

- **`src/{project_name}/`**: The main source code directory where all the core project files are located.
- **`components/`**: Contains the logic for individual components of the machine learning pipeline, including data ingestion, transformation, training, and monitoring.
- **`pipeline/`**: Contains the pipeline scripts that orchestrate the data flow and model training/prediction processes.
- **`exception.py`**: Contains custom exceptions for error handling.
- **`logger.py`**: Logging utilities to keep track of the application's execution and errors.
- **`utils.py`**: Utility functions used throughout the project for tasks such as metrics calculation and data loading.
- **`app.py`**: Main entry point for running the application and interacting with the trained model.
- **`Dockerfile`**: Configuration file to containerize the application using Docker.
- **`requirements.txt`**: Contains a list of dependencies required to run the project.
- **`setup.py`**: Setup script for packaging and installing the project.
- **`artifacts/`**: Directory for storing models, data, and outputs generated during training and prediction.

---

## **How to Run the Project**

### 1. **Run the Application**

To start the application and interact with the model, use the following command:

```bash
python app.py
```

This will launch the application and allow you to make predictions based on input data such as student scores and personal information.

---

## **Features**

- **Data Ingestion**: Loads raw data from external sources (e.g., CSV, database).
- **Data Transformation**: Preprocesses the data by encoding categorical features, handling missing values, and scaling numerical features.
- **Model Training**: Trains machine learning models (e.g., Logistic Regression, Random Forest, SVM) to predict student performance.
- **Model Monitoring**: Monitors the performance of the model after deployment, with tools to track accuracy and other metrics.
- **Prediction Pipeline**: Provides functionality to make predictions on new data based on the trained model.

---

## **Modeling**

This project explores multiple machine learning models to predict student performance:

- **Logistic Regression**
- **Random Forest Classifier**
- **Support Vector Machine (SVM)**

The models are evaluated using a **train-test split** (typically 80/20) and **cross-validation** techniques to ensure robust results. The best-performing model is selected for final predictions.

### **Model Training Pipeline**:
1. **Preprocessing**: Handle missing data, encode categorical features (e.g., one-hot encoding for gender), and scale numerical features (e.g., using StandardScaler).
2. **Model Evaluation**: Evaluate different models on the training data using cross-validation and metrics like accuracy, precision, and recall.
3. **Final Model**: Save the best-performing model in the `artifacts/` directory for later predictions.

<!-- Example usage of the model:

```python
from src.{project_name}.components.model_trainer import predict_performance

# Example input data (can be taken from user input or test data)
student_data = {
    'gender': 'female',
    'race_ethnicity': 'group A',
    'parental_level_of_education': 'some college',
    'lunch': 'standard',
    'test_preparation_course': 'completed',
    'math_score': 75,
    'reading_score': 80,
    'writing_score': 85
}

predicted_score = predict_performance(student_data)
print(f"Predicted Performance: {predicted_score}")
``` -->

---

## **Usage**

1. **Run the application**:
   - Open the terminal and run the `app.py` script to interact with the trained model.
   - The app will load the trained model and accept inputs like gender, test scores, etc., to predict student performance.

2. **Input Data**:
   - Provide input in the form of a dictionary with features such as `gender`, `math_score`, `reading_score`, etc.
   - The model will output a predicted performance score.

3. **Predictions**:
   - The model predicts student performance based on various features, which can help in identifying students at risk of underperforming.

---

## **Contributing**

We welcome contributions! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Clone your fork to your local machine.
3. Create a new branch for your feature or bugfix.
4. Make your changes and test them locally.
5. Push your changes to your fork.
6. Open a pull request with a clear description of your changes.

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## **Acknowledgments**

- **Dataset**: The data used for this project can be sourced from [Kaggle](https://www.kaggle.com/datasets) or similar datasets related to student performance.
- **Libraries Used**: 
    - **Scikit-learn** for model building and evaluation.
    - **Pandas** and **NumPy** for data processing.
    - **Matplotlib** and **Seaborn** for visualizations.