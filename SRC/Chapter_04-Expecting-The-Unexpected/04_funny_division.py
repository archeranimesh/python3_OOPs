def funny_division(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky")
        return 100 / anumber
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"


if __name__ == "__main__":
    # The below line produces a ZeroDivisionError, which is caught
    # print(funny_division(0))
    print(funny_division(50.0))
    # the below raises a TypeErro
    print(funny_division("hello"))
