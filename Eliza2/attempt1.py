def respond(incoming):
    return "hello"

while True:
            incoming = input('> ')

            output = respond(incoming)
            if output is None:
                break

            print(output)