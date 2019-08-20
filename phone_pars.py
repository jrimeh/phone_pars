import re
import csv
import getpass
import os

directory = r'C:\\Users\\'+getpass.getuser()+'\\Desktop\\base'
files = os.listdir(directory)
for file in files:
    len_serach_file = len(file) - 4
    if  file[len_serach_file:] == r'.txt': 

        filepath = r'C:\\Users\\'+getpass.getuser()+'\\Desktop\\base\\'+file
        
        filepath2 = r'C:\\Users\\'+getpass.getuser()+'\\Desktop\\base\\output.csv'

        with open(filepath, "r+", newline="") as file,open(filepath2, 'w',newline="") as output:
        #читаем файл целиком
                f = set()
                sum_phone = 0
                pars_phon = 0
                for line in file:
                    a = line
                    sum_phone = sum_phone + 1            
                    print ("Количество номеров\строк:",sum_phone,        "\r",end='')
                    for a in re.findall(r'[^\r\n\D]', a),:
                        b = ''.join(a)
                        for b in re.sub(r'^9', '79', b),:
                            for b in re.sub(r'^8', '7', b),:
                            
                            
                                if len(b) == 11:
                                    
                                    pars_phon = pars_phon + 1 
                                    f.add(b +'\r\n')
                                    
                                    
                                                           
                f = list(f)
                Write_uniq_phone = 0 
                print("\nКоличество обработанных:",pars_phon,"\r\n",end='')
                for _ in f,:
                    a = _
                    for line in a:
                        output.write(line)
                        Write_uniq_phone = Write_uniq_phone + 1
                        #print("Записанно уникальных номеров в файл:",Write_uniq_phone,'\r',end='')
                print("\nфайл записан, колличество не валидных номеров:",sum_phone - Write_uniq_phone, "\r")
                input('Press ENTER to exit')
    print('Файла с расширением .txt в: ',directory,' не найден')
#input('Press ENTER to exit')
                            





