def calculate_pay(hours, wage):
    """
    Return an employee’s weekly pay
    :param hours:
    :param wage:
    :return:
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
    print(calculate_pay(60, 20))


if __name__ == "__main__":
    main()
