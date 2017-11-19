from datetime import datetime, date
from user_id import UserId
from friends import Friends

if __name__ == "__main__":
    ages_dct = dict()
    get_user_id = UserId(input())
    get_friends = Friends(get_user_id.execute())
    for f in get_friends.execute():

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

    items = sorted(ages_dct.items(), key=lambda item: item[0])
    for key, value in items:
        print(key, end=' ')
        for i in range(value):
            print('#', end='')
        print()
