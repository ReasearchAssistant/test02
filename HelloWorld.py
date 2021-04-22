# -*- coding:utf-8 -*-

import os
import pandas as pd


path = r'D:\office_heating.csv'

def method_name():
    df =pd.read_csv(path)
    return df


df = method_name()