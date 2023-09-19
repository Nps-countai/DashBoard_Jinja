import json
import pandas as pd
import firebase_admin
from firebase_admin import db, credentials
import json
from datetime import datetime
from pandas import json_normalize

def updatedData():
    
    cred = credentials.Certificate("credential.json")
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred, {
            "databaseURL": "https://coneui-default-rtdb.asia-southeast1.firebasedatabase.app/"
        })

    ref = db.reference("/")
    fbData = ref.get()

    uv_df = pd.DataFrame(columns=[])
    conetip_df = pd.DataFrame(columns=[])
    mill_list = []
    final_df = pd.DataFrame(columns=['millName', 'totalCount','totaluvCount' ,'totalconetipCount' ,'total_uv_Defect', 'total_uv_Nondefect', 'total_conetip_Nondefect', 'total_conetip_Defect', 'lastDay_uv_Defect', 'lastDay_uv_Nondefect', 'lastDay_conetip_Nondefect', 'lastDay_conetip_Defect', 'lastuv_inspectionOn', 'lastconetip_inspectionOn','firstInspectionOn', 'lastDay_totaluvCount', 'lastDay_totalconetipCount', 'lastDay_totalCount'])

    for i in fbData:
        mill_list.append(i)
        temp_conetip = pd.json_normalize(fbData[i]["conetip"] )
        temp_conetip['millName'] = i
        temp_uv = pd.json_normalize(fbData[i]["uv"])
        temp_uv['millName'] = i
        uv_df =uv_df._append(temp_uv)
        temp_conetip['detectedcone'] = temp_conetip.apply(lambda x : True if x['detectedconetype'] != x['selectedconetype'] else False, axis=1)
        conetip_df =conetip_df._append(temp_conetip)
        
        # final df
        millName = i
        total_uv_Defect = (len(temp_uv[(temp_uv['detecteduv'] == 'True') ]))
        total_uv_Nondefect = (len(temp_uv[(temp_uv['detecteduv'] == 'False') ]))
        total_conetip_Nondefect = len(temp_conetip[(temp_conetip['detectedcone'] == False) ])
        total_conetip_Defect = len(temp_conetip[(temp_conetip['detectedcone'] == True) ])
        lastDay_uv_Defect = len(temp_uv[(temp_uv['detecteduv'] == 'True') & (temp_uv['timestamp'] == max(temp_uv['timestamp']))])
        lastDay_uv_Nondefect = len(temp_uv[(temp_uv['detecteduv'] == 'False') & (temp_uv['timestamp'] == max(temp_uv['timestamp']))])
        lastDay_conetip_Nondefect = len(temp_conetip[(temp_conetip['detectedcone'] == False) & (temp_conetip['timestamp'] == max(temp_conetip['timestamp']))])
        lastDay_conetip_Defect = len(temp_conetip[(temp_conetip['detectedcone'] == True) & (temp_conetip['timestamp'] == max(temp_conetip['timestamp']))])
        lastuv_inspectionOn = max(temp_uv['timestamp'])
        lastconetip_inspectionOn = max(temp_conetip['timestamp'])
        firstInspectionOn = min(temp_uv['timestamp']) if min(temp_uv['timestamp']) <= min(temp_conetip['timestamp']) else min(temp_conetip['timestamp'])    
        totalCount = total_uv_Defect+total_uv_Nondefect + total_conetip_Nondefect + total_conetip_Defect
        totaluvCount = total_uv_Defect+total_uv_Nondefect 
        totalconetipCount = total_conetip_Nondefect + total_conetip_Defect
        lastDay_totaluvCount = lastDay_uv_Defect + lastDay_uv_Nondefect
        lastDay_totalconetipCount = lastDay_conetip_Nondefect + lastDay_conetip_Defect
        lastDay_totalCount = lastDay_totaluvCount + lastDay_totalconetipCount 
        data = [millName, totalCount,totaluvCount ,totalconetipCount , total_uv_Defect, total_uv_Nondefect, total_conetip_Nondefect, total_conetip_Defect, lastDay_uv_Defect, lastDay_uv_Nondefect, lastDay_conetip_Nondefect, lastDay_conetip_Defect, lastuv_inspectionOn, lastconetip_inspectionOn,firstInspectionOn, lastDay_totaluvCount, lastDay_totalconetipCount, lastDay_totalCount]
        # final_df =final_df._append(data)
        
        final_df.loc[len(final_df)] = data
        
        


    print(final_df.head(2))

    print(final_df.to_string())

    final_df.to_csv('new.csv')
    return final_df
