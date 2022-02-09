from docx import Document



def func_replacements() -> dict:
    
    input_replacements = input("Введите ФИО пользователя, лицевой счет, дату составления договора, день, до которого необходимо оплачивать, \
                                серию/номер паспорта, кем и когда выдан паспорт, номер телефона, тип подключения, адрес подключения, \
                                стоимость тарифа логин и пароль для выхода в личный кабинет.")
   
    # Ф И О, 2331, 23-2323-2232, 23, 1212 121221, ФМС 900-003, 2323223, +7878878, стандарт_100, ул. Луговая 6у 123, 670, 23321, 3213213

    input_replacements = input_replacements.split(', ')
    key_replacements = ['%replace_name%', '%replace_ls%', '%replace_date%', '%replace_day%', '%replace_pasport_ser_num%', '%replace_pasport_place%', 
                        '%replace_pasprot_date%', '%replace_phone%', '%replace_type_connect%', '%replace_address%', '%replace_sum%',
                         '%replace_login%', '%replace_pass%']
    replacements = dict()

    for key, val in zip(key_replacements, input_replacements):
        replacements[key] = val

    return replacements


def pass_arguments_in_file(replacements: dict) -> None:
    path = ''
    doc = Document(path)

    for paragraph in doc.paragraphs:
        for key in replacements:
            paragraph.text = paragraph.text.replace(key, replacements[key])
    
    doc.save(f'document_{replacements[''%replace_ls%'']}.docx')


if __name__ == __main__:
    dict_replacements = func_replacements()
    pass_arguments_in_file(dict_replacements)
