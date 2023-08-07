import os
import time

def delete_photo(dict_photo_horizontal, dict_photo_vertical, full_list_name_photo_vertical, full_list_name_photo_horizontal):
    
    # Отбираем самые горизонтальные карточки
    k = 0
    max_item_horizontal = dict_photo_horizontal['ширина'][0]

    list_photos_with_max_width = [max_item_horizontal] # ширина
    list_photos_index_horizontal = [k]
    list_photos_name_horizontal = []

    print('Горизонтальный список', list_photos_name_horizontal)
    list_photos_name_horizontal.append(dict_photo_horizontal['название_фотографии'][k])
    
    print('Горизонтальный список', list_photos_name_horizontal)
    n = 0
    for item in dict_photo_horizontal['ширина']:
        print(item, max_item_horizontal)

        if len(dict_photo_horizontal['ширина']) <= 3:
            list_photos_name_horizontal.append(dict_photo_horizontal['название_фотографии'])
            break
        else:
            if item > max_item_horizontal:
                max_item_horizontal = item
                list_photos_with_max_width.append(max_item_horizontal)
                list_photos_index_horizontal.append(k)
                list_photos_name_horizontal.append(dict_photo_horizontal['название_фотографии'][k])
        k += 1
        n += 1

    print('Горизонтальный список', list_photos_name_horizontal)

    print('ПОЛНЫЙ горизонтальный список', full_list_name_photo_horizontal)

    for item1 in full_list_name_photo_horizontal:
        for item2 in list_photos_name_horizontal:
            if item1 == item2:
                pass
            else:
                time.sleep(0.05)
                os.remove(item1)
                print(f'горизонтальная фотография {item1} удалена')
            
    # Отбираем самые вертикальные карточки
    k = 0
    n = 0
    max_item = dict_photo_vertical['высота'][0]

    list_photos_with_max_height = [max_item] # высота 
    list_photos_index_vertical = [k]
    list_photos_name_vertical = []
    list_photos_name_vertical.append(dict_photo_vertical['название_фотографии'][k])
    
    for item in dict_photo_vertical['высота']:
        if len(dict_photo_vertical['высота']) <= 3:
            list_photos_name_vertical.append(dict_photo_vertical['название_фотографии'])
            break
        else:
            if item > max_item:
                max_item = item
                list_photos_with_max_width.append(max_item)
                list_photos_index_vertical.append(k)
                list_photos_name_vertical.append(dict_photo_vertical['название_фотографии'][k])
        k += 1
        n += 1

    print('Вертикальный список', list_photos_name_vertical)
    for item in full_list_name_photo_vertical:
        for item2 in list_photos_name_vertical:
            if item == item2:
                pass
            else:
                # item = item.replace("\\\\", "\\")
                time.sleep(0.05)
                os.remove(item)
                print(f'вертикальная фотография {item} удалена')
