get_ipython().run_line_magic('run', 'Dataset_reading_and_manipulation.ipynb')
get_ipython().run_line_magic('run', 'General_analysis.ipynb')
get_ipython().run_line_magic('run', 'Mapping_data.ipynb')
get_ipython().run_line_magic('run', 'Visual_analysis.ipynb')
get_ipython().run_line_magic('run', 'Final_pts_calculation.ipynb')

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

drm = Dataset_reading_and_manipulation()
gnrl = General_analysis()
md = Mapping_data()
vsl = Visual_analysis()
pts = Final_pts_calculation()
    
appsData = drm.reading_dataset()
drm.data_manipulation()
category_elements = drm.grouping_elements_by_category()
category_of_apps = drm.set_of_category_of_apps()    
no_of_apps_in_category = drm.total_no_of_apps_in_each_category()

gnrl.statistics_of_numerical_columns()
gnrl.rating_boxplot()
gnrl.reviews_boxplot()
gnrl.installs_boxplot()
gnrl.price_boxplot()
gnrl.rating_histogram()
gnrl.reviews_histogram()
gnrl.installs_histogram()
gnrl.price_histogram()

rating_mean_for_each_category_dict = md.mean_rating_dict()
reviews_mean_for_each_category_dict = md.mean_reviews_dict()
installs_mean_for_each_category_dict = md.mean_downloads_dict()
price_mean_for_each_category_dict = md.mean_price_dict()
fullyRatedAppsInCategory_per = md.full_rated_apps_dict()
below_four_RatedAppsInCategory_per = md.apps_rated_below_four_dict()
more_than_one_million_reviews_in_category_per = md.more_than_1M_reviews_dict()
more_than_one_million_downloads_in_category_per = md.more_than_1M_downloads_dict()
no_of_free_apps_in_category_per = md.free_apps_dict()
no_of_paid_apps_in_category_per = md.paid_apps_dict()

vsl.display_mean_rating_for_each_category()
vsl.display_mean_review_for_each_category()
vsl.display_mean_downloads_for_each_category()
vsl.display_mean_price_for_each_category()
vsl.display_fully_rated_apps_in_each_category()
vsl.display_apps_rated_below_four_in_each_category()
vsl.display_more_than_1M_reviews_in_each_category()
vsl.display_more_than_1M_downloads_in_each_category()
vsl.display_free_apps_in_each_category()
vsl.display_paid_apps_in_each_category()

total_pts_for_each_category = pts.get_empty_dict()
total_pts_for_each_category = pts.get_final_pts()
vsl.display_total_pts_for_each_category()

