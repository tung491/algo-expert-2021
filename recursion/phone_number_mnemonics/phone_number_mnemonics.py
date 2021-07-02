DIGIT_LETTERS = {'0': '0', '1': '1', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                 '8': 'tuv', '9': 'wxyz'}


def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    found_memo = []
    current_memo = ['0'] * len(phoneNumber)
    phone_nmonics(0, phoneNumber, current_memo, found_memo)
    return found_memo


def phone_nmonics(idx, phoneNumber, current_memo, found_memo):
    if idx == len(phoneNumber):
        found_memo.append(''.join(current_memo))
    else:
        letters = DIGIT_LETTERS[phoneNumber[idx]]
        for letter in letters:
            current_memo[idx] = letter
            phone_nmonics(idx + 1, phoneNumber, current_memo, found_memo)


if __name__ == '__main__':
    phone_number = "1905"
    expected = ["1w0j", "1w0k", "1w0l", "1x0j", "1x0k", "1x0l", "1y0j", "1y0k", "1y0l", "1z0j", "1z0k", "1z0l"]
    print(f"Actual result: {phoneNumberMnemonics(phone_number)}. Expected: {expected}")