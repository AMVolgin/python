def p_user(tmp_dict_user):
    print(tmp_dict_user)

u_name = input("Имя: ")
u_surname = input("Фамилия: ")
u_year_born = input("Год рождения: ")
u_city = input("Город: ")
u_mail = input("e-mail: ")
u_phone = input("Телефон: ")

dict_user = {
    "name": u_name,
    "surname": u_surname,
    "year_born": u_year_born,
    "city": u_city,
    "email": u_mail,
    "phone": u_phone
}
p_user(dict_user)