import os
import time

def delete_photo(dict_photo_horizontal, dict_photo_vertical, final_dict_vertical, final_dict_horizontal, full_list_name_photo):

    sorted_final_dict_horizontal = {}
    sorted_keys = sorted(final_dict_horizontal, key=final_dict_horizontal.get)
    for w in sorted_keys:
        sorted_final_dict_horizontal[w] = final_dict_horizontal[w]

    sorted_final_dict_vertical = {}
    sorted_keys = sorted(final_dict_vertical, key=final_dict_vertical.get)
    for w in sorted_keys:
        sorted_final_dict_vertical[w] = final_dict_vertical[w]

    list_1 = []
    list_2 = []
    
    final_spisok = []

    list_1 = list(sorted_final_dict_horizontal.keys())
    list_2 = list(sorted_final_dict_vertical.keys())

    print(list_1)
    print(list_2)
    final_spisok = list_1 + list_2
    print('Финальный список', final_spisok)
    print('ПОЛНЫЙ список', full_list_name_photo)
    
    for item in full_list_name_photo:
        if item in final_spisok:
                print(f'Файл {item} нужен')
        else:
            try:
                time.sleep(0.1)
                os.remove(item)
                time.sleep(0.1)
            except:
                print(f'Файл {item} не найден')
                continue

    

    



   
