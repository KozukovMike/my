import copy
import random
import statistics
from copy import deepcopy


list_of_hair = ['blond', 'dark', 'dark brown', 'orange', 'white', 'light blond']
list_of_eye = ['blue', 'green', 'brown', 'dark', 'hazel', 'gray']
man_names = [
                'Alexander', 'Alexey', 'Anatoly', 'Andrey', 'Anton', 'Bogdan', 'Boris', 'Denis', 'Dmitry',
                'Eduard', 'Elisei', 'Gleb', 'Grigory', 'Grischa', 'Ilya', 'Iosif', 'Ivan', 'Kirill',
                'Kliment', 'Kolya', 'Matvei', 'Maxim', 'Mikhail', 'Vadim', 'Valentin', 'Valery'
            ]
woman_names = [
                    'Anna', 'Alina', 'Angelyna', 'Anastasia', 'Karolina', 'Katerina', 'Katya',
                    'Lada', 'Lana', 'Larissa', 'Lena', 'Lina', 'Ludmila', 'Marina', 'Mariya',
                    'Marta', 'Tamara', 'Tanya', 'Valentina', 'Valeria', 'Varvara', 'Olga'
              ]


class Human:
    name: str
    surname: str
    eye_color: str
    hair_color: str
    birthday: str
    age: float

    def __init__(self):
        self.hair_color = random.choice(list_of_hair)
        self.eye_color = random.choice(list_of_eye)

    def eating(self):
        return f'{self.name} {self.surname} is eating'

    def sleeping(self):
        return f'{self.name} {self.surname} is sleeping'

    def walk(self):
        return f'{self.name} {self.surname} walks'

    def playground(self):
        if isinstance(self, (Man, Woman)):
            return f'{self.name} {self.surname} not a child'
        else:
            return f'{self.name} {self.surname} is on the playground'

    def field_work(self):
        if isinstance(self, (Man, Woman)):
            return f'{self.name} {self.surname} can work on the field'
        else:
            return f'{self.name} {self.surname} is a child'

    def hunt(self):
        if isinstance(self, Boy):
            return f'{self.name} {self.surname} is hunting'
        else:
            return f'{self.name} {self.surname} is female'

    def growing_up(self):
        self.age += 1/12

    def die(self):
        if random.random() < statistics.NormalDist(80, 8.3).cdf(self.age):
            return True
        else:
            return False


class Boy(Human):
    parents: list

    def __init__(self, date: list, parents: list):
        super(Boy, self).__init__()
        self.name = random.choice(man_names)
        self.surname = f'{random.choice(man_names)}surname'
        self.age = 0
        self.birthday = f'{date[0]}.{date[1]}'
        self.parents = parents


class Girl(Human):
    parent: list

    def __init__(self, date: list, parents: list):
        super(Girl, self).__init__()
        self.name = random.choice(woman_names)
        self.surname = f'{random.choice(woman_names)}surname'
        self.age = 0
        self.birthday = f'{date[0]}.{date[1]}'
        self.parents = parents


class Man(Boy):
    marriage: bool

    def __init__(self, b: Boy):
        self.age = b.age
        self.name = b.name
        self.surname = b.surname
        self.hair_color = b.hair_color
        self.eye_color = b.eye_color
        self.birthday = b.birthday
        self.parents = b.parents
        self.marriage = False


class Woman(Girl):
    pregnant: bool
    marriage: bool
    gestation_period: int

    def __init__(self, g: Girl):
        self.age = g.age
        self.name = g.name
        self.surname = g.surname
        self.hair_color = g.hair_color
        self.eye_color = g.eye_color
        self.birthday = g.birthday
        self.parents = g.parents
        self.pregnant = False
        self.marriage = False
        self.gestation_period = 0

    def fertilization(self):
        if self.age < 50:
            self.pregnant = True if random.random() < 0.3 else False
        else:
            self.pregnant = False

    def update_fetus(self):
        self.gestation_period += 1


def update_date(date: list):
    '''
    обновляет дату на 1 месяц
    :param date:
    :return: date
    '''
    date[0] += 1
    date[1] += date[0] // 12
    date[0] %= 12
    return date


def use_growing_up():
    '''
    обновляет возраст всех с списке +1 к месяцу
    :param list1:
    :return:
    '''
    for i in range(len(people)):
        people[i].growing_up()


def meeting():
    '''
    реализация встречи раз в месяц
    :return:
    '''
    i = 0
    while i < len(list_men_not_married):
        j = 0
        while j < len(list_women_not_married):
            if (list_men_not_married[i].parents[0] == list_women_not_married[j].parents[0]
                or list_men_not_married[i].parents[1] == list_women_not_married[j].parents[1]
            ):
                pass
            else:
                r_number = random.random()
                if (
                        list_men_not_married[i].eye_color == list_women_not_married[j].eye_color or
                        list_men_not_married[i].hair_color == list_women_not_married[j].hair_color
                ) \
                        and r_number < 0.35:
                    married.append([list_men_not_married[i], list_women_not_married[j]])
                    list_women_not_married[j].marriage = True
                    list_men_not_married[i].marriage = True
                    del list_men_not_married[i]
                    del list_women_not_married[j]
                    break
                elif r_number < 0.25:
                    married.append([list_men_not_married[i], list_women_not_married[j]])
                    list_women_not_married[j].marriage = True
                    list_men_not_married[i].marriage = True
                    del list_men_not_married[i]
                    del list_women_not_married[j]
                    break
            j += 1
        if j == len(list_women_not_married):
            i += 1
    return married


