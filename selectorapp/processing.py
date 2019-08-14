#pip install gspread oauth2client

import sys
sys.path.append('/home/varun331/.local/lib/python2.7/site-packages/')
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import json, ast
import numpy as ny
import pandas as pd
import random
from datetime import datetime,timedelta
import os

class receipe:
    """docstring for ClassName"""
    #def __init__(self, arg):
        #super(ClassName, self).__init__()
        #self.arg = arg
        


    def display_recepie(self):

        scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'creds.json')
        #creds = ServiceAccountCredentials.from_json_keyfile_name("/home/varun331/mysite/creds.json", scope)
        creds = ServiceAccountCredentials.from_json_keyfile_name(my_file, scope)
        client = gspread.authorize(creds)
        sheet = client.open("recipeselector").sheet1  # Open the spreadhseet
        raw = sheet.get_all_records()
        data1 = ast.literal_eval(json.dumps(raw))


        test = pd.DataFrame.from_dict(data1)
        test['Date'] =  pd.to_datetime(test['Date'])
        a =  test.copy()
        today=(datetime.today() - timedelta(days=14)).strftime('%m/%d/%Y')
        pa=0
        type1=a[(a.Type==1) &(a.Date<=today)]
        if pa == 1:
            type2=a[(a.Type==2) & (a.Date<=today)]
        else:
            type2=a[(a.Type==2)&(a.Date<=today)&(a.ing!='pa')]

        b = {}

        list1 = type1.index.values.tolist()
        list2 = type2.index.values.tolist()
        d = random.choice(list1)
        b.update(dict(zip(type1.loc[[d]].Dish,type1.loc[[d]].ing)))

        for i in range(len(type2)):
             if (len(b)<4):
                r = random.choice(list2)
                if type2.loc[[r]].ing.item() not in b.values():
                    b.update(dict(zip(type2.loc[[r]].Dish,type2.loc[[r]].ing)))
                    list2.remove(r)
        c = str(b)
        return (c)
        #print (c)
    #display_recepie()
    