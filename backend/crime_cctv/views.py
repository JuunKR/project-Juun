from crime_cctv.services import Services
from crime_cctv.models import Models
from common.services import CommonService


class CrimeCctvApi(object):


    @staticmethod
    def main():
        common = CommonService()
        services = Services()


        while 1:
            menu = input('0. exit\n'
                         '1. modeling\n')
            if menu == '0':
                break

            elif menu == '1':

                result = services.new_model_for_xls('pop_in_seoul')

                # result2 = services.new_model_for_csv('cctv_in_seoul.csv')
                services.print_dframe(result)



            else:
                print('Wrong Number')

CrimeCctvApi.main()









