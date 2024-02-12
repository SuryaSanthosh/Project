from .train import Train


class Train:
    def __init__(self, train_id, train_name, days_of_week, departure_station, route):
        self.train_id = train_id
        self.train_name = train_name
        self.days_of_week = days_of_week
        self.departure_station = departure_station
        self.route = route
