class CalendarGenerator:
    def __init__(self):
        pass


    def is_leap_year(self,year):
        return (year%4==0 and year%100!=0) or (year%400==0)

    def get_days_in_month(self,month,year):
        mon31=[1,3,5,7,8,10,12]
        mon30=[4,6,9,11]
        if month in mon31:
            return 31
        elif month in mon30:
            return 30
        elif self.is_leap_year(year) and month==2:
            return 28
        else:
            return 29


    def get_start_day_of_month(month,year):
        pass


    def build_grid_string(start_day_index,total_days):
        pass


    def generate_calendar(month,year):
        pass
if __name__ == "__main__":
    Cg = CalendarGenerator()
    print(Cg.is_leap_year(2024))
    print(Cg.get_days_in_month(2,2024))