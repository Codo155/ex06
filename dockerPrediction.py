import uvicorn
from fastapi import FastAPI
import pandas as pd
from sklearn import tree

app = FastAPI()

clf = tree.DecisionTreeClassifier()
data = pd.read_csv("diabetes.csv")
features = data.iloc[:, :-1]
target = data["Outcome"]
clf = clf.fit(features, target)


@app.get("/calculate/")
def root(Pregnancies: int = 6, Glucose: int = 148, BloodPressure: int = 72, SkinThickness: int = 35, Insulin: int = 0,
         BMI: float = 33.6, DiabetesPedigreeFunction: float = 0.627, Age: int = 50):
    x = clf.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])[0]
    if(x==1):
        return ["Congrats, you have Diabetes"]
    elif(x!=1):
        return ["We do not think you have Diabetes"]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
