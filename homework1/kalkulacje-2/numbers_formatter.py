def number_input(prompter_string):
    user_input = input(prompter_string)
    output = input_type_checker(user_input)
    return output


def input_type_checker(function_input):
    if "." in function_input:
        return float(function_input)
    elif "," in function_input:
        return float(function_input.replace(",", "."))
    else:
        return int(function_input)
