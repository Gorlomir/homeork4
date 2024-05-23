immutable_var_ = 1, 'Типочек', True
print(immutable_var_,  type(immutable_var_))
# immutable_var_[0] = 4 Изменить не получится, так как кортеж не поддерживает обращение по элементам.
mutable_list = [700, 'корнишоны', 'шаровары']
print(mutable_list)
mutable_list[0] = 300
mutable_list.remove('корнишоны')
mutable_list.append('Вячеслава')
print(mutable_list)
