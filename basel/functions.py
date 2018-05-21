import matplotlib
import matplotlib.pyplot as plt
from matplotlib.dates import MONDAY
from matplotlib.dates import MonthLocator, WeekdayLocator, DateFormatter
import pandas as pd
import numpy as np
import seaborn as sns
def initial_time_series(df, df2):
    fig = plt.figure(figsize=(14,7))
    ax_one = plt.subplot2grid((2,14), (0,0), colspan=11, rowspan=2)
    ax_two = plt.subplot2grid((2,13), (0,11), colspan=2, rowspan=2)

    x_two = df.date.values
    x_two = pd.to_datetime(x_two)
    y_two = df.density
    y_three = df.pop_dens


    x_one = df2.date.values
    x_one = pd.to_datetime(x_one)
    y_one = df2.density
    y_four = df2.pop_dens.values



    monday = WeekdayLocator(MONDAY)
    months = MonthLocator(interval=3, bymonthday=1)

    monthsFmt = DateFormatter("%b '%y")
    ax_one.scatter(x_two, y_two, s= np.sqrt(y_three), color='b', label='SLR', alpha=0.5)
    ax_one.scatter(x_one, y_one, s= np.sqrt(y_four), color='black', label='hammerdirt', alpha=0.5)
    ax_one.xaxis.set_major_locator(months)
    ax_one.xaxis.set_major_formatter(monthsFmt)
    ax_one.xaxis.set_minor_locator(monday)
    ax_one.set_title('Litter inventories: hammerdirt - SLR 2015-2018', fontsize=18, color='b')
    ax_one.set_ylabel('Pcs/meter of shoreline', fontsize=16, color='b')
    ax_one.legend(loc='upper right')

    y_five = list(df.pop_dens.unique())
    y_six = list(df2.pop_dens.unique())

    y_pop = [y_five, y_six]
    def make_list(b):
        a = []
        for c in b:
            for e in c:
                a.append(e)
        a.sort()
        return a
    y_fourx = make_list(y_pop)

    def x_axis(y,x):
        b=[]
        for i in y:
            a = x
            b.append(a)
        return b
    x_four = x_axis(y_five, 1)
    x_five = x_axis(y_six, 2)


    ax_two.scatter(x_four, y_five, s=np.sqrt(y_five),color='b', alpha=1 )
    ax_two.scatter(x_five, y_six, s=np.sqrt(y_six),color='black', alpha=1 )
    ax_two.set_title('Population density', color='b')
    ax_two.set_xlim(0, 2.5)
    ax_two.set_xticks([1,2])
    ax_two.set_xticklabels(['1', '2'])
    plt.show()

def initial_scatter(df1, df2, df3):
    fig = plt.figure(figsize=(14,7))
    ax_one = plt.subplot2grid((2,14), (0,0), colspan=11, rowspan=2)
    ax_two = plt.subplot2grid((2,13), (0,11), colspan=2, rowspan=2)

    x_one = df1.date.values

    x_one = pd.to_datetime(x_one)
    y_one = np.log(df1.density)
    r_one = df1.pop_dens.values

    x_two = df2.date.values
    x_two = pd.to_datetime(x_two)
    y_two = np.log(df2.density)
    r_two = df2.pop_dens.values

    x_three = df3.date.values
    x_three = pd.to_datetime(x_three)
    y_three = np.log(df3.density)
    r_three = df3.pop_dens.values

    y_min = y_one.min()
    y_max = y_one.max()
    ymin = np.exp(y_one.min()).round(2)
    y25 = np.exp(np.percentile(y_one, 25)).round(2)
    y50 = np.exp(np.percentile(y_one, 50)).round(2)
    y75 = np.exp(np.percentile(y_one, 75)).round(2)
    ymax = np.exp(y_one.max()).round(2)

    monday = WeekdayLocator(MONDAY)
    months = MonthLocator(interval=3, bymonthday=1)
    monthsFmt = DateFormatter("%b '%y")

    ax_one.scatter(x_two, y_two, s= np.sqrt(r_two), color='r', label = 'River - SLR', alpha=0.5)
    ax_one.scatter(x_one, y_one, s=np.sqrt(r_one), color='b', label='Lake - SLR', alpha=0.5)
    ax_one.scatter(x_three, y_three, s=np.sqrt(r_three), color='black', label='Lake hammerdirt', alpha=0.5)

    ax_one.xaxis.set_major_locator(months)
    ax_one.xaxis.set_major_formatter(monthsFmt)
    ax_one.xaxis.set_minor_locator(monday)
    ax_one.set_ylim(y_min-.15, y_max+1)
    ax_one.set_yticklabels([str(ymin), str(y25), str(y50), str(y75), str(ymax)])
    ax_one.set_yticks([y_min, np.percentile(y_one, 25), np.percentile(y_one, 50), np.percentile(y_one, 75), y_max])
    ax_one.legend(loc='upper right')
    ax_one.set_title('Litter inventories 2015-2018: hammerdirt & SLR', fontsize=18, color='b')
    ax_one.set_ylabel('Pcs/meter of shoreline: log scale', fontsize=16, color='b')
    y_four = df1.pop_dens.unique()
    y_five = df2.pop_dens.unique()
    y_six = df3.pop_dens.unique()

    def x_axis(y,x):
        b=[]
        for i in y:
            a = x
            b.append(a)
        return b
    x_four = x_axis(y_four, 1)
    x_five = x_axis(y_five, 2)
    x_six = x_axis(y_six, 3)

    ax_two.scatter(x_four, y_four, s=np.sqrt(y_four*1.5),color='r', alpha=0.5 )
    ax_two.scatter(x_five, y_five, s=np.sqrt(y_five*1.5), color='b', alpha=0.5 )
    ax_two.scatter(x_six, y_six, s=np.sqrt(y_six*1.5), color='black', alpha=1)
    ax_two.set_ylim(min(y_five), max(y_six)+500)
    ax_two.set_title('Population density', color='b')
    ax_two.set_xlim(0, 3.5)
    ax_two.set_xticks([1,2,3])
    ax_two.set_xticklabels(['1', '2','3'])
    plt.show()


def lem_zur(df1, df2, df3):
    fig = plt.figure(figsize=(14,7))
    ax_one = plt.subplot2grid((2,14), (0,0), colspan=11, rowspan=2)
    ax_two = plt.subplot2grid((2,13), (0,11), colspan=2, rowspan=2)

    x_one = df1.date.values
    x_one = pd.to_datetime(x_one)
    y_one = np.log(df1.density)
    r_one = df1.pop_dens.values

    x_two = df2.date.values
    x_two = pd.to_datetime(x_two)
    y_two = np.log(df2.density)
    r_two = df2.pop_dens.values


    x_three = df3.date.values
    x_three = pd.to_datetime(x_three)
    y_three = np.log(df3.density)
    r_three = df3.pop_dens.values

    y_min = y_one.min()
    y_max = y_three.max()
    ymin = np.exp(y_one.min()).round(2)
    y25 = np.exp(np.percentile(y_one, 25)).round(2)
    y50 = np.exp(np.percentile(y_one, 50)).round(2)
    y75 = np.exp(np.percentile(y_one, 75)).round(2)
    ymax = np.exp(y_three.max()).round(2)



    monday = WeekdayLocator(MONDAY)
    months = MonthLocator(interval=3, bymonthday=1)
    monthsFmt = DateFormatter("%b '%y")
    #plt.subplot(1, 2, 1)
    ax_one.scatter(x_one, y_one, s= np.sqrt(r_one*1.5), color='b', label='Zürichsee - Swiss Litter Report', alpha=0.5)
    ax_one.scatter(x_two, y_two, s=np.sqrt(r_two*1.5), color='black', label='Lac Léman - Swiss Litter Report', alpha=0.5)
    ax_one.scatter(x_three, y_three, s=np.sqrt(r_three*1.5), color='black', label='Lac Léman - hammerdirt', alpha=0.7)

    ax_one.xaxis.set_major_locator(months)
    ax_one.xaxis.set_major_formatter(monthsFmt)
    ax_one.xaxis.set_minor_locator(monday)

    ax_one.set_ylim(y_min-.15, y_max+1)
    ax_one.set_yticklabels([str(ymin), str(y25), str(y50), str(y75), str(ymax)])
    ax_one.set_yticks([y_min, np.percentile(y_one, 25), np.percentile(y_one, 50), np.percentile(y_one, 75), y_max])
    ax_one.set_title('Litter inventories: Lac Léman-Zürichsee, 2015-2018', fontsize=20, color='b')
    ax_one.set_ylabel('Pcs/meter of shoreline: log scale', fontsize=16, color='b')
    ax_one.legend(loc='upper right')

    y_four = df1.pop_dens.unique()
    y_five = df2.pop_dens.unique()
    y_six = df3.pop_dens.unique()

    def x_axis(y,x):
        b=[]
        for i in y:
            a = x
            b.append(a)
        return b
    x_four = x_axis(y_four, 1)
    x_five = x_axis(y_five, 2)
    x_six = x_axis(y_six, 3)

    ax_two.scatter(x_four, y_four, s=np.sqrt(y_four*1.5),color='b', alpha=0.5 )
    ax_two.scatter(x_five, y_five, s=np.sqrt(y_five*1.5), color='black', alpha=0.5 )
    ax_two.scatter(x_six, y_six, s=np.sqrt(y_six*1.5), color='black', alpha=1)
    ax_two.set_title('Population density', color='b')


    ax_two.set_xlim(0, 3.5)
    ax_two.set_xticks([1,2,3])
    ax_two.set_xticklabels(['1', '2','3'])
    #plt.ylabel('Pcs/meter of shorelin: log scale', fontsize=20)
    plt.show()

