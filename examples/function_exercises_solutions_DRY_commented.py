from typing import Tuple, List


def assert_dtypes(first_name: str, second_name: str, year_of_birth: int) -> None:
    """Checks that the input parameters are the correct datatype

    Args:
        first_name: str, the first (individual) name of the subject
        second_name: str, the second (family) name of the subject
        year_of_birth: int, the year of birth of the subject

    Returns: None

    Raises:
        AssertionError: on incorrect dtypes for first_name, second_name, year_of_birth

    """
    assert type(first_name) is str, "first_name expected as a string"
    assert type(second_name) is str, "second_name expected as a string"
    assert type(year_of_birth) is int, "year_of_birth expected as an int"


def combine_names_and_year_as_tuple(first_name: str, second_name: str, year_of_birth: int) -> Tuple:
    """ Merges the two names together with a space, and returns it with the year of birth

    Args:
        first_name: str, the first (individual) name of the subject
        second_name: str, the second (family) name of the subject
        year_of_birth: int, the year of birth of the subject

    Returns:
        Tuple, of a string of the concatenated names, and the int year of birth
    """
    merged_names: str = str(first_name + " " + second_name)
    merged_names_and_year: Tuple = (merged_names, year_of_birth)

    return merged_names_and_year


def combine_names_and_year_as_string(first_name: str, second_name: str, year_of_birth: int) -> str:
    """Concatenates the names and the year of birth, with a "born"

    Args:
        first_name: str, the first (individual) name of the subject
        second_name: str, the second (family) name of the subject
        year_of_birth: int, the year of birth of the subject

    Returns:
        String, of the concatenated names, "born" and year of birth
    """
    merged_names: str = str(first_name + " " + second_name)
    merged_names_and_year: str = merged_names + ", born " + str(year_of_birth)

    return merged_names_and_year


def get_year_and_initials(first_name: str, second_name: str, year_of_birth: int) -> str:
    """ Initialises the names and concatenates them with the year of birth

    Args:
        first_name: str, the first (individual) name of the subject
        second_name: str, the second (family) name of the subject
        year_of_birth: int, the year of birth of the subject

    Returns:
        String, of the initials and year of birth
    """
    first_name_initial: str = first_name[0].upper()
    second_name_initial: str = second_name[0].upper()

    merged_initials_and_year: str = (
        first_name_initial + "." + second_name_initial + ". " + str(year_of_birth)
    )

    return merged_initials_and_year


if __name__ == "__main__":

    named_lambda_function = (
        lambda first_name, second_name, year_of_birth: first_name[0].upper()
        + ". "
        + second_name
        + " "
        + str(year_of_birth)
    )

    list_of_functions: List = [
        combine_names_and_year_as_tuple,
        combine_names_and_year_as_string,
        get_year_and_initials,
        named_lambda_function,
    ]

    assert_dtypes("Richard", "Strange", 1995)

    for function in list_of_functions:
        print(function("Richard", "Strange", 1995))

    print([function("Richard", "Strange", 1995) for function in list_of_functions])
