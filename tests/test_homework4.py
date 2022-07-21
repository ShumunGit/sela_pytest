import pytest
import logging
import datetime


@pytest.fixture(scope="class")
def Get_Date(request):
    request.cls.day = 4
    request.cls.month = 3
    request.cls.year = 2015
    logging.info("scope get date with class")


def date_full_moth(day: int, month: int) -> bool:
    """
    1. receive day and month and evaluate them if full month of 31 days.
    2. evaluate date between range of 1 - 31 and month with list of specific months.
    :param day: int, month: int, full_month: list
    :return: true: bool, false: bool
    """
    # list all the month with 31 days.
    full_month = [1, 3, 5, 7, 8, 10, 12]
    if day in range(1, 32) and month in full_month:
        return True
    else:
        return False


def date_full_month_last_day(day: int, month: int) -> bool:
    """
    1. receive day and month and evaluate them if full month of 30 days.
    2. evaluate date between range of 1 - 30 and month with list of specific months.
    :param day: int, month: int, full_month_last_day: list
    :return: true: bool, false: bool
    """
    full_month_last_day = [4, 6, 9, 11]
    if day in range(1, 31) and month in full_month_last_day:
        return True
    else:
        return False


def date_min_days(day: int, year: int) -> bool:
    """

    :param day:
    :param year:
    :return:
    """
    # evaluate if day 28/29 days.
    if year % 4 == 0 and day in range(1, 30):
        return True
    elif year % 4 != 0 and day in range(1, 29):
        return True
    else:
        return False


class OtherDate:
    def __init__(self, day=4, month=2, year=2012):
        self.otherday = day
        self.Othermont = month
        self.Otheryear = year


@pytest.mark.usefixtures("Get_Date")
class TestDate:

    @pytest.mark.smoke
    def __str__(self):
        print(f"{self.day}, {self.month}, {self.year}")

    def test_str(self, capfd):
        TestDate.__str__(self)
        out, err = capfd.readouterr()
        assert out == f"{self.day}, {self.month}, {self.year}\n"

    def test_Is_valid(self):
        """
        1. receive date parameters from get date function.
        2. evaluate the year if in range of possible of 4-digit number.
        3 . assert the day and month with 3 efferent functions of 31 days, 30 days, or 28/29 days.
        4. variable date to get the range of current year.
        :param: other: int
        :return: logging info message - date is valid else not valid.
        """
        other = datetime.datetime.now()
        # evaluate if the date is 31 days.
        if self.year in range(1500, other.year+1):
            if self.month in [1, 3, 5, 7, 8, 10, 12]:
                assert date_full_moth(self.day, self.month),\
                    logging.error("date is not valid")
                logging.info("date is valid.")
            # evaluate if the date is 30 days.
            elif self.month in [4, 6, 9, 11]:
                assert date_full_month_last_day(self.day, self.month),\
                    logging.error("date is not valid")
                logging.info("date is valid.")
            # evaluate if the date is 28/9 days.
            elif self.month == 2:
                assert date_min_days(self.day, self.year), \
                    logging.error("date is not valid")
                logging.info("date is valid.")
        else:
            assert isinstance(self.year,  type(1)), logging.info("year is not comparable")
            logging.info("year is not in range!")

    def test_Get_next_day(self):
        """
        1.
        :return:
        """
        # update the day.
        day = self.day
        # update the month,
        month = self.month
        # update the year.
        year = self.year
        # update date if in full month.
        if date_full_moth(self.day, self.month):
            # update full date.
            if self.day == 31 and self.month == 12:
                month = 1
                year += 1
            # update month.
            elif self.day == 31 and self.month < 12:
                month += 1
            # update day.
            elif self.day < 31:
                day += 1

        # reset date if month in 30 days.
        elif date_full_month_last_day(self.day, self.month):
            # reset month & day.
            if self.day == 30:
                month += 1
            # update day.
            elif self.day in range(1, 30):
                day += 1

        # reset date if month less than 29 days.
        elif self.month == 2:
            # update month.
            if self.day in range(28, 30):
                month += 1
            # update day.
            elif self.day < 28:
                day += 1

        other_day = OtherDate(day, month, year)
        current_date = OtherDate(self.day, self.month, self.year)
        assert other_day != current_date,\
            logging.error("date is not updated to next day.")
        logging.info(f"date is, {self.day}/{self.month}/{self.year}, date on next day {day}/{month}/{year}")

    def test_Next_Days(self, days=10):
        """
        1. received int value to add to the date object.
        2. update the date with add number days of the days.
        3. assert and evaluate the update day with added days, and logging info message.
        param: day: int, month: int , year:int, total_days: int
        """
        day = 0
        month = self.month
        year = self.year
        total_days = days + self.day

        # update if full month.
        if date_full_moth(self.day, self.month):
            # update day.
            day = total_days % 31
            # update month.
            total_month = (total_days // 31) + self.month
            month = total_month % 12
            # update year.
            year += (total_month // 12)
        # update if month is 30 days.
        elif date_full_month_last_day(self.day, self.month):
            # update day.
            day = total_days % 30
            # update month.
            total_month = (total_days // 30) + self.month
            month = total_month % 12
            # update year.
            year += (total_month // 12)
        # update if month is feb.
        elif self.month == 2 and self.day in range(1, 30):
            if self.year % 4 == 0:
                day = total_days % 29
                total_month = (total_days // 29) + self.month
                month = total_month % 12
                year += (total_month // 12)
            elif self.ear % 4 != 0 and self.day in range(1, 29):
                    day = total_days % 28
                    total_month = (total_days // 28) + self.month
                    month = total_month % 12
                    year += (total_month // 12)

        # reset day & month if zero.
        if day == 0:
            day = 1
        elif month == 0:
            month = 1
        elif month == 0 and day == 0:
            month = 1
            day = 1
            # Update Date.
        self.day = day
        self.month = month
        self.year = year
        other_day = OtherDate(day, month, year)
        current_date = OtherDate(self.day, self.month, self.year)
        assert other_day != current_date
        logging.info(f"{days} days add to month, {self.day}/{self.month}/{self.year}")

    def test__Sub__(self):
        """
        1. subtract the date values with the current day.
        2. convert the result  into days.
        :return: sum of the days.
        """
        other = datetime.datetime.now()

        day = abs(self.day - other.day)
        month = abs((self.month - other.month) * 31)
        year = abs(((self.year - other.year) * 12) * 31)

        assert (day + month + year) == 2745, logging.error("days is not equal")
        logging.info(f"sum of days is :{day + month + year}")

    def test__eq__(self):
        """
        1. assert and evaluate the date values with current date if equal.
        .2 logging info message.
        """
        other = datetime.datetime.now()
        assert self.day == other.day and self.month == other.month and self.year == other.year, logging.warning(
            "dates not equal")
        logging.info("scope equal")

    def test__ne__(self):
        """
        1. assert and evaluate the date values with the current date if not equal.
        2. logging info message.
        """
        other = datetime.datetime.now()
        assert self.day != other.day or self.month != other.month or self.year != other.year, logging.warning(
            "This test warning")
        logging.info("date is not equal to current date")

    def test__gt__(self):
        """
        1. assert and evaluate the date values and the current value if date is greater.
        2. logging info message.
        """
        flag = False
        other = datetime.datetime.now()
        if self.year >= other.year:
            if self.year > other.year:
                flag = True
        elif self.year == other.year:
            if self.month > other.month:
                flag = True
            elif self.month == other.month:
                if self.day > other.day:
                    flag = True
        assert flag, logging.error("date is not greater than current date")
        logging.info("date is grater than current date")

    def test__lt__(self):
        """
        1. assert and evaluate the date values with the current date if date is less than current.
        2. logging info message.
        """
        flag = False
        other = datetime.datetime.now()
        if self.year <= other.year:
            if self.year < other.year:
                flag = True
        elif self.year == other.year:
            if self.month < other.month:
                flag = True
            elif self.month == other.month:
                if self.day < other.day:
                    flag = True
        assert flag, logging.error("date is not less greater than current date")
        logging.info("date is less than current date")