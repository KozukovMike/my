class Time:

    timeline: list

    def __init__(self, start_time: str, end_time: str, delta: str):
        if not isinstance(start_time, str):
            raise ValueError
        if not isinstance(delta, str):
            raise ValueError
        if not isinstance(end_time, str):
            raise ValueError
        self.timeline = []
        self.start_time = start_time
        self.end_time = end_time
        self.delta = delta

    def get_timeline(self):
        if len(self.timeline):
            return self.timeline
        minutes = [self.start_time[self.start_time.find(':') + 1:], self.end_time[self.end_time.find(':') + 1:], self.delta[self.delta.find(':') + 1:]]
        hours = [self.start_time[:self.start_time.find(':')], self.end_time[:self.end_time.find(':')], self.delta[:self.delta.find(':')]]
        minutes = list(map(int, minutes))
        hours = list(map(int, hours))
        while (hours[0] < hours[1]) or (hours[0] == hours[1] and minutes[0] < minutes[1]):
            self.timeline.append(f'{hours[0]}:{minutes[0]}0' if minutes[0] == 0 else f'{hours[0]}:{minutes[0]}')
            hours[0] += (minutes[0] + minutes[2]) // 60
            hours[0] += hours[2]
            minutes[0] += minutes[2]
            minutes[0] %= 60
        if len(self.timeline) == 1:
            return 'свободного времени нет'
        else:
            return self.timeline

    def reserve_time(self, time: str):
        if time in self.timeline:
            del self.timeline[self.timeline.index(time)]
class ReverseDataTime:

    def __init__(self, dates: list[int], times: list[Time]):
        if not isinstance(dates, list):
            raise ValueError
        for i in dates:
            if not isinstance(i, int):
                raise ValueError
        if not isinstance(times, list):
            raise ValueError
        for i in times:
            if not isinstance(i, Time):
                raise ValueError
        self.dates = dates
        self.times = times

    def get_timeline(self, day: int):
        if day not in self.dates:
            raise 'такой даты не существует'
        return self.times[self.dates.index(day)].get_timeline()

    def reserve_time(self, day: int, time: str):
        if day not in self.dates:
            raise 'такой даты не существует'
        return self.times[self.dates.index(day)].reserve_time()

t = Time('10:30', '19:00', '0:45')
r = ReverseDataTime([1], [t])

print(t.end_time)
print(t.get_timeline())
t.reserve_time('14:15')
print(t.get_timeline())
print(r.get_timeline(1))
