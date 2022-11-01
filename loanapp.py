from flask import Flask, render_template, request
import pickle
from csv import writer

app = Flask(__name__)

model = pickle.load(open('loaneligibility.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        
        
        ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Dependents',
       'Loan_Amount_Term', 'Credit_History', 
       
       'Male', 'Married_Yes',
       'Self_Employed_Yes', 'Not_Graduate', 'Semiurban', 'Urban']
        
        ApplicantIncome = float(request.form['ApplicantIncome'])
        
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        
        LoanAmount = float(request.form['LoanAmount'])
        
        Dependents = float(request.form['Dependents'])
        
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        
        Credit_History = float(request.form['Credit_History'])
        
        
        
        Gender = request.form['Gender']
        if (Gender == 'Male'):
            Male = 1
            
        else :
            Male = 0
            
            
            
        Married = request.form['Married']
        if (Married == 'Yes'):
            Married_Yes = 1
            
        else :
            Married_Yes = 0
            
            
            
        Self_Employed = request.form['Self_Employed']
        if (Self_Employed == 'Yes'):
            Self_Employed_Yes = 1
            
        else :
            Self_Employed_Yes = 0
            
            
            
        Education = request.form['Education']
        if (Education == 'No'):
            Not_Graduate = 1
            
        else :
            Not_Graduate = 0
            
            
            
        Property_Area = request.form['Property_Area']                
        if (Property_Area == 'Urban'):
            Area_yes=2
            
            
        elif (Property_Area == 'Semiurban'):
            Area_yes=1
            
        else:
            Area_yes=0
            
        prediction=model.predict([[ApplicantIncome, CoapplicantIncome, LoanAmount, Dependents, Loan_Amount_Term, Credit_History, Male, Married_Yes, Self_Employed_Yes, Not_Graduate, Area_yes]])
        output = prediction
        Loan_Status = 'Y'
        if prediction == 0: 
            Loan_Status = 'N'
        
        data = [Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area,Loan_Status]
        
        with open('train_u6lujuX_CVtuZ9i (1).csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            f_object.close()
        
        if output == 0:
            return render_template('index.html',prediction_text="The applicant is Not Eligible for Loan")
        elif output == 1:
            return render_template('index.html',prediction_text="The applicant is Eligible for Loan")
    else:
        return render_template('index.html')
            
        

if __name__=="__main__":
    app.run(debug=True)
