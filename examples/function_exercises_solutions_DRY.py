def assert_dtypes(first_name, second_name, year_of_birth):
    assert type(first_name) is str, "first_name expected as a string"
    assert type(second_name) is str, "second_name expected as a string"
    assert type(year_of_birth) is int, "year_of_birth expected as an int"


def combine_names_and_year_as_tuple(first_name, second_name, year_of_birth):
    merged_names = str(first_name + " " + second_name)
    merged_names_and_year = (merged_names, year_of_birth)

    return merged_names_and_year


def combine_names_and_year_as_string(first_name, second_name, year_of_birth):
    merged_names = str(first_name + " " + second_name)
    merged_names_and_year = merged_names + ", born " + str(year_of_birth)

    return merged_names_and_year


def get_year_and_initials(first_name, second_name, year_of_birth):
    first_name_initial = first_name[0].upper()
    second_name_initial = second_name[0].upper()

    merged_initials_and_year = (
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

    list_of_functions = [
        combine_names_and_year_as_tuple,
        combine_names_and_year_as_string,
        get_year_and_initials,
        named_lambda_function,
    ]

    assert_dtypes("Richard", "Strange", 1995)

    for function in list_of_functions:
        print(function("Richard", "Strange", 1995))

    print([function("Richard", "Strange", 1995) for function in list_of_functions])
