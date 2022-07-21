
class Date:
    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    # Update and return arguments with set & get. 
    def GetDay(self) -> int:
        return self._day

    def GetMonth(self) -> int:
        return self._month

    def GetYear(self) -> int:
        return self._year

    # A. 
    def __str__(self) -> str:
        return f"{self._day},{self._month},{self._year}" # printed. 

    # B. return True or False.
    def Is_valid(self) -> bool:

        """

        :return:
        """

        # list all the month with 31 days. 
        full_month = [1,3,5,7,8,10,12]
        # list all the month with 30 days. 
        full_month_last_day = [4,6,9,11]

        # check if day is in full month. 
        if self._month in full_month and self._day in range(1,32):
            return True
        # check if day is in 30 days. 
        elif self._month in full_month_last_day and self._day in range(1,31):
            return True
        # check if day 28/29 days. 
        elif self._month == 2:
            if self._year%4 == 0 and self._day in range(1,30):
                return True
            elif self._year%4 != 0 and self._day in range(1,29):
                return True
            else:
                return False
        else: 
            return False

    # C. return new date one day after.
    def Get_next_day(self) -> object:
        """

        :return:
        """
        # list all the month with 31 days.
        full_month = [1, 3, 5, 7, 8, 10, 12]
        # list all the month with 30 days.
        full_month_last_day = [4, 6, 9, 11]

        # update the day. 
        day = 1
        # update the month, 
        month = self._month
        # update the year. 
        year  = self._year
        # reset date if in full month. 
        if  self._month in full_month:
            # reset day & month if full month. 
            if self._day == 31 and self._month == 12:
               month = 1
               year +=1
              
            # reset month & day if end. 
            elif self._day == 31 and self._month < 12:
                month +=1
               
            # update day. 
            elif self._day < 31:
                day += self._day
               
        # reset date if  month in 30 days. 
        elif self._month in full_month_last_day:
            # reset month & day if end. 
            if self._day == 30: 
                month += 1

            # update day. 
            elif self._day in range(1,30):
                day += self._day


       # reset date if month less then 29 days. 
        elif self._month == 2:
            # update month if end.
            if  self._day in range(28, 30):
                month += 1
            # update day. 
            elif self._day < 28:
                day += self._day
        otherdate = Date(day, month, year)
        return otherdate

    # D. reutrn date after adding days to the arguments.
    def Get_Next_Days(self, days) -> object:
        """

        :param days:
        :return:
        """
        day = 0
        month = self._month
        year = self._year
        total_days = days + self._day
        # list all the month with 31 days.
        full_month = [1, 3, 5, 7, 8, 10, 12]
        # list all the month with 30 days.
        full_month_last_day = [4, 6, 9, 11]
        # update if full month. 
        if self._month in full_month:
            # update day. 
            day = total_days%31

            # update month. 
            total_month = (total_days//31) + self._month
            month = total_month%12

            # update year. 
            year += (total_month//12)
        # update if month is 30 days. 
        elif self._month in full_month_last_day:
            # update day.
            day = total_days%30

            # update month. 
            total_month = (total_days//31) +self._month
            month = total_month%12

            # update year. 
            year += (total_month//12)
        # update if month is feb.
        elif self._month == 2 and self._day in range(1, 30): 
            if self._year%4 != 0 and self._day in range(1, 29):
                day = total_days % 28
                total_month = (total_days//28) + self._month
                month = total_month % 12
                year += (total_month // 12)
            elif self._year%4 == 0 and self._day in range(1, 30):
                day = total_days % 29
                total_month = (total_days//29) + self._month
                month = total_month % 12
                year += (total_month // 12)
       
        # reset day & month if zero. 
        if day == 0:
            day =1
        elif month == 0:
            month = 1
        elif month == 0 and day == 0:
            month = 1
            day =1
        
        # Update Date. 
        self._day = day
        self._month = month
        self._year = year
        next_days = Date(self._day, self._month, self._year)
        return next_days

    # E. eq, ne, lt, gt
    def __eq__(self, other: "Date") -> bool:
        """ recevied other date obj & return true if equales """
        # validate all the arguments if equale. 
        if self._day == other.GetDay() and self._month == other.GetMonth() and self._year == other.GetYear():
            return True
        else: 
            return False

    def __ne__(self, other: "Date") -> bool:
        """ received other date obj and return True if not equales"""
        if self._day != other.GetDay():
            return True
        elif self._month != other.GetMonth():
            return True
        elif self._year != other.GetYear():
            return True
        else: 
            return False

    def __gt__(self, other: "Date") -> bool:
        """ receive other date obj & return True if current greater """
        if self._year >= other.GetYear():
            if self._year > other.GetYear():
                return True
            elif self._year == other.GetYear():
                if self._month > other.GetMonth():
                    return True
                elif self._month == other.GetMonth():
                    if self._day > other.GetDay():
                        return True
                    else:
                        return False
        else:
            return False

    def __lt__(self, other: "Date") -> bool:
        """ received other obj date & return true if current less then obj. """
        if self._year <= other.GetYear():
            if self._year < other.GetYear():
                return True
            elif self._year == other.GetYear():
                if self._month < other.GetMonth():
                    return True
                elif self._month == other.GetMonth():
                    if self._day < other.GetDay():
                        return True
                    else:
                        return False
        else:
            return False

    # F. return remainder of current & object date.
    def Subtract(self, other: "Date") -> int:
        """ receviced object of Date & return remainder of current & obj dates """
        day = abs(self._day -  other.GetDay())
        month = abs((self._month - other.GetMonth()) * 31)
        year = abs(((self._year - other.GetYear()) * 12) * 31)

        return day + month + year


def main():
    today = Date(1, 2, 2022)
    other_date = Date(2, 2, 2022)
    print(today.Subtract(other_date))
if __name__ == "__main__":
    main()