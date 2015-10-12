def letter_count(message):
    """
    Count all letters in a string
    :param message: string that will be counted
    :return: dictionary with keys of letters and values of counts
    """
    message = message.lower().replace(" ", "")

    freq = {}
    for letter in message:
        if letter not in freq:
            freq[letter] = 1
        else:
            current_value = freq[letter]
            freq[letter] = current_value + 1

    return freq

if __name__ == '__main__':
    print(letter_count("The Quick Brown Fox Jumped Over The Lazy Dog"))