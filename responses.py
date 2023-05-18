from PyDictionary import PyDictionary
from autocorrect import Speller


def handle_response(message) -> str:

    if message.__contains__(' '):
        return 'Must be only one word.'
    dictionary = PyDictionary
    p_message = message.lower()
    str_response = dictionary.meaning(p_message, disable_errors=True)
    correct_spelling = p_message

    if str_response is None:
        spell = Speller()
        correct_spelling = spell(p_message)
        str_response = dictionary.meaning(correct_spelling)
        if str_response is None:
            return 'Couldn\'t find a definition for the word **' + p_message + '**.'

    str_response = format_str(str_response, p_message, correct_spelling)

    return str_response


def format_str(str_response, original_spelling, correct_spelling) -> str:
    final_str = ''
    counter = 1
    keys = list(str_response.keys())
    for key in keys:
        str_list = str_response.get(key)
        for definition in str_list:
            final_str += str(counter) + '. *' + key + '*: **' + definition + '**\n'
            counter += 1

    if original_spelling == correct_spelling:
        final_str = '**' + original_spelling + '**:\n' + final_str
    else:
        final_str = '*' + original_spelling + "* not found... showing results for:\n\n" + '**' + correct_spelling + '**:\n' + final_str

    return final_str
