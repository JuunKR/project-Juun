from real_estate.controller import Controller

if __name__ == '__main__':
    controller = Controller()
    while 1:
        menu = input('0.exit\n1.new model\n2.DF생성\n')

        if menu == '0':
            break
        elif menu == '1':
            controller.modeling('data.xlsx')