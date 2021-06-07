import pandas as pd

from real_estate.dataset import DataSet


class Housing(object):
    dataset = DataSet()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = './data/'
        this.fname = payload
        return pd.read_excel(this.context + this.fname, sheet_name='전세종합')



