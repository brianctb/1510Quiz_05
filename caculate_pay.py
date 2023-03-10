def calculate_pay(hours, wage):
    """
    Return an employee’s weekly pay

    :param hours: Any real numbers
    :param wage: Any real numbers
    :precondition: hours and wage must be real numbers
    :postcondition: calculates the employee's correct weekly pay
    :return: Employee's weekly pay as a real number
    >>> calculate_pay(0, 0)
    0
    >>> calculate_pay(35, 35)
    1225
    >>> calculate_pay(45, 20.0)
    1000
    """
    if hours <= 0:
        return 0
    elif wage <= 0:
        return 0
    elif hours <= 40:
        return hours * wage
    else:
        return (40 * wage) + ((hours - 40) * (wage * 2))


def main():
    """
    Drives the program.
    :return:
    """
    print("This is Quiz_05")


if __name__ == "__main__":
    main()
