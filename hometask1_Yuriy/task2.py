"""
Создать и вывести с помощью print() список который будет хранить данные о пользователе которые хранятся в словаре base:
login, avatar, email, phone, gdpr_data, loss_limit_amount.
ответ в формате: ['Test_login', 'banana', 1000]

Создать и вывести с помощью print() словарь который будет хранить ключи со значениями.
ключи: login, avatar, email, phone, gdpr_data, loss_limit_amount.
ответ в формате: {'login': 'Test_login', 'loss_limit_amount': 1000}
только перечисленные ключи должны быть в словаре
Выполняем задание теми средствами которые вчера прошли.
если у кого то есть опыт работы с циклами, можно сделать и прислать мне как альтернативное решение
"""

import base_dict

new_dict={}
new_dict["login"] = base_dict.base.get("login")
new_dict["avatar"] = base_dict.base.get("avatar")
new_dict["email"] = base_dict.base.get("email")
new_dict["phone"] = base_dict.base.get("phone")
new_dict["gdpr_data"] = base_dict.base.get("gdpr_data")
new_dict["loss_limit_amount"] = base_dict.base.get("loss_limit").get("amount")

# а вот еще один способ добавления значения в словарь,
# но он показался мне не таким читаемым, как 1-ый
# new_dict.update({"login": base_dict.base.get("login")})

print("Dictionary: ", new_dict)

new_dict = list(new_dict.values())
print("\nList: ", new_dict)