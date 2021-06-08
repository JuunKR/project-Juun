import pandas as pd
import xlwings as xw
from common.services import CommonService
from crime_cctv.models import Models


class Services(CommonService):
    models = Models()
    print = CommonService()

    def new_model_for_csv(self, payload) -> object:
        this = self.models
        this.context = './data/'
        this.fname = payload

        return pd.read_csv(this.context + this.fname)

    def new_model_for_xls(self, payload) -> object:
        this = self.models
        this.context = './data/'
        this.fname = payload
        df = pd.read_excel(this.context + payload + '.xls')
        # sheet = xw.Book(this.context + payload + ".xls")
        # row_num = sheet.range(1, 1).end('down').end('down').end('down').row
        # data_range = 'A2:GE' + str(row_num)
        # df = sheet[data_range].option(pd.DataFrame, index= False, header=True).value
        return df











