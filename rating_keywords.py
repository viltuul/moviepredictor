#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import pandas as pd
import ast

# read file
df = pd.read_csv('Sylvester Stallone_main_business_vote details_keywords_taglines_trivia_release dates.csv', index_col = False) 

# choose only needed columns
df = df.filter(['median','keywords'])

# drop rows containing NaN in any
df = df.dropna(axis=0,how='any')

# cast type from float to integer
df['median'] = df['median'].astype(int)

print df['keywords'].head(5)
# convert list of unicode keywords ot plain text keywords
keywords = df['keywords'].tolist()
ia = 0
for kwlist in keywords:
    kwlist = ast.literal_eval(kwlist)
    keywords[ia] = kwlist
    ia = ia + 1
    ib = 0
    for kw in kwlist:
        kw = kw.encode('utf-8')
        kwlist[ib] = kw
        ib = ib + 1
df['keywords'] = pd.Series(keywords, df.index.values)

print df['keywords'].head(5)

print df.head(5)

print len(df)

rat01 = df.loc[df['median'] == 1]
rat02 = df.loc[df['median'] == 2]
rat03 = df.loc[df['median'] == 3]
rat04 = df.loc[df['median'] == 4]
rat05 = df.loc[df['median'] == 5]
rat06 = df.loc[df['median'] == 6]
rat07 = df.loc[df['median'] == 7]
rat08 = df.loc[df['median'] == 8]
rat09 = df.loc[df['median'] == 9]
rat10 = df.loc[df['median'] == 10]

print len(rat01), len(rat02), len(rat03), len(rat04), len(rat05), len(rat06), len(rat07), len(rat08), len(rat08), len(rat09), len(rat10)


#print df.head(5)
#print len(keys)
#t = keys[1]
#print t
#print t[0]
#print type(t[0])
#t = ast.literal_eval(t)
#print t
#print t[0]
#print type(t[0])
#t[0] = t[0].encode('utf-8')
#print t[0]
#print type(t[0])
#print t