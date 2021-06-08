class Country(object):
    name = 'Country Name'
    population = "Population"
    capital = 'Capital'

    def show(self):
        print('Country Class Method')




class Korea(Country):
    
    def show_name(self):
        print(f'Country Name : {self.name}')

def main():
    k = Korea()
    k.name = '대한민국'
    k.show_name()

main()

