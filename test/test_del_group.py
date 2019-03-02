import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_del_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) == 1:
        app.groups.add_new_group(random_string("gr_", 10))
        old_list = app.groups.get_group_list()
        print("осталась одна группа - удалять нельзя, добавлена группа для проверки удаления")
    group_to_del = random.choice(old_list)
    print(old_list)
    print(group_to_del)
    app.groups.del_group(group_to_del)
    old_list.remove(group_to_del)
    new_list = app.groups.get_group_list()
    print(old_list)
    print(new_list)
    assert sorted(old_list) == sorted(new_list)


