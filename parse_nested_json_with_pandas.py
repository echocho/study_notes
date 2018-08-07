# Original post: https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas

import json 
import pandas as pd 
from pandas.io.json import json_normalize #package for flattening json in pandas df

#load json object
with open([path]) as f:
    data = json.load(f)

# put the data into a pandas df
# and let's pretend 'program' is a main key in the dict
daa_level1 = json_normalize(d['program'])
data_level1.head(3)

# let say, column works still cantains nested json and we want to
# 1. flatten all keys and values in works
# 2. keep other columns in data_level1
works_data = json_normalize(data=d['programs'], record_path='works', 
                            meta=['id', 'orchestra','programID', 'season'])
works_data.head(3)

# we can put more than one columns in json_normalize, very useful when we want to flatten more than one nested columns at one time
# again, soloists is anther column we want to flatten
soloist_data = json_normalize(data=d['programs'], record_path=['works', 'soloists'], meta=['id'])
soloist_data.head(3)
