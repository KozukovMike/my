import random
import datetime


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

    def __init__(self, date: list, parents: list):
        super(Man, self).__init__(date, parents)
        self.marriage = False


class Woman(Girl):
    pregnant: bool
    marriage: bool
    gestation_period: int

    def __init__(self, date: list, parents: list):
        super(Woman, self).__init__(date, parents)
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
    date[0] += 1
    date[1] += date[0] // 12
    date[0] %= 12
    return date


def use_growing_up(list1):
    for k in range(len(list1)):
        list1[k].growing_up()
    return list1


def fertilization_women(list1):
    for k in range(len(list1)):
        if not isinstance(list1[k], Woman):
            raise ValueError
        list1[k].fertilization()
    return list1


def meeting(list_men, list_women, married):
    i = 0
    while i < len(list_women):
        j = 0
        while j < len(list_women):
            if list_men[i].parents == list_women[j].parents:
                print('kukusiki')
            else:
                r_number = random.random()
                if (
                        list_men[i].eye_color == list_women[j].eye_color or
                        list_men[i].hair_color == list_women[j].hair_color
                ) \
                        and r_number < 0.35:
                    married.append([list_men[i], list_women[j]])
                    list_women[j].marriage = True
                    list_men[i].marriage = True
                    del list_men[i]
                    del list_women[j]
                    break
                elif r_number < 0.25:
                    married.append([list_men[i], list_women[j]])
                    list_women[j].marriage = True
                    list_men[i].marriage = True
                    del list_men[i]
                    del list_women[j]
                    break
            j += 1
        if j == len(list_women):
            i += 1
    return married


def birthday_or_not():
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


if __name__ == '__main__':
    data_of_date = [0, 1000]
    list_men = []
    list_women = []
    for i in range(20):
        month = random.randint(0, 11)
        years = random.randint(20, 69)
        list_men.append(Man([12 - month, 1000 - years], [f'First Man{i}', f'First Woman{i}']))
        list_men[i].age = years + month/12
        month = random.randint(0, 11)
        years = random.randint(20, 69)
        list_women.append(Woman([12 - month, 1000 - years], [f'{i}First Man', f'{i}First Woman']))
        list_women[i].age = years + month / 12
    print(list_men)
    print(list_women)
    for i in range(20):
        print(list_men[i].age, end='  ')
    list_men = use_growing_up(list_men)
    print()
    for i in range(20):
        print(list_men[i].age, end='  ')
    print()
    list_women = fertilization_women(list_women)
    for i in range(20):
        print(list_women[i].pregnant, list_women[i].age, end='  ')
    print()
    married = []
    married = meeting(list_men, list_women, married)
    married_men = [i[0] for i in married]
    married_women = [i[1] for i in married]
    print(len(married), len(married_women), len(married_men))
    print(len(list_women), len(list_men))
    OLga = Woman([1, 1], ['1', '1'])
    OLga.age = 20
    print(OLga.pregnant, OLga.age)
    OLga.fertilization()
    print(OLga.pregnant)
    if OLga.pregnant:
        for i in range(9):
            OLga.update_fetus()
        print(OLga.gestation_period)
        OLga.gestation_period = 0
    print(OLga.gestation_period)
    list_boys = []
    list_girls = []
    for _ in range(12):
        data_of_date = update_date(data_of_date)
        birthday_or_not()
    print(len(list_girls), len(list_boys))
    for i in list_girls:
        print(i.parents, i.birthday, i.name, i.surname)
    for i in list_boys:
        print(i.parents, i.birthday, i.name, i.surname)
    all = [*married_women, *married_men, *list_boys]
    for i in all:
        i.growing_up()
    print(all[0].age)
    print(married[0][1].age)