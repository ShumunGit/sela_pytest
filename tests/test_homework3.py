import logging
import pytest

dict_1 = {"name": "John", "gender": "male", "age": 32}
dict_2 = {"name": "Mike", "gender": "male", "age": 21}
dict_3 = {"name": "Alex", "gender": "male", "age": 40}
dict_4 = {"name": "Marina", "gender": "female", "age": 54}
lst_dict = [dict_1, dict_2, dict_3, dict_4]


@pytest.fixture
def nested_dict() -> dict:
    """
    1. update the list of list to list of dicts.
    :return: list of dicts,  list_dict: dict
    """
    global lst_dict
    lst_dict = {i: lst_dict[i] for i in range(len(lst_dict))}
    return lst_dict


@pytest.mark.printTests
def test_print_values_above(capfd: object, nested_dict: dict, num=30):
    """
    1. recevie nested dict, and int value to evaluate if num bigger than 0.
    2. received capfd to capture print errors.
    3. the function will print all the dict of people if num vlaue is equal to 0,
     else print all people with age greater than num.
    :param capfd: object
    :param nested_dict: dict
    :param num: integer
    :return: print the people form the received dict.
    """
    if num > 0:
        for i in range(len(lst_dict)):
            if nested_dict[i]["age"] > num:
                print(nested_dict[i])
                out, err = capfd.readouterr()
                assert out == f"{nested_dict[i]}\n"
        logging.info(f"scop of ages > {num}")
    else:
        for i in range(len(lst_dict)):
            print(nested_dict[i])
            out, err = capfd.readouterr()
            assert out == f"{nested_dict[i]}\n"
        logging.info(f"scope of all people")


@pytest.fixture
def split_male_female(nested_dict: object):
    """
    received nested dict & return two nested dict one male other female.
    :param nested_dict:: function, key_male: int, key_female: int
    :return: dict_of_male: dict, dict_of_female: dict
    """
    dict_of_male = {}
    dict_of_female = {}
    key_male = 0
    key_female = 0
    for i in range(len(lst_dict)):
        if nested_dict[i]["gender"] == "male":
            dict_of_male[key_male] = nested_dict[i]
            key_male += 1
        else:
            dict_of_female[key_female] = nested_dict[i]
            key_female += 1
    return dict_of_male, dict_of_female


def test_split_male_female(split_male_female):
    """
    1. received dict of mix gender people.
    2. extract them from the tuple to two return values.
    3. assert them with the split_male_female function.
    :param split_male_female: dict_lst_male: dict, dict__lst_female: dict
    :return: logging info message valuated dict.
    """
    dict_lst_male = split_male_female[0]
    dict__lst_female = split_male_female[1]
    assert dict_lst_male in split_male_female and dict__lst_female in split_male_female
    logging.info("scope of dict of male and dict of female")


@pytest.fixture
def median_average(nested_dict: object):
    """
    1. receive nested dict and find the average age, and median age.
    :param nested_dict: dic, avg_ages: float, sum_age: int, lst_ages: list, med_ages: int
    :return: avg_ages: float, med_ages: int
    """
    sum_age = 0
    lst_ages = []

    # count the sum of average.
    for i in range(len(nested_dict)):
        sum_age += nested_dict[i]["age"]
        # find the average.
        lst_ages.append(nested_dict[i]["age"])
        lst_ages = sorted(lst_ages)

    avg_ages = sum_age / len(nested_dict)
    # find median.
    med_ages = len(lst_ages) // 2
    if med_ages % 2 == 0:
        med_ages = lst_ages[med_ages - 1]
    else:
        med_ages = lst_ages[med_ages]
    return avg_ages, med_ages


def test_median_average(median_average):
    """
    1. received function with that received nested nested dicts.
    :param median_average: function, avg: float, med: int
    :return: assert message if avg: float and med: int is valeted.
    """
    avg = median_average[0]
    med = median_average[1]
    assert avg == 36.75 and med == 32
    logging.info("scope of average and median")
"""
@pytest.mark.smoke
def test_male_female(nested_dict: object):

    dict_of_male = {}
    dict_of_female = {}
    key_male = 0
    key_female = 0
    for i in range(len(nested_dict)):
        if nested_dict[i]["gender"] == "male":
            dict_of_male[key_male] = nested_dict[i]
            key_male += 1
        else:
            dict_of_female[key_female] = nested_dict[i]
            key_female += 1

    for i in range(len(dict_of_male)):
        assert dict_of_male[i]["gender"] == "male", logging.error("not all people in dict male")
    logging.info("scope dict list of male")
    for i in range(len(dict_of_female)):
        assert dict_of_female[i]["gender"] == "female", logging.error("not all people in the dict are female")
    logging.info("scope dict list of female")
"""
"""
1. received nested dict and spread the dict to two dicts one male sec female.
2. key for male and key for female to index the different lists.
3. test the two lists with diffrent assert one for gender male and one for female.
:param nested_dict: dict, dict_of_male: dict, dict_of_female: dict, key_male: int, key_female: int:
:return: logging info if success else return logging error.
"""



