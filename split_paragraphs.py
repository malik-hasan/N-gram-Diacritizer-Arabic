input_string = ""
with open('jazeera_file.txt', 'r') as input_file:
    input_string = input_file.read()
    input_lines = input_string.split()
    output_lines = open("jazeera_output.txt", "w")
    counter = 0
    output_string = ""
    for line in input_lines:
        if counter < 7:
            output_string += line + " "
            counter += 1
        else:
            counter = 0
            output_lines.write(output_string+ "\n")
            output_string = ""
    output_lines.close()
