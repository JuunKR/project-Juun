import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
from crime.services import CrimeService


class Crime_API(object):

    @staticmethod
    def main():
        crimeService = CrimeService()
        while 1:
            menu = input('0. exit\n'
                         '1. pop_in_seoul\n'
                         '2. cctv_in_seoul\n'
                         '3. crime_in_seoul\n'
                         '4. police_position\n'
                         )
            if menu == '0':
                break
            elif menu == '1':
                crimeService.xls({'context':'./data/', 'fname':'pop_in_seoul'})
            elif menu == '2':
                crimeService.csv({'context':'./data/', 'fname':'cctv_in_seoul'})
            elif menu == '3':
                crimeService.csv({'context':'./data/', 'fname':'crime_in_seoul'})
            elif menu == '4':
                crimeService.csv({'context':'./data/', 'fname':'police_position'})


            else:
                continue

Crime_API.main()















