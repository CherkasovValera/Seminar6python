# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
print("Взято из файла")
with open("filerle.txt", "r") as filerle:
    rle = filerle.read()
print (rle)
print("___________________")
string =[rle[i] for i in range(len(rle))]

def encode_mess(string):
    encode_lst = ""
    i = 0
    while (i <= len(string)-1):
        count =1
        ch = string[i]
        j=i
        while (j < len(string)-1):
            if (string[j] == string[j+1]):
                count= count + 1
                j = j+1
            else:
                break
        encode_lst = encode_lst + str(count) + ch
        i = j+1
    return encode_lst

lst1 = encode_mess(string)
lst2 = lst1.replace("1", "")
print(lst2)

text_list = list(filter(lambda x : x.isdigit(), lst2))
text_list2 = list(filter(lambda x : not x.isdigit(), lst2))
decoded_str = ''
for i in range(len(text_list)):
    decoded_str += int(text_list[i])*text_list2[i]
print(decoded_str)
print("___________________")
print("Записано в файл")
with open("file_res.txt", "w") as file_res:
    file_res.write(decoded_str)
print(decoded_str)