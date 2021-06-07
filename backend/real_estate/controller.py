from real_estate.dataset import DataSet
from real_estate.housing import Housing

class Controller(object):

    dataset = DataSet()
    housing = Housing()

    def modeling(self,data):
        this = self.preprocess(data)
        return this

    def preprocess(self, data):
        housing = self.housing
        this = self.dataset
        this.housing = housing.new_model(data)
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*' * 100)
        print(f'1. data 의 type \n {type(this.housing)} ')
        print(f'2. data 의 column \n {this.housing.columns} ')
        print(f'3. data 의 상위 1개 행\n {this.housing.head(1)} ')
        print(f'4. data 의 null 의 갯수\n {this.housing.isnull().sum()} ')
        print('*' * 100)

if __name__ == '__main__':
    controller = Controller()
    controller.modeling('housing')
