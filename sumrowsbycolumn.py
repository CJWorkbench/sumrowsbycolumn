import numpy as np

class Importable:
    @staticmethod
    def __init__(self):
        pass

    @staticmethod
    def event():
        pass

    @staticmethod
    def render(wf_module, table):
        groupby = wf_module.get_param_column('groupby')
        sumcolumn = wf_module.get_param_column('sumcolumn')

        if sumcolumn == '':
            wf_module.set_ready(notify=False)
            return table
        elif groupby not in table.columns and groupby != '':
            wf_module.set_error('Invalid column to group row.')
            return table
        elif sumcolumn not in table.columns:
            wf_module.set_error('Invalid column for sum.')
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
            wf_module.set_ready(notify=False)
            return newtab