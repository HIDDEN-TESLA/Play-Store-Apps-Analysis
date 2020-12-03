class Mapping_data:
    
    def mean_price_dict(self):
        price_mean_for_each_category = category_elements['Price'].agg(np.mean)
        price_mean_for_each_category_dict = dict(price_mean_for_each_category)
        return price_mean_for_each_category_dict
    
    def mean_downloads_dict(self):
        installs_mean_for_each_category = category_elements['Installs'].agg(np.mean)
        installs_mean_for_each_category_dict = dict(installs_mean_for_each_category)
        return installs_mean_for_each_category_dict
    
    def mean_reviews_dict(self):
        reviews_mean_for_each_category = category_elements['Reviews'].agg(np.mean)
        reviews_mean_for_each_category_dict = dict(reviews_mean_for_each_category)
        return reviews_mean_for_each_category_dict
    
    def mean_rating_dict(self):
        rating_mean_for_each_category = category_elements['Rating'].agg(np.mean)
        rating_mean_for_each_category_dict = dict(rating_mean_for_each_category)
        return rating_mean_for_each_category_dict
    
    def full_rated_apps_dict(self):
        fully_rated_rows = appsData[appsData.Rating==5]
        fullyRatedAppsInCategory = {}
        for i in fully_rated_rows.Category:
            if fullyRatedAppsInCategory.__contains__(i):
                fullyRatedAppsInCategory[i] = fullyRatedAppsInCategory[i] + 1;
            else:
                fullyRatedAppsInCategory[i] = 1;
        fullyRatedAppsInCategory_per = {}
        for i in fully_rated_rows.Category:
            fullyRatedAppsInCategory_per[i] = round(((fullyRatedAppsInCategory[i]
                                                      /no_of_apps_in_category[i])*100), 2)
        return fullyRatedAppsInCategory_per
    
    def apps_rated_below_four_dict(self):
        rating_below_four_in_rows = appsData[appsData.Rating<4]
        below_four_RatedAppsInCategory = {}
        for i in rating_below_four_in_rows.Category:
            if below_four_RatedAppsInCategory.__contains__(i):
                below_four_RatedAppsInCategory[i] = below_four_RatedAppsInCategory[i] + 1;
            else:
                below_four_RatedAppsInCategory[i] = 1;
        below_four_RatedAppsInCategory_per = {}
        for i in category_of_apps:
            below_four_RatedAppsInCategory_per[i] = round(((below_four_RatedAppsInCategory[i]
                                                            /no_of_apps_in_category[i])*100), 2)
        
        return below_four_RatedAppsInCategory_per

    def more_than_1M_reviews_dict(self):
        more_than_one_million_reviews = appsData[appsData.Reviews>=1000000]
        more_than_one_million_reviews_in_category = {}
        for i in more_than_one_million_reviews.Category:
            if more_than_one_million_reviews_in_category.__contains__(i):
                more_than_one_million_reviews_in_category[i] = more_than_one_million_reviews_in_category[i] + 1;
            else:
                more_than_one_million_reviews_in_category[i] = 1;
        more_than_one_million_reviews_in_category_per = {}
        for i in more_than_one_million_reviews_in_category:
            more_than_one_million_reviews_in_category_per[i] = round(((more_than_one_million_reviews_in_category[i]/
                                                                       no_of_apps_in_category[i])*100), 2)
        return more_than_one_million_reviews_in_category_per
    
    def more_than_1M_downloads_dict(self):
        more_than_one_million_downloads = appsData[appsData.Installs>=1000000]
        more_than_one_million_downloads_in_category = {}
        for i in more_than_one_million_downloads.Category:
            if more_than_one_million_downloads_in_category.__contains__(i):
                more_than_one_million_downloads_in_category[i] = more_than_one_million_downloads_in_category[i] + 1;
            else:
                more_than_one_million_downloads_in_category[i] = 1;
        more_than_one_million_downloads_in_category_per = {}
        for i in category_of_apps:
            more_than_one_million_downloads_in_category_per[i] = round(((more_than_one_million_downloads_in_category[i]
                                                                         /no_of_apps_in_category[i])*100), 2)
        return more_than_one_million_downloads_in_category_per
    
    def free_apps_dict(self):
        group_apps_by_category = {}
        for i in category_of_apps:
            group_apps_by_category[i] = appsData[appsData.Category == i]
        no_of_free_apps_in_category = {}
        free = 0
        for i in category_of_apps:
            free = 0
            for j in group_apps_by_category[i].Type:
                if j == "Free":
                    free+=1
            no_of_free_apps_in_category[i] = free
        no_of_free_apps_in_category_per = {}
        for i in no_of_free_apps_in_category:
            no_of_free_apps_in_category_per[i] = round(((no_of_free_apps_in_category[i]
                                                         /no_of_apps_in_category[i])*100), 2)  
        return no_of_free_apps_in_category_per
    
    def paid_apps_dict(self):
        group_apps_by_category = {}
        for i in category_of_apps:
            group_apps_by_category[i] = appsData[appsData.Category == i]
        no_of_paid_apps_in_category = {}
        paid = 0
        for i in category_of_apps:
            paid = 0
            for j in group_apps_by_category[i].Type:
                if j == "Paid":
                    paid+=1
            no_of_paid_apps_in_category[i] = paid  
        no_of_paid_apps_in_category_per = {}
        for i in no_of_paid_apps_in_category:
            no_of_paid_apps_in_category_per[i] = round(((no_of_paid_apps_in_category[i]
                                                         /no_of_apps_in_category[i])*100), 2)
        return no_of_paid_apps_in_category_per

