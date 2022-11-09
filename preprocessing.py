# binning

def qcut(col, base, df):
    qcut_list = pd.qcut(df[col], base, duplicates='drop').value_counts().index.categories.to_list()
    base_lis = []
    for i in range(len(qcut_list)):
        special = '(' + str(int(qcut_list[i].left)) + ',' + str(int(qcut_list[i].right)) + ']'
        base_lis.append(special)
    return base_lis

def spread(base_lis):
    base_lisa = []
    for i in range(len(base_lis)):
        j = float(base_lis[i].split(',')[0][1:])
        k = float(base_lis[i].split(',')[1][:-1])
        base_lisa.append(j)
        base_lisa.append(k)
    return base_lisa

def col_bin(len_cat, base_lisa, col, df):
    for i, l in zip(range(int(len(base_lisa)/2)), [i for i in range(0,len(base_lisa)-1, 2)]):
        df.loc[(base_lisa[l] < df[col]) & (df[col] <= base_lisa[l+1]), col+'_bin'] = i+1

    df.loc[(base_lisa[-1] <= df[col]), col+'_bin'] = len(base_lisa)/2
    df.loc[(base_lisa[0] >= df[col]), col+'_bin'] = 1 
    
def col_bin2(len_cat, base_lisa, col, df):
    for i, l in zip(range(int(len(base_lisa)/2)), [i for i in range(0,len(base_lisa)-1, 2)]):
        df.loc[(base_lisa[l] < df[col]) & (df[col] <= base_lisa[l+1]), col+'_bin2'] = i+1

    df.loc[(base_lisa[-1] <= df[col]), col+'_bin2'] = len(base_lisa)/2
    df.loc[(base_lisa[0] >= df[col]), col+'_bin2'] = 1 

def col_bin3(len_cat, base_lisa, col, df):
    for i, l in zip(range(int(len(base_lisa)/2)), [i for i in range(0,len(base_lisa)-1, 2)]):
        df.loc[(base_lisa[l] < df[col]) & (df[col] <= base_lisa[l+1]), col+'_bin3'] = i+1

    df.loc[(base_lisa[-1] <= df[col]), col+'_bin3'] = len(base_lisa)/2
    df.loc[(base_lisa[0] >= df[col]), col+'_bin3'] = 1 
