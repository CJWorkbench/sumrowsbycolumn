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
        groupby = wf_module.get_param_string('groupby')
        sumcolumn = wf_module.get_param_string('sumcolumn')

        if groupby == '' or sumcolumn == '':
            return table
        elif groupby not in table.columns:
            wf_module.set_error('Invalid group by column.')
            return table
        elif sumcolumn not in table.columns:
            wf_module.set_error('Invalid column for sum.')
            return table
        else:
            if table[sumcolumn].dtype != np.float64 and table[sumcolumn].dtype != np.int64:
                table[sumcolumn] = table[sumcolumn].str.replace(',', '')
                table[sumcolumn] = table[sumcolumn].astype(float)
            newtab = table.groupby([groupby])[[sumcolumn]].sum()
            wf_module.set_ready(notify=False)
            return newtab