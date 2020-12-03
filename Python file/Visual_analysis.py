#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Visual_analysis:
    
    def display_mean_rating_for_each_category(self):
        category_list_for_rating = list(rating_mean_for_each_category_dict.keys()) 
        rating_mean_for_each_category_list = list(rating_mean_for_each_category_dict.values())   
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.bar(category_list_for_rating, rating_mean_for_each_category_list,color = 'blue',width = 0.5)
        ax.grid()
        ax.set_title("Category (vs) Mean Rating", fontsize = 14,fontweight="bold")
        ax.set_ylabel("Mean Rating", fontsize = 12, labelpad = 20,fontweight="bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20,fontweight="bold")
        ax.set_xticklabels(category_list_for_rating,rotation=90)
        ax.set_ylim([1,5])
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[1]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(3)
        y_grid_two = yGrids[5]
        y_grid_two.set_color('green')
        y_grid_two.set_linewidth(3)
          
    def display_mean_review_for_each_category(self):
        category_list_for_reviews = list(reviews_mean_for_each_category_dict.keys()) 
        reviews_mean_for_each_category_list = list(reviews_mean_for_each_category_dict.values())   
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.bar(category_list_for_reviews, reviews_mean_for_each_category_list,color = 'blue',width = 0.5)
        ax.grid()
        ax.set_title("Category (vs) Mean Reviews", fontsize = 14,fontweight="bold")
        ax.set_ylabel("Mean Reviews", fontsize = 12, labelpad = 20,fontweight="bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20,fontweight="bold")
        ax.set_xticklabels(category_list_for_reviews,rotation=90)
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[2]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(3)
        y_grid_two = yGrids[5]
        y_grid_two.set_color('green')
        y_grid_two.set_linewidth(3)
        
    def display_mean_downloads_for_each_category(self):
        category_list_for_installs = list(installs_mean_for_each_category_dict.keys()) 
        installs_mean_for_each_category_list = list(installs_mean_for_each_category_dict.values())   
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.bar(category_list_for_installs, installs_mean_for_each_category_list,color = 'blue',width = 0.5)
        ax.grid()
        ax.set_title("Category (vs) Mean Downloads", fontsize = 14,fontweight="bold")
        ax.set_ylabel("Mean Downloads", fontsize = 12, labelpad = 20,fontweight="bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20,fontweight="bold")
        ax.set_xticklabels(category_list_for_installs,rotation=90)
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[1]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(3)
        y_grid_two = yGrids[4]
        y_grid_two.set_color('green')
        y_grid_two.set_linewidth(3)
        
    def display_mean_price_for_each_category(self):
        category_list_for_price = list(price_mean_for_each_category_dict.keys()) 
        price_mean_for_each_category_list = list(price_mean_for_each_category_dict.values())   
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.bar(category_list_for_price, price_mean_for_each_category_list,color = 'blue',width = 0.5)
        ax.grid()
        ax.set_title("Category (vs) Mean Price ($)", fontsize = 14,fontweight="bold")
        ax.set_ylabel("Mean Price ($)", fontsize = 12, labelpad = 20,fontweight="bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20,fontweight="bold")
        ax.set_xticklabels(category_list_for_price,rotation=90)
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[6]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(3)
        y_grid_two = yGrids[2]
        y_grid_two.set_color('green')
        y_grid_two.set_linewidth(3)
             
    def display_fully_rated_apps_in_each_category(self):
        category_list_for_fully_rated_apps = list(fullyRatedAppsInCategory_per.keys()) 
        per_of_fully_rated_apps_list_in_category = list(fullyRatedAppsInCategory_per.values()) 
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.bar(category_list_for_fully_rated_apps, per_of_fully_rated_apps_list_in_category,color = 'blue',width = 0.5)
        ax.grid()
        ax.set_title("Category Vs % of fully rated Apps in each category", fontsize = 14, fontweight = "bold")
        ax.set_ylabel("Percentage", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xticklabels(category_list_for_fully_rated_apps,rotation=90)
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[1]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(3)
        y_grid_two = yGrids[5]
        y_grid_two.set_color('green')
        y_grid_two.set_linewidth(3)
        
    def display_apps_rated_below_four_in_each_category(self):
        category_list_for_apps_rated_below_4 = list(below_four_RatedAppsInCategory_per.keys()) 
        per_of_apps_rated_below_4_list_in_category = list(below_four_RatedAppsInCategory_per.values()) 
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.bar(category_list_for_apps_rated_below_4, 
               per_of_apps_rated_below_4_list_in_category,color = 'blue',width = 0.5)
        ax.grid()
        ax.set_title("Category Vs % of apps rated below four in each category", fontsize = 14, fontweight = "bold")
        ax.set_ylabel("Percentage", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xticklabels(category_list_for_apps_rated_below_4,rotation=90)
        ax.set_ylim([0,50])
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[3]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(3)
        y_grid_two = yGrids[1]
        y_grid_two.set_color('green')
        y_grid_two.set_linewidth(3)
        
    def display_more_than_1M_reviews_in_each_category(self):
        category_list_for_apps_more_than_1M_reviews = list(more_than_one_million_reviews_in_category_per.keys()) 
        per_of_apps_more_than_1M_reviews_list_in_category = list(more_than_one_million_reviews_in_category_per.values()) 
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.bar(category_list_for_apps_more_than_1M_reviews, 
               per_of_apps_more_than_1M_reviews_list_in_category,color = 'blue',width = 0.5)
        ax.grid()
        ax.set_title("Category Vs % of apps has more than 1M reviews in each category", 
                     fontsize = 14, fontweight = "bold")
        ax.set_ylabel("Percentage", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xticklabels(category_list_for_apps_more_than_1M_reviews,rotation=90)
        ax.set_ylim([0,10])
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[1]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(3)
        y_grid_two = yGrids[3]
        y_grid_two.set_color('green')
        y_grid_two.set_linewidth(3)
        
    def display_more_than_1M_downloads_in_each_category(self):
        category_list_for_apps_more_than_1M_downloads = list(more_than_one_million_downloads_in_category_per.keys()) 
        per_of_apps_more_than_1M_downloads_list_in_category = list(
            more_than_one_million_downloads_in_category_per.values()) 
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.bar(category_list_for_apps_more_than_1M_downloads, 
               per_of_apps_more_than_1M_downloads_list_in_category,color = 'blue',width = 0.5)
        ax.grid()
        ax.set_title("Category Vs % of apps has more than 1M downloads in each category", 
                     fontsize = 14, fontweight = "bold")
        ax.set_ylabel("Percentage", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xticklabels(category_list_for_apps_more_than_1M_downloads,rotation=90)
        ax.set_ylim([5,80])
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[2]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(3)
        y_grid_two = yGrids[6]
        y_grid_two.set_color('green')
        y_grid_two.set_linewidth(3)
        
    def display_free_apps_in_each_category(self):
        category_list_for_free_apps = list(no_of_free_apps_in_category_per.keys()) 
        per_of_free_apps_list_in_category = list(no_of_free_apps_in_category_per.values()) 
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.bar(category_list_for_free_apps, per_of_free_apps_list_in_category,color = 'blue',width = 0.5)
        ax.grid()
        ax.set_title("Category Vs % of Free Apps in each category", fontsize = 14, fontweight = "bold")
        ax.set_ylabel("Percentage", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xticklabels(category_list_for_free_apps,rotation=90)
        ax.set_ylim([25,100])
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[1]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(3)
        y_grid_two = yGrids[6]
        y_grid_two.set_color('green')
        y_grid_two.set_linewidth(3)
        
    def display_paid_apps_in_each_category(self):
        category_list_for_paid_apps = list(no_of_paid_apps_in_category_per.keys()) 
        per_of_paid_apps_list_in_category = list(no_of_paid_apps_in_category_per.values()) 
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.bar(category_list_for_paid_apps, per_of_paid_apps_list_in_category,color = 'blue',width = 0.5)
        ax.grid()
        ax.set_title("Category Vs % of Paid Apps in each category", fontsize = 14, fontweight = "bold")
        ax.set_ylabel("Percentage", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xticklabels(category_list_for_paid_apps,rotation=90)
        ax.set_ylim([0,35])
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[5]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(3)
        y_grid_two = yGrids[2]
        y_grid_two.set_color('green')
        y_grid_two.set_linewidth(3)
        
    def display_total_pts_for_each_category(self):
        category_list_all = list(total_pts_for_each_category.keys()) 
        pts_list_for_each_category = list(total_pts_for_each_category.values()) 
        fig, ax = plt.subplots(figsize=(15,5))
        fig = plt.figure()
        ax.plot(category_list_all, pts_list_for_each_category,color = 'green')
        ax.grid()
        ax.set_title("Category Vs Total points", fontsize = 14, fontweight = "bold")
        ax.set_ylabel("Points", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xlabel("Category of Apps", fontsize = 12, labelpad = 20, fontweight = "bold")
        ax.set_xticklabels(category_list_all,rotation=90)
        yGrids = ax.get_ygridlines()
        y_grid_one = yGrids[5]
        y_grid_one.set_color('red')
        y_grid_one.set_linewidth(2)

