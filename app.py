from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        # Present_Price=float(request.form['Present_Price'])
        Kms_Driven=int(request.form['Kms_Driven'])
        Mileage = float(request.form['Mileage']) #in kmpl
        Engine = int(request.form['Engine'])
        Max_Power = float(request.form['Max_Power'])
        Owner=request.form['Owner']
        if(Owner=='2nd'):
            Second_Owner,Third_Owner=1,0
            # Second_Owner,Third_Owner,Fourth_Owner = 1,0,0
        elif(Owner=='3rd'):
           Second_Owner,Third_Owner=0,1
        #    Second_Owner,Third_Owner,Fourth_Owner = 0,1,0
        # elif(Owner=='4th+'):
        #     Second_Owner,Third_Owner,Fourth_Owner = 0,0,1
        else:
            # Second_Owner,Third_Owner,Fourth_Owner = 0,0,0
            Second_Owner,Third_Owner=0,0

        Seats=int(request.form['Seats'])
        Fuel_Type=request.form['Fuel_Type']
        if(Fuel_Type=='Petrol'):
                Fuel_Type_Petrol,Fuel_Type_Diesel,Fuel_Type_LPG=1,0,0
        elif(Fuel_Type=="Diesel"):
            Fuel_Type_Petrol,Fuel_Type_Diesel,Fuel_Type_LPG=0,1,0
        elif(Fuel_Type=="LPG"):
            Fuel_Type_Petrol,Fuel_Type_Diesel,Fuel_Type_LPG=0,0,1
        else:
            Fuel_Type_Petrol,Fuel_Type_Diesel,Fuel_Type_LPG=0,0,0

        Year=2020-Year #dataset prepared as of 2020
        Seller_Type=request.form['Seller_Type']
        if(Seller_Type=='Individual'):
            Seller_Type_Individual,Seller_Type_Trustmark_dealer=1,0
        elif(Seller_Type=='Trustmark_Dealer'): 
            Seller_Type_Individual,Seller_Type_Trustmark_dealer=0,1
        else:
            Seller_Type_Individual,Seller_Type_Trustmark_dealer=0,0




        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Manual'): Transmission_Mannual=1
        else: Transmission_Mannual=0


        #['km_driven', 'mileage', 'engine', 'max_power', 'seats', 'no_of_yrs','fuel_Diesel', 'fuel_LPG',\
        #fuel_Petrol', 'seller_type_Individual',
       #'seller_type_Trustmark Dealer', 'transmission_Manual',
       #'owner_Fourth & Above Owner', 'owner_Second Owner',
       #'owner_Third Owner'
        prediction=model.predict([[Kms_Driven,Mileage,Engine,Max_Power,Seats,Year,Fuel_Type_Diesel,Fuel_Type_LPG,Fuel_Type_Petrol,
        Seller_Type_Individual,Seller_Type_Trustmark_dealer,Transmission_Mannual,Third_Owner,Second_Owner]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True) 