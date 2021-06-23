import re 
import pandas as pd

def find_url(obj):
    access_link = []
    for i in obj:
        access_link.append(re.findall('://([\w\.]+)<', i))
    return access_link


data = {'Device_Type' : ['AXO145','TRU151', 'ZOD231', 'YRT326' ,'LWR245'],
    'Stats_Access_Link' : ['<url>https://xcd32112.smart_meter.com</url>' ,
                           '<url>https://tXh67.dia_meter.com</url>', 
                           '<url>https://yT5495.smart_meter.com</url>',
                           '<url>https://ret323_TRu.crown.com</url>',
                           '<url>https://luwr3243.celsius.com</url>'] }

df = pd.DataFrame.from_dict(data)

print(find_url(df['Stats_Access_Link']))
