
import recipe_search
import recipe_search.database
import recipe_search.cluster
import recipe_search.search
import recipe_search.analyze

import MySQLdb

rs = recipe_search

db = rs.database.get_db("localhost","root","pwd4recDB","recipes_small")
cursor = rs.database.get_cursor(db)



ingred = 'mushrooms'
#ingred = 'carrots'
#ingred = 'chocolate'
#ingred = 'raisins'
#ingred = 'ears'
#ingred = 'couscous'

metric = 'jaccard'
inc=5
max_num_recipes = 15
num_trials = 2
data_dir = ("/Users/amorten/Projects/RecipeSearch/Database/"
            "/HClusters/")

rs.analyze.compare_cluster_vs_random(cursor,ingred,metric,
                          inc,max_num_recipes,num_trials,
                          data_dir)



