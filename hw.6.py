def print_gugudan_right_aligned():
    output = ""
    for row in range(1, 10):
        for dan in range(2, 6):
            result = dan * row
            output += f"{dan} x {row} = {result:2}\t"
        output += "\n"

    output += "\n"

    for row in range(1,10):
        for dan in range(6,10):
            result = dan * row
            output += f"{dan} x {row} = {result:2}\t"
        output += "\n"

    return output




