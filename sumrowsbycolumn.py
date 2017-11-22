def render(table, params):
    groupby = params['groupby']
    sumcolumn = params['sumcolumn']

    if sumcolumn == '':
        return table
    elif groupby != '':
        return table
    else:
        if table[sumcolumn].dtype != np.float64 and table[sumcolumn].dtype != np.int64:
            table[sumcolumn] = table[sumcolumn].str.replace(',', '')
            table[sumcolumn] = table[sumcolumn].astype(float)
        if groupby == '':
            newtab = table[[sumcolumn]].sum().to_frame()
            newtab.columns = [sumcolumn + '_sum']
        else:
            newtab = table.groupby([groupby])[[sumcolumn]].sum()
            newtab = newtab.add_suffix('_sum').reset_index()
        return newtab
