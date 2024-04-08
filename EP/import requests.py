# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:32:10 2024

@author: mickael
"""

import requests

for i in range(11,26):
    URL = "https://www.math93.com/images/pdf/annales_bac/Bac_NSI/bac_NSI_2024/nsi-pratique-2024/24-NSI-%02d"%i+"-ex2.py"
    print("24-NSI-%02d"%i+".pdf")
    response = requests.get(URL)
    open("24-NSI-%02d"%i+"-ex2.py", "wb").write(response.content)
