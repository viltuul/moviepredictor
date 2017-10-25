#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import pandas as pd
import ast
from collections import Counter

# read file
#df = pd.read_csv('Sylvester Stallone_main_business_vote details_keywords_taglines_trivia_release dates.csv', index_col = False)
df = pd.read_csv('raw_data/Ron Jeremy_main_business_vote details_keywords_taglines_trivia_release dates.csv', index_col = False) 

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

dfrat01 = df.loc[df['median'] == 1]
dfrat02 = df.loc[df['median'] == 2]
dfrat03 = df.loc[df['median'] == 3]
dfrat04 = df.loc[df['median'] == 4]
dfrat05 = df.loc[df['median'] == 5]
dfrat06 = df.loc[df['median'] == 6]
dfrat07 = df.loc[df['median'] == 7]
dfrat08 = df.loc[df['median'] == 8]
dfrat09 = df.loc[df['median'] == 9]
dfrat10 = df.loc[df['median'] == 10]

print len(dfrat07)

rat01 = dfrat01['keywords'].tolist()
rat02 = dfrat02['keywords'].tolist()
rat03 = dfrat03['keywords'].tolist()
rat04 = dfrat04['keywords'].tolist()
rat05 = dfrat05['keywords'].tolist()
rat06 = dfrat06['keywords'].tolist()
rat07 = dfrat07['keywords'].tolist()
rat08 = dfrat08['keywords'].tolist()
rat09 = dfrat09['keywords'].tolist()
rat10 = dfrat10['keywords'].tolist()

print rat07

if rat01:
    rat01 = rat01[0]
    srat01 = ' '.join(rat01)
    rat01mc10 = Counter(rat01).most_common(10)
if rat02:
    rat02 = rat02[0]
    rat02mc10 = Counter(rat02).most_common(10)
if rat03:
    rat03 = rat03[0]
    rat03mc10 = Counter(rat03).most_common(10)
if rat04:
    rat04 = rat04[0]
    rat04mc10 = Counter(rat04).most_common(10)
if rat05:
    rat05 = rat05[0]
    rat05mc10 = Counter(rat05).most_common(10)
if rat06:
    rat06 = rat06[0]
    rat06mc10 = Counter(rat06).most_common(10)
if rat07:
    rat07 = rat07[0]
    rat07mc10 = Counter(rat07).most_common(10)
if rat08:
    rat08 = rat08[0]
    rat08mc10 = Counter(rat08).most_common(10)
if rat09:
    rat09 = rat09[0]
    rat09mc10 = Counter(rat09).most_common(10)
if rat10:
    rat10 = rat10[0]
    rat10mc10 = Counter(rat10).most_common(10)
    
print len(rat01), len(rat02), len(rat03), len(rat04), len(rat05), len(rat06),len(rat07), len(rat08), len(rat09), len(rat10) 
print rat01mc10
print rat02mc10
print rat03mc10
print rat04mc10
print rat05mc10
print rat06mc10
print rat07mc10
print rat08mc10
print rat09mc10
#print rat10mc10

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