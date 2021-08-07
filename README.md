
# Used Car Price Prediction

Used XGBoost algorithm to predict the selling price of an used car based on relevant features like mileage, no. of seats, no. of years used, etc.
 
# Tools Used
## Python libraries
* pandas - Data Cleaning and Pre-processing
* numpy - Performing mathematical operations on data
* sklearn - Implementing machine learning algorithms
* matplotlib - Data visualization
* Flask - Hosting the project locally
## Other Tools
+ Jupyter Notebook - Code Editor
+ Heroku - Deploying the project on the web





## Run Locally

Clone the project

```bash
  git clone https://github.com/Vishodhan/Used-Car-Price-Prediction.git
```

Go to the project directory

```bash
  cd Used-Car-Price-Prediction
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the project locally

```bash
  python app.py
```

  
## Deployment

This project is deployed on Heroku.

https://usedcarpricepredictionapp.herokuapp.com

  
## Optimizations

The project has been implemented using Random Forest and XGBoost algorithm. The latter gave a better accuracy. The performance of the model can be improved by tuning the algorithm's parameters.

| Model         | Accuracy on Test Dataset |
|---------------|--------------------------|
| Random Forest | 0.8705        |
| XGBoost       | 0.8780        |

  