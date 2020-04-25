import random
playersmap=[]
for i in range(0,5):
        playersmap.append([])
        for j in range(0,5):
            playersmap[i].append('0') 
                                
def addship():    #добавляет корабли в массив для будущей обработки компьютера
        n =0
        while n<5:
                x = input('Введите первую числовую координату от 1 до 5 для вашего корабля')
                if coordinate1 >0 and coordinates1 <=5:
                        y = input('Введите вторую числовую координату от 1 до 5 для вашего корабля')
                        if coordinate2 >0 and coordinates <=5:
                            x=x-1 
                            y=y-1
                            if playersmap[y][x] == '0':
                                playersmap[y][x] = '1'
                            if y>0:
                                playersmap[y-1][x] = '2'
                            if x<4:
                                playersmap[y][x+1] = '2'
                            if x>0:
                                playersmap[y][x-1] = '2'
                            if y<4:
                                playersmap[y+1][x] = '2'
                        else:
                                print('Выбери еще раз')
                playerprint(playersmap)
        return(playersmap)


def fieldgenerator():              #генерирует рандомизирование поле компьютера  в качестве результата 
        field =[]
        for i in range(0,5):
            field.append([])
            for j in range(0,5):
                field[i].append('0')
        n = 0
        while n <5:
            i = random.randrange(0,5)
            j = random.randrange(0,5)
            if field[i][j] == '0':
                field[i][j] = '1'
                if i>0:
                    field[i-1][j] = '2'
                if i<4:
                    field[i+1][j] = '2'
                if j>0:
                    field[i][j-1] = '2'
                if j<4:
                    field[i][j+1] = '2'
                n+=1
        return(field)

   

class Game():
    def __init__(self, field, playersmap):  #класс введен с целью передачи полей из одной функции в другую не вызывая при этом одну в другой
        self.field = field
        self.playersmap =playersmap



    def playershoot(self):
        x = input('Введите первую координату выстрела')
        y = input('Введите вторую координату выстрела')
        if self.field[y][x] == '1':     #обработка выстрела игрока 
            self.field[y][x] = '3' 
            x=x-1
            y=y-1
            if x>0:
                self.field[y][x-1] ='4'
            if x<4:
                self.field[y][x+1] ='4'
            if y>0:
                self.field[y-1][x] ='4'
            if y<4:
                self.field[y+1][x] ='4'
            n=1
        else :
            self.field[x][y] == '4'
            n=0
        return(n)
                



    def computershoot(self):
        i = random.randrange(0,5)
        j = random.randrange(0,5)
        if self.playersmap[i][j] == '1':      #отображение попадания и клеток мимо вокруг  0 пусто 1 корабль 2 запретная зона вокруг 3 убит 4 мимо
            self.playersmap[i][j] = '3'
            if i>0:
                self.playersmap[i-1][j] = '4'
            if i<4:
                self.playersmap[i+1][j] = '4'
            if j>0:
                 self.playersmap[i][j-1] ='4'
            if j<4:
                self.playersmap[i][j+1] = '4'                            
            m=1
        elif self.playersmap[i][j] ==('2') or ('0'):
            self.playersmap[i][j] = '4'
            m=0
        return(m)
    

def playerprinter(fmap):
    for i in range(0,5):
        for j in range(0,5):
            if fmap[i][j] == '2' or '0':
                fmap[i][j] ='O'
            if fmap[i][j] == '1':
                fmap[i][j] ='V'
            if fmap[i][j] == '3':
                fmap[i][j] = 'X'
            if fmap[i][j] == '4':
                fmap[i][j] ='.'
    print(fmap)




def compprinter(fmap):
    for i in range(0,5):
        for j in range(0,5):
            if fmap[i][j] == '2' or '0':
                fmap[i][j] ='O'
            if fmap[i][j] == '1':
                fmap[i][j] ='O'
            if fmap[i][j] == '3':
                fmap[i][j] = 'X'
            if fmap[i][j] == '4':
                fmap[i][j] ='.'
    print(fmap)


        

def checkwin(fieldmap):
    for i in range(0,5):
        for j in range(0,5):
            if fieldmap[i][j] == '1':
                n+=1                   #фунция сообщающая попадание + запрос на новый выстрел
            if n == 0:
                print('Победа')
    a = 0
    return(a)






if __name__ =='__main__':
    a = 1
    compprinter(fieldgenerator())
    print('Поле компьютера')
    addship()
    while a!=0:
        if playersmap.playershoot() == 1:
            playersmap.playershoot()
        if checkwin(playersmap)== 0:
            print('Вы выйграли')
            break
        if field.computershoot() == 1:
            field.computershoot()
        if checkin(field) == 0:
            print('Вы проиграли')
            break
        
        
        

            
        



                
