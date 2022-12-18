#!/usr/bin/env python
# coding: utf-8

# In[3]:

import pandas as pd
import numpy as np
import networkx as nx
import numpy as np
import seaborn as sns
import datetime as dt
from lifetimes.plotting import *
from lifetimes.utils import *
#from lifetimes.estimation import *
import lifetimes
from lifetimes.plotting import plot_period_transactions
from lifetimes.utils import calibration_and_holdout_data
from lifetimes.plotting import plot_calibration_purchases_vs_holdout_purchases
from lifetimes import GammaGammaFitter
from lifetimes import BetaGeoFitter
from lifetimes.plotting import plot_frequency_recency_matrix
import matplotlib.pyplot as plt
from lifetimes.plotting import plot_probability_alive_matrix



class clv():
  
    def __init__(self,CustomerID='CustomerID',InvoiceDate='InvoiceDate'):

        self.customerid = CustomerID
        self.invoicedate = InvoiceDate
        self.input_df = input_df
        self.quantity= Quantity
        self.unitprice = UnitPrice
        self.sales = self.quantity*self.unitprice
        self.analyze()
        

        
    def ploting(self):
        data = summary_data_from_transaction_data(df, self.customerid, self.invoicedate, monetary_value_col='Sales', observation_period_end='2011-12-9')
        data['frequency'].plot(kind='hist', bins=40)

        return sum(data['frequency'] == 0)/float(len(data))
    
    
    def betageofitter(self):
        data = summary_data_from_transaction_data(df, self.customerid, self.invoicedate, monetary_value_col='Sales', observation_period_end='2011-12-9')
        betageofit = BetaGeoFitter(penalizer_coef=0.0)
        betageofit.fit(data['frequency'], data['recency'], data['T'])
        figure = plt.figure(figsize=(16,6))
        plot_frequency_recency_matrix(betageofit)
        figure = plt.figure(figsize=(16,6))
        data['Purchases_Predicted'] = betageofit.conditional_expected_number_of_purchases_up_to_time(1, data['frequency'], data['recency'], data['T'])
        plot_period_transactions(betageofit)
        summary_hold = calibration_and_holdout_data(df, 'CustomerID', 'InvoiceDate',
                                        calibration_period_end='2011-06-08',
                                        observation_period_end='2011-12-09' )
        betageofit.fit(summary_hold['frequency_cal'], summary_hold['recency_cal'], summary_hold['T_cal'])
        
        plot_calibration_purchases_vs_holdout_purchases(betageofit, summary_hold)
        
        return betageofit.predict(10, data.loc[12347]['frequency'], data.loc[12347]['recency'], data.loc[12347]['T'])


# In[ ]:




