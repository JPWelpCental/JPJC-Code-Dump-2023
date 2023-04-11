def is_valid_ISBN10(isbn10):
    # Write your code here
    if len(isbn10) != 10:
        return "ISBN-10 must only have 10 digits."
    for i in range(10):
        if isbn10[i] not in "0123456789X":
            return "ISBN-10 can only contain numbers and the character 'X'."
        if isbn10[i] == 'X' and i != 9:
            return "'X' can only be found at the last digit of isbn10."
    sum = 0
    for i in range(9):
        sum += int(isbn10[i]) * (i + 1)
    if isbn10[9] == 'X':
        sum += 10 * 10
    else:
        sum += int(isbn10[9]) * 10
    if sum % 11 != 0:
        return "Wrong check digit."
    return "Valid ISBN-10."
