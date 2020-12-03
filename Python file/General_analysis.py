#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class General_analysis:
    
    def statistics_of_numerical_columns(self):
        print(appsData.describe())
           
    def rating_boxplot(self):
        appsData.boxplot(column = ["Rating"])
        plt.show()
            
    def reviews_boxplot(self):
        appsData.boxplot(column = ["Reviews"])
        plt.show()
           
    def installs_boxplot(self):
        appsData.boxplot(column = ["Installs"])
        plt.show()
           
    def price_boxplot(self):
        appsData.boxplot(column = ["Price"]) 
        plt.show()
          
    def rating_histogram(self):
        appsData.hist(column = ["Rating"])
           
    def reviews_histogram(self):
        appsData.hist(column = ["Reviews"])
           
    def installs_histogram(self):
        appsData.hist(column = ["Installs"])
          
    def price_histogram(self):
        appsData.hist(column = ["Price"])

