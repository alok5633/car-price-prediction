# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 17:13:53 2020

@author: Alok
"""

import pandas as pd
import numpy as np
import seaborn as sns

sns.set(rc={'figure.figsize':(11.7,8.27)})

cars_data=pd.read_csv('cars_sampled.csv')
#print(cars_data)
cars=cars_data.copy()

cars.info()

#cars.describe()
pd.set_option('display.float_format',lambda x:'%.3f' %x)
cars.describe()

pd.set_option('display.max_columns',500)
cars.describe()

col=['name','dateCrawled','postalCode','lastSeen','dateCreated']
cars=cars.drop(columns=col,axis=1)

cars.drop_duplicates(keep="first",inplace=True)

cars.isnull().sum()

yearwise_count=cars['yearOfRegistration'].value_counts().sort_index()
sum(cars['yearOfRegistration'] > 2018)
sum(cars['yearOfRegistration'] < 1950)

sns.regplot(x="yearOfRegistration",y="price",scatter=True,fit_reg=False,data=cars)


price_count=cars['price'].value_counts().sort_index()
sns.distplot(cars['price'])
cars['price'].describe()
sns.boxplot(y=cars['price'])
sum(cars['price'] > 150000)
sum(cars['price'] < 100)

power_count=cars['powerPS'].value_counts().sort_index()
sns.distplot(cars['powerPS'])
cars['powerPS'].describe()
sns.boxplot(y=cars['powerPS'])
sns.regplot(x="powerPS",y="price",scatter=True,fit_reg=False,data=cars)
sum(cars['powerPS'] > 500)
sum(cars['powerPS'] < 10)