import seaborn as sns
def dists(df1, df2, df3, family):
    plt.figure(figsize=(12,8))


    x_one = df1
    x_two = df2
    x_three = df3
    a = str(len(x_one))
    b = str(len(x_two))
    c = str(len(x_three))
    x_one_l = 'Lac Léman: 2015-2016, n= ' + a
    x_two_l = 'Lac Léman: 2017-2018, n= ' + b
    x_three_l = 'Zürichsee: 2017-2018, n= ' + c

    sns.distplot(x_one, hist=False, kde=True, label= x_one_l, kde_kws = {'linewidth': 4})
    sns.distplot(x_two, hist=False, kde=True, label= x_two_l,kde_kws = {'linewidth': 4})
    sns.distplot(x_three, hist=False, kde=True, label= x_three_l,kde_kws = {'linewidth': 4} )

    plt.xlim(-6, max(x_two)+1)
    locs, labels = plt.xticks()
    labes = []
    for s in locs:
        a = np.exp(s).round(2)
        a = str(a)
        labes.append(a)
    plt.xticks(locs, labes)
    plt.title('Probability density: '+ family + ' Lac Léman & Zürichsee', fontsize=20, color='b')
    plt.xlabel('Pieces per meter of shoreline', fontsize=16, color='b')
    plt.ylabel('Probability density', fontsize=16, color='b')

    plt.legend(fontsize=14)
    plt.show()

def pop_scatter(df1):
    fig = plt.figure(figsize=(10,7))
    ax_one = plt.subplot2grid((2,14), (0,0), colspan=11, rowspan=2)
    ax_two = plt.subplot2grid((2,13), (0,11), colspan=2, rowspan=2)

    x_one = df1.date.values

    x_one = pd.to_datetime(x_one)
    y_one = np.log(df1.density)
    r_one = df1.pop_dens.values

    x_two = df1.date.values
    x_two = pd.to_datetime(x_two)
    y_two = np.log(df1.density)
    r_two = df1.cor_pop.astype('float64')

#     x_three = df3.date.values
#     x_three = pd.to_datetime(x_three)
#     y_three = np.log(df3.density)
#     r_three = df3.pop_dens.values

    y_min = y_one.min()
    y_max = y_one.max()
    ymin = np.exp(y_one.min()).round(2)
    y25 = np.exp(np.percentile(y_one, 25)).round(2)
    y50 = np.exp(np.percentile(y_one, 50)).round(2)
    y75 = np.exp(np.percentile(y_one, 75)).round(2)
    ymax = np.exp(y_one.max()).round(2)

    monday = WeekdayLocator(MONDAY)
    months = MonthLocator(interval=3, bymonthday=1)
    monthsFmt = DateFormatter("%b '%y")

    ax_one.scatter(x_two, y_two, s= r_two/8, color='black', label = 'Effective density', alpha=0.5)
    ax_one.scatter(x_one, y_one, s=r_one/8, color='b', label='Density', alpha=1)
    #ax_one.scatter(x_three, y_three, s=np.sqrt(r_three), color='black', label='Lake hammerdirt', alpha=0.5)

    ax_one.xaxis.set_major_locator(months)
    ax_one.xaxis.set_major_formatter(monthsFmt)
    ax_one.xaxis.set_minor_locator(monday)
    ax_one.set_ylim(y_min-.15, y_max+1)
    ax_one.set_yticklabels([str(ymin), str(y25), str(y50), str(y75), str(ymax)])
    ax_one.set_yticks([y_min, np.percentile(y_one, 25), np.percentile(y_one, 50), np.percentile(y_one, 75), y_max])
    ax_one.legend(loc='upper right')
    ax_one.set_title('Effective pop density 2015-2016: Montreux', fontsize=14, color='b')
    ax_one.set_ylabel('Pcs/meter of shoreline: log scale', fontsize=16, color='b')
    y_four = df1.pop_dens.unique()
    y_five = df1.cor_pop.unique().astype('float64')
    #y_six = df3.pop_dens.unique()

    def x_axis(y,x):
        b=[]
        for i in y:
            a = x
            b.append(a)
        return b
    x_four = x_axis(y_four, 1)
    x_five = x_axis(y_five, 2)
    #x_six = x_axis(y_six, 3)

    ax_two.scatter(x_four, y_four, s=y_four/8,color='b', alpha=0.5 )
    ax_two.scatter(x_five, y_five, s=y_five/8, color='black', alpha=0.5 )
    #ax_two.scatter(x_six, y_six, s=np.sqrt(y_six*1.5), color='black', alpha=1)
    ax_two.set_ylim(min(y_four)-1000, max(y_five)+1500)
    ax_two.set_title('Population density', color='b')
    ax_two.set_xlim(0, 3.5)
    ax_two.set_xticks([1,2])
    ax_two.set_xticklabels(['1', '2'])
    plt.show()
