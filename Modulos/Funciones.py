import urllib.request, json
import pandas as pd
import csv

from pandas.io.feather_format import read_feather



def replace_all(Csv ,str ,text, remplace):
    for i in Csv[str]:
        Csv[str] = Csv[str].str.replace(text, remplace)
