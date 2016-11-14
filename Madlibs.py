madlib = "Make sure your lunch _ is filled with nutritious _ food. Do not go to the _ food stand across the street from school"
print(madlib)


def addResponse(madlib, response):
    length = len(madlib) - 1
    newMadlib = ""
    counter = 0

    for i in range(length):
        newMadlib += madlib[i]

        if madlib[i] == "_" and counter == 0:
            newMadlib = newMadlib.replace("_", response)
            counter = counter+1

    return newMadlib


response1 = raw_input("first answer: ")
madlib1 = addResponse(madlib, response1)
print(madlib1)

response2 = raw_input("second answer: ")
madlib2 = addResponse(madlib1, response2)
print(madlib2)

response3 = raw_input("third answer: ")
madlib3 = addResponse(madlib2, response3)
print(madlib3)
