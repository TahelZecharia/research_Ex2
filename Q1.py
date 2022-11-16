import re

def find_mail_addresses(file_name):
    """
    The function receives the name of a text file, and searches for email addresses in it.
    The function prints two lists: one list with all valid addresses, and a second list with all invalid addresses.

    1) file without email addresses (the file is not empty):
    >>> find_mail_addresses("NotMailAddresses.txt")
    valid_emails: []
    invalid_emails: []

    2) file without valid email addresses:
    >>> find_mail_addresses("MailAddressesInvalid.txt")
    valid_emails: []
    invalid_emails: ['tah#el@gmail.com', 'abcd_@efg.ff', '123456789@987654321_a.oo']

    3) file without invalid email addresses:
    >>> find_mail_addresses("MailAddressesValid.txt")
    valid_emails: ['abc.def@mail.com', 'good@morning.to.me', 'tahel123@gmail.com']
    invalid_emails: []

    4) A file with many addresses:
    >>> find_mail_addresses("MailAddresses.txt")
    valid_emails: ['abc-d@mail.com', 'abc.def@mail.com', 'abc@mail.com', 'abc_def@mail.com', 'abc.def@mail.cc', 'abc.def@mail-archive.com', 'abc.def@mail.org', 'abc.def@mail.com']
    invalid_emails: ['llll@pppp', 'abc-@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc#def@mail.com', 'abc.def@mail.c', 'abc.def@mail#archive.com', 'abc.def@mail', 'abc.def@mail..com']

    """

    # open the file
    try:
        with open(file_name) as file:
            file_str = file.read()

    except FileNotFoundError:
        print("there is no such file, try again…")

    # lists for the emails
    valid_emails = []
    invalid_emails = []

    # email Regular Expression:
    # \S - 	Returns a match where the string DOES NOT contain a white space character
    mail_addresse = re.findall('\S+@\S+', file_str)

    # valid email Regular Expression:
    # \. - the char '.'
    # {2,} - at least 2 chars
    regex = re.compile(r'([a-z0-9]+[._-])*[a-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    for add in mail_addresse:
        if re.fullmatch(regex, add):
            valid_emails.append(add)
        else:
            invalid_emails.append(add)

    print(f"valid_emails: {valid_emails}")
    print(f"invalid_emails: {invalid_emails}")

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# I helped with the code: https://stackabuse.com/python-validate-email-address-with-regular-expressions-regex/