import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_group(app):
    old_list = app.groups.get_group_list()
    new_group = random_string("gr_", 10)
    app.groups.add_new_group(new_group)
    new_list = app.groups.get_group_list()
    old_list.append(new_group)
    assert sorted(old_list) == sorted(new_list)


