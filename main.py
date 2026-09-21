import transmissionWrapper.L, position.L, message.L

import sys, time

def run(source):
    for line in source.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith("print "):
            value = line[6:].strip()
            print(value.strip('"'))

if __name__ == "__main__":
    with open(sys.argv[1], "r") as file:
        source = file.read()

    run(source)
while True:
    run(transmissionWrapper.L)
    run(position.L)
    run(message.L)

return
