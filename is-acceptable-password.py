def is_acceptable_password(password):
    di = (len(list(filter(str.isdigit, password))))
    num = len(set(password))

    if 6 <= len(password) <= 9 and 0 < di < len(password) and password.lower().find('password') == -1 and len(
            set(password)) > 2:
        return True
    elif len(password) > 9 and len(set(password)) > 2 and password.lower().find('password') == -1:
        return True
    else:
        return False


def is_acceptable_password(password: str) -> bool:
    return bool(re.match(r"""
        # contains at least one digit and not digit and bigger than 6 or not less than 10
        ((?=.*\d)(?=.*\D)(?=.{7,})|(?=.{10,}))

        # not contain the word "password" in any case
        (?!(?i:.*password))

        # contains 3 different letters (or digits)
        (?P<x>.).*?(?!(?P=x))(?P<y>.).*?(?!(?P=x))(?!(?P=y))(.)""",
                         password, re.VERBOSE))