import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore")

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv("/Users/samsonqian/Desktop/Health Hack.csv")

def main():
    data.rename(index=str, columns={"Hipertension": "Hypertension", "Handcap": "Handicap"}, inplace=True)
    data.drop(labels=["PatientId", "AppointmentID"], axis=1, inplace=True)
    encoding()
    scaling()
    data.drop(labels=["ScheduledDay", "AppointmentDay"], axis=1, inplace=True)

def encoding():
    le_gender = LabelEncoder()
    le_gender.fit(data["Gender"])
    encoded_gender = le_gender.transform(data["Gender"])
    data["Gender"] = encoded_gender

    le_noshow = LabelEncoder()
    le_noshow.fit(data["No-show"])
    encoded_noshow = le_noshow.transform(data["No-show"])
    data["No-show"] = encoded_noshow

    le_neighbourhood = LabelEncoder()
    le_neighbourhood.fit(data["Neighbourhood"])
    encoded_neighbourhood = le_neighbourhood.transform(data["Neighbourhood"])
    data["Neighbourhood"] = encoded_neighbourhood

def scaling():
    scaler = MinMaxScaler()

    age = np.array(data["Age"]).reshape(-1, 1)
    neighbourhood = np.array(data["Neighbourhood"]).reshape(-1, 1)

    data["Age"] = scaler.fit_transform(age)
    data["Neighbourhood"] = scaler.fit_transform(neighbourhood)


main()
