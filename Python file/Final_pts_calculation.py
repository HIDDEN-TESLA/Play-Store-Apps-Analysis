class Final_pts_calculation:
    
    def get_empty_dict(self):
        total_pts_for_each_category = {}
        for i in category_of_apps:
            total_pts_for_each_category[i] = 0
        return total_pts_for_each_category
    
    def get_pts_fully_rated():
        max_value = fullyRatedAppsInCategory_per[max(fullyRatedAppsInCategory_per.keys(), 
                                                     key=(lambda k: fullyRatedAppsInCategory_per[k]))]
        upper_cutoff = max_value*0.75
        lower_cutoff = max_value*0.25
        for i,j in sorted(fullyRatedAppsInCategory_per.items(), key=lambda x: x[1], reverse=True):
            if (j>= lower_cutoff and j<=upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 0
            elif (j>upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 1
            else:
                total_pts_for_each_category[i] = total_pts_for_each_category[i] - 1  
                            
    def get_pts_rated_below_four():
        max_value = below_four_RatedAppsInCategory_per[max(below_four_RatedAppsInCategory_per.keys(), 
                                                           key=(lambda k: below_four_RatedAppsInCategory_per[k]))]
        upper_cutoff = max_value*0.75
        lower_cutoff = max_value*0.25
        for i,j in sorted(below_four_RatedAppsInCategory_per.items(), key=lambda x: x[1], reverse=True):
            if (j>= lower_cutoff and j<=upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 0
            elif (j>upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] - 1
            else:
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 1
                            
    def get_pts_more_than_1M_downloads():
        max_value = more_than_one_million_downloads_in_category_per[max(
            more_than_one_million_downloads_in_category_per.keys(), 
            key=(lambda k: more_than_one_million_downloads_in_category_per[k]))]
        upper_cutoff = max_value*0.75
        lower_cutoff = max_value*0.25
        for i,j in sorted(more_than_one_million_downloads_in_category_per.items(), key=lambda x: x[1], reverse=True):
            if (j>= lower_cutoff and j<=upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 0
            elif (j>upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 1
            else:
                total_pts_for_each_category[i] = total_pts_for_each_category[i] - 1   
                          
    def get_pts_more_than_1M_reviews():
        max_value = more_than_one_million_reviews_in_category_per [max(
            more_than_one_million_reviews_in_category_per .keys(), 
            key=(lambda k: more_than_one_million_reviews_in_category_per [k]))]
        upper_cutoff = max_value*0.75
        lower_cutoff = max_value*0.25
        for i,j in sorted(more_than_one_million_reviews_in_category_per .items(), key=lambda x: x[1], reverse=True):
            if (j>= lower_cutoff and j<=upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 0
            elif (j>upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 1
            else:
                total_pts_for_each_category[i] = total_pts_for_each_category[i] - 1 
                         
    def get_pts_free_apps():
        max_value = no_of_free_apps_in_category_per [max(
            no_of_free_apps_in_category_per .keys(), 
            key=(lambda k: no_of_free_apps_in_category_per [k]))]
        upper_cutoff = max_value*0.75
        lower_cutoff = max_value*0.25
        for i,j in sorted(no_of_free_apps_in_category_per .items(), key=lambda x: x[1], reverse=True):
            if (j>= lower_cutoff and j<=upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 0
            elif (j>upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 1
            else:
                total_pts_for_each_category[i] = total_pts_for_each_category[i] - 1  
        
    def get_pts_paid_apps():
        max_value = no_of_paid_apps_in_category_per [max(
            no_of_paid_apps_in_category_per .keys(), 
            key=(lambda k: no_of_paid_apps_in_category_per [k]))]
        upper_cutoff = max_value*0.75
        lower_cutoff = max_value*0.25
        for i,j in sorted(no_of_paid_apps_in_category_per .items(), key=lambda x: x[1], reverse=True):
            if (j>= lower_cutoff and j<=upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 0
            elif (j>upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] - 1
            else:
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 1   
                
    def get_pts_mean_rating():
        max_value = rating_mean_for_each_category_dict [max(
            rating_mean_for_each_category_dict .keys(), 
            key=(lambda k: rating_mean_for_each_category_dict [k]))]
        upper_cutoff = max_value*0.75
        lower_cutoff = max_value*0.25
        for i,j in sorted(rating_mean_for_each_category_dict .items(), key=lambda x: x[1], reverse=True):
            if (j>= lower_cutoff and j<=upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 0
            elif (j>upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 1
            else:
                total_pts_for_each_category[i] = total_pts_for_each_category[i] - 1  
                 
    def get_pts_mean_reviews():
        max_value = reviews_mean_for_each_category_dict [max(
            reviews_mean_for_each_category_dict .keys(), 
            key=(lambda k: reviews_mean_for_each_category_dict [k]))]
        upper_cutoff = max_value*0.75
        lower_cutoff = max_value*0.25
        for i,j in sorted(reviews_mean_for_each_category_dict .items(), key=lambda x: x[1], reverse=True):
            if (j>= lower_cutoff and j<=upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 0
            elif (j>upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 1
            else:
                total_pts_for_each_category[i] = total_pts_for_each_category[i] - 1  
                
    def get_pts_mean_installs():
        max_value = installs_mean_for_each_category_dict [max(
            installs_mean_for_each_category_dict .keys(), 
            key=(lambda k: installs_mean_for_each_category_dict [k]))]
        upper_cutoff = max_value*0.75
        lower_cutoff = max_value*0.25
        for i,j in sorted(installs_mean_for_each_category_dict .items(), key=lambda x: x[1], reverse=True):
            if (j>= lower_cutoff and j<=upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 0
            elif (j>upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 1
            else:
                total_pts_for_each_category[i] = total_pts_for_each_category[i] - 1  
     
    def get_pts_mean_price():
        max_value = price_mean_for_each_category_dict [max(
            price_mean_for_each_category_dict .keys(), 
            key=(lambda k: price_mean_for_each_category_dict [k]))]
        upper_cutoff = max_value*0.75
        lower_cutoff = max_value*0.25
        for i,j in sorted(price_mean_for_each_category_dict .items(), key=lambda x: x[1], reverse=True):
            if (j>= lower_cutoff and j<=upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 0
            elif (j>upper_cutoff):
                total_pts_for_each_category[i] = total_pts_for_each_category[i] - 1
            else:
                total_pts_for_each_category[i] = total_pts_for_each_category[i] + 1  
                     
    def get_final_pts(self):
        Final_pts_calculation.get_pts_mean_rating()
        Final_pts_calculation.get_pts_mean_reviews()
        Final_pts_calculation.get_pts_mean_installs()
        Final_pts_calculation.get_pts_mean_price()
        Final_pts_calculation.get_pts_fully_rated()
        Final_pts_calculation.get_pts_rated_below_four()
        Final_pts_calculation.get_pts_more_than_1M_downloads()
        Final_pts_calculation.get_pts_more_than_1M_reviews()
        Final_pts_calculation.get_pts_free_apps()
        Final_pts_calculation.get_pts_paid_apps()
        return total_pts_for_each_category

