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

cars = cars[
        (cars.yearOfRegistration<=2018)&
        (cars.yearOfRegistration>=1950)
        &(cars.price>=100)
        &(cars.price<=150000)
        &(cars.powerPS >= 10)
        &(cars.powerPS <= 500)
        ]

cars['monthOfRegistration']/=12

cars['Age']=(2018-cars['yearOfRegistration'])+cars['monthOfRegistration']
cars['Age']=round(cars['Age'],2)
cars['Age'].describe()

cars=cars.drop(columns=['yearOfRegistration','monthOfRegistration'],axis=1)

sns.distplot(cars['Age'])
sns.boxplot(y=cars['Age'])

sns.distplot(cars['price'])
sns.boxplot(y=cars['price'])

sns.distplot(cars['powerPS'])
sns.boxplot(y=cars['powerPS'])

sns.regplot(x='Age',y='price',scatter=True,fit_reg=False,data=cars)

sns.regplot(x='powerPS',y='price',scatter=True,fit_reg=False,data=cars)

cars['seller'].value_counts()
pd.crosstab(cars['seller'],columns='count',normalize=True)
sns.countplot(x='seller',data=cars)

cars['offerType'].value_counts()
sns.countplot(x='offerType',data=cars)

cars['abtest'].value_counts()
pd.crosstab(cars['abtest'],columns='count',normalize=True)
sns.countplot(x='abtest',data=cars)

sns.boxplot(x='abtest',y='price',data=cars)

cars['vehicleType'].value_counts()
pd.crosstab(cars['vehicleType'],columns='count',normalize=True)
sns.countplot(x='vehicleType',data=cars)
sns.boxplot(x='vehicleType',y='price',data=cars)

cars['gearbox'].value_counts()
pd.crosstab(cars['gearbox'],columns='count',normalize=True)
sns.countplot(x='gearbox',data=cars)
sns.boxplot(x='gearbox',y='price',data=cars)

cars['model'].value_counts()
pd.crosstab(cars['model'],columns='count',normalize=True)
sns.countplot(x='model',data=cars)
sns.boxplot(x='model',y='price',data=cars)

cars['kilometer'].value_counts()
pd.crosstab(cars['kilometer'],columns='count',normalize=True)
sns.boxplot(x='kilometer',y='price',data=cars)
cars['kilometer'].describe()

cars['fuelType'].value_counts()
pd.crosstab(cars['fuelType'],columns='count',normalize=True)
sns.countplot(x='fuelType',data=cars)
sns.boxplot(x='fuelType',y='price',data=cars)

cars['brand'].value_counts()
pd.crosstab(cars['brand'],columns='count',normalize=True)
sns.countplot(x='brand',data=cars)
sns.boxplot(x='brand',y='price',data=cars)

cars['notRepairedDamage'].value_counts()
pd.crosstab(cars['notRepairedDamage'],columns='count',normalize=True)
sns.countplot(x='notRepairedDamage',data=cars)
sns.boxplot(x='notRepairedDamage',y='price',data=cars)

col=['seller','offerType','abtest']
cgars=cars.drop(columns=col,axis=1)
cars_copy=cars.copy()

cars_select1=cars.select_dtypes(exclude=[object])
correlation=cars_select1.corr()
round(correlation,3)
cars_select1.corr().loc[:,'price'].abs().sort_values(ascending=False)[1:]