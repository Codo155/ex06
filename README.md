API using Fastapi for prediciting diabetes using several metrics. Details about metrics can be found on : 
https://www.kaggle.com/uciml/pima-indians-diabetes-database

Docker Image:

*https://hub.docker.com/r/codo155/ex05

Docker Run command:

*docker run -p 2000:5000 75d55db34932

NOTE: For "75d55db34932" insert your own image ID


Sample request:
	  
*http://localhost:5000/calculate/?Pregnancies=1&Glucose=85&BloodPressure=66&SkinThickness=29&Insulin=0&BMI=26.6&DiabetesPedigreeFunctio=0.351&Age=31