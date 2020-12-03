#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Dataset_reading_and_manipulation:
    
    def reading_dataset(self):
        appsData = pd.read_excel("E:/PythonMiniProject_PlayStoreAppAnalysis/PlayStoreApps.xlsx")
        return appsData
    
    def data_manipulation(self):
        appsData['Price'] = appsData['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else str(x))
        appsData['Price'] = appsData['Price'].apply(lambda x: float(x))
        appsData['Installs'] = appsData['Installs'].apply(lambda x: str(x).replace('+', '') if '+' in str(x) else str(x))
        appsData['Installs'] = appsData['Installs'].apply(lambda x: str(x).replace(',', '') if ',' in str(x) else str(x))
        appsData['Installs'] = appsData['Installs'].apply(lambda x: float(x))
        appsData["LatestVersion"].fillna(str(appsData["LatestVersion"].mode().values[0]), inplace = True)
           
    def grouping_elements_by_category(self):
        category_elements = appsData.groupby('Category')
        return category_elements
    
    def set_of_category_of_apps(self):
        category_of_apps = set()
        for i in appsData.Category:
            category_of_apps.add(i)
        return category_of_apps
    
    def total_no_of_apps_in_each_category(self):
        no_of_apps_in_category = dict()
        for i in category_of_apps:
            no_of_apps_in_category[i] = len(appsData[appsData.Category == i])
        return no_of_apps_in_category

