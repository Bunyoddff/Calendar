class CalendarGenerator:
    def __init__(self):
        pass


    def is_leap_year(self,year):
        if (year%4==0 and year%100!=0) or (year%400==0):
            return True
        else:
            return False

    def get_days_in_month(month,year):
        pass


    def get_start_day_of_month(month,year):
        pass


    def build_grid_string(start_day_index,total_days):
        pass


    def generate_calendar(month,year):
        pass
if __name__ == "__main__":
    Cg = CalendarGenerator()
    print(Cg.is_leap_year(2023))