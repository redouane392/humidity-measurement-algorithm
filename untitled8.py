# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:27:35 2020

@author: Redouane
"""

import json
import numpy as np
[(0,   15), 'saturated',  'red'],
[(15,  30), 'too wet', 'orange'],
[(30,  60), 'perfect',	'green'],
[(60, 100), 'plan to water', 'yellow'],
[(100, 200), 'dry', 'red']
]
def clean_data(dataframe):
	
	return dataframe.replace(200, np.nan)
f=open("data.txt","r")
json_data=json.load(f)[:-1]
humidity_dataframe = pd.DataFrame(
	data  = { data[i]['datasets']['label'] : data[i]['datasets']['data'] for i in range(len(data)) },
	index =	data[0]['labels']
    )


