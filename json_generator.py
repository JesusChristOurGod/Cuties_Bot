
typ = ""
eatable=""
household=""
size=""
area=""
while True:
    f = open("json_animals.txt", "a+")
    typ = ""
    eatable = ""
    household = ""
    size = ""
    area = ""
    print("Название жвиотного")
    name = input()
    while typ not in {"млекопитающее", "рептилия", "амфибия", "птица", "рыба", "моллюск",  "насекомое", "неведомое"}:
        print("Тип животного (млекопитающее, рептилия, амфибия, птица, рыба, моллюск,  насекомое, неведомое)")
        typ = input()
    while eatable not in {"да", "нет", "иногда"}:
        print("Сьедобное")
        eatable=input()
    while household not in {"дикое", "домашнее", "сельское"}:
        print("Домащнее?")
        household=input()
    while size not in {"микро", "маленький", "средний", "большой"}:
        print("Размер")
        size = input()
    while area not in {"воздух","земля","вода"}:
        print("Среда")
        area = input()
    js = '{ "name":'+'"'+name+'"'+', "typ":'+'"'+typ+'"'+', "eatable":'+'"'+eatable+'"'+', "household":'+'"'+household+'"'+', "size":'+'"'+size+'"'+', "area":'+'"'+area+'"'+'}'
    f.write(js)
    f.write("\n")
    f.close()