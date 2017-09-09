# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

########Airplane Crashes since 1908##########

####Import Librarys

import pandas as pd ##load data set and first look


####Load Data set
df = pd.read_csv("Data/AirplaneCrashes.csv")

#Overview
print(df.head(3))

#Which Colums are contained?
print(list(df.columns))


####Calculate Survivors Plane, People, Survivors total, total deaths
df['surv_plane']= df.Aboard - df.Fatalities

df['people'] = df.Aboard + df.Ground

df['surv_tot'] = df.people -df.Fatalities -df.Ground

df['death_tot'] = df.people - df.surv_tot	

###Checking some Values
print(df.loc[df['Aboard'] == 0])


