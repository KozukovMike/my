import datetime


class Time:

    timeline: list

    def __init__(self, start_time: str, end_time: str, delta: str):
        if not isinstance(start_time, str):
            raise ValueError
        if not isinstance(delta, str):
            raise ValueError
        if not isinstance(end_time, str):
            raise ValueError
        self.timeline = [start_time]
        self.start_time = datetime.datetime.strptime(start_time, '%H:%M')
        self.end_time = datetime.datetime.strptime(end_time, '%H:%M')
        self.delta = datetime.timedelta(hours=int(delta.split(':')[0]), minutes=int(delta.split(':')[1]))

    def get_timeline(self):
        buf = self.start_time
        while buf < self.end_time:
            buf += self.delta
            self.timeline.append(buf.strftime('%H:%M'))
        return self.timeline

    def reserve_time(self, _time: str):
        if not isinstance(_time, str):
            raise ValueError
        if _time in self.timeline:
            del self.timeline[self.timeline.index(_time)]


class ReserveDateTime:

    def __init__(self, dates: list[int], times: list[Time]):
        if isinstance(dates, list):
            for i in dates:
                if not isinstance(i, int):
                    raise ValueError
        else:
            raise ValueError
        if isinstance(times, list):
            for i in times:
                if not isinstance(i, Time):
                    raise ValueError
        else:
            raise ValueError
        self.dates = dates
        self.times = times

    def get_timeline(self, day: int):
        if not isinstance(day, int):
            raise ValueError
        return self.times[self.dates.index(day)].get_timeline()

    def reserve_time(self, day: int, _time: str):
        if not isinstance(day, int):
            raise ValueError
        if not isinstance(_time, str):
            raise ValueError
        return self.times[self.dates.index(day)].reserve_time()