def birth_or_not():
    '''
    обновляет беременность женщин
    :return:
    '''
    for i in range(len(married)):
        if not married[i][1].gestation_period:
            married[i][1].fertilization()
            if married[i][1].pregnant:
                married[i][1].update_fetus()
        else:
            married[i][1].update_fetus()
        if married[i][1].gestation_period == 9:
            married[i][1].gestation_period = 0
            married[i][1].pregnant = False
            if random.randint(0, 1):
                list_boys.append(Boy(data_of_date, married[i]))
            else:
                list_girls.append(Girl(data_of_date, married[i]))


def death():
    '''
    если человек умер, то удаляет его из списка
    :param list1:
    :return: list2
    '''
    for i in range(len(people)):
        if people[i].die():
            list_of_deaths.append(i)


def become_18():
    '''
    переход в другой класс
    :return: список объектов которых надо занести в другой класс
    '''
    k = 0
    while k < len(list_boys):
        if round(list_boys[k].age, 1) == 18:
            list_men_not_married.append(Man(list_boys[k]))
            del list_boys[k]
        else:
            k += 1
    k = 0
    while k < len(list_girls):
        if round(list_girls[k].age, 1) == 18:
            list_women_not_married.append(Woman(list_girls[k]))
            del list_girls[k]
        else:
            k += 1


if __name__ == '__main__':
    data_of_date = [0, 1000]
    list_men_not_married = []
    list_women_not_married = []
    married = []
    list_girls = []
    list_boys = []
    people = []
    married_men = []
    married_women = []
    list_of_deaths = []
    for i in range(20):
        month = random.randint(0, 11)
        years = random.randint(20, 69)
        a = Boy([12 - month, 1000 - years], [f'First Man{i}', f'First Woman{i}'])
        list_men_not_married.append(Man(a))
        list_men_not_married[i].age = years + month/12
        month = random.randint(0, 11)
        years = random.randint(20, 69)
        a = Girl([12 - month, 1000 - years], [f'{i}First Man', f'{i}First Woman'])
        list_women_not_married.append(Woman(a))
        list_women_not_married[i].age = years + month / 12
    for _ in range(300):
        people = (list_men_not_married +
                  list_women_not_married +
                  list_boys +
                  list_girls +
                  married_women +
                  married_men
                  )
        meeting()
        married_men = [i[0] for i in married]
        married_women = [i[1] for i in married]
        print(
            f'в начале месяца на острове {len(list_men_not_married) + len(married)} мужчин',
            f'{len(list_women_not_married) + len(married)} женщин',
            f'{len(list_boys)} мальчиков',
            f'{len(list_girls)} девочек'
        )
        data_of_date = update_date(data_of_date)
        birth_or_not()
        use_growing_up()
        become_18()
        death()
        # list_boys = list_boys(filter(lambda x: x not in list_of_deaths, list_boys))
        # list_girls = list_girls(filter(lambda x: x not in list_of_deaths, list_girls))
        # list_men_not_married = list_men_not_married(filter(lambda x: x not in list_of_deaths, list_men_not_married))
        # list_women_not_married = list_women_not_married(filter(lambda x: x not in list_of_deaths, list_women_not_married))
        # married_men = married_men(filter(lambda x: x not in list_of_deaths, married_men))
        # married_women = married_women(filter(lambda x: x not in list_of_deaths, married_women))
        i = 0
        while i < len(married):
            if married[i][0] in list_of_deaths and married[i][1] not in list_of_deaths:
                list_women_not_married.append(married[i][1])
                del married[i]
            elif married[i][0] not in list_of_deaths and married[i][1] in list_of_deaths:
                list_men_not_married.append(married[i][0])
                del married[i]
            elif married[i][0] in list_of_deaths and married[i][1] in list_of_deaths:
                del married[i]
            elif married[i][0] not in list_of_deaths and married[i][1] not in list_of_deaths:
                i += 1
        print(
            f'в конце месяца на острове {len(list_men_not_married) + len(married)} мужчин',
            f'{len(list_women_not_married) + len(married)} женщин',
            f'{len(list_boys)} мальчиков',
            f'{len(list_girls)} девочек'
        )
print(people)
print(isinstance(people[0], Human))
print(people[0])
print(len(list_men_not_married))
print(list_boys[0].age)
print(data_of_date)
print(len(list_of_deaths))
print('the end')

