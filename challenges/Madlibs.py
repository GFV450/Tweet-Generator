def addResponse(madlib, response):
    madlib_length = len(madlib)
    new_madlib = ""
    counter = 0

    # Iterates through the characters on a madlib
    for i in range(madlib_length):
        # Adds each character to the new_madlib variable
        new_madlib += madlib[i]

        if madlib[i] == "_" and counter == 0:
            # Changes underscore for user responde in new_madlib variable
            new_madlib = new_madlib.replace("_", response)
            # Avoids changing every underscore for current response
            counter = counter+1

    # Prints madlib modified by user
    print(new_madlib)

    return new_madlib


if __name__ == "__main__":
    madlib = "Make sure your lunch _ is filled with nutritious _ food. " \
             "Do not go to the _ food stand across the street from school"

    # Shows original madlib to the user
    print(madlib)

    # Reads and add first response to the madlib string
    response_one = raw_input("first answer: ")
    madlib_one = addResponse(madlib, response_one)

    # Reads and add second response to the madlib string
    response_two = raw_input("second answer: ")
    madlib_two = addResponse(madlib_one, response_two)

    # Reads and add third response to the madlib string
    response_three = raw_input("third answer: ")
    madlib_three = addResponse(madlib_two, response_three)
