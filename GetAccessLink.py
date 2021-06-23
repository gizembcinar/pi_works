import re 
a= ['<url>https://xcd32112.smart_meter.com</url>' ,
    '<url>https://tXh67.dia_meter.com</url>',
    '<url>https://yT5495.smart_meter.com</url>',
    '<url>https://ret323_TRu.crown.com</url>',
    '<url>https://luwr3243.celsius.com</url>' ]

for i in a:
    o = re.findall('://([\w\.]+)<', i)
    print(o)
