from datetime import datetime, date
from user_id import UserId
from friends import Friends
from random import randint, normalvariate

import matplotlib.pyplot as plt

if __name__ == "__main__":
    ages_dct = dict()
    get_user_id = UserId(input())
    get_friends = Friends(get_user_id.execute())
    it_dict = get_friends.execute()
    for f in it_dict:

        if f.get('bdate') is None:
            continue

        bdate = f['bdate'].split('.')
        if len(bdate) != 3:
            continue

        age = datetime.now(tz=None).date() - date(int(bdate[2]), int(bdate[1]), int(bdate[0]))
        age = int(age.days / 365)

        if ages_dct.get(age) is None:
            ages_dct[age] = 1
        else:
            ages_dct[age] += 1

    x_axis = []
    y_axis = []

    items = sorted(ages_dct.items(), key=lambda item: item[0])
    for key, value in items:
        x_axis.append(key)
        y_axis.append(value)
        print(key, end=' ')
        for i in range(value):
            print('#', end='')
        print()

    plt.bar(x_axis, y_axis, align='center')
    plt.show()


