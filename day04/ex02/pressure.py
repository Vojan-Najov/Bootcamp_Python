from random import randrange
import time


def emit_gel(step):
    sign = 1
    pressure = 50
    while True:
        pressure = min(pressure, 100)
        receive_value = yield pressure
        if isinstance(receive_value, int):
            sign = -sign
        elif receive_value is not None:
            break
        pressure += sign * randrange(step + 1)


def valve():
    step = 14
    gen = emit_gel(step)

    pressure = next(gen)
    prev_pressure = pressure
    print(f'Mesuared pressure of liquid {pressure}')

    while 10 <= pressure <= 90:
        to_send = None
        if pressure > 80 and pressure > prev_pressure:
            to_send = -1
        elif pressure < 20 and pressure < prev_pressure:
            to_send = 1

        prev_pressure = pressure
        pressure = gen.send(to_send)

        time.sleep(0.1)
        print(f'Mesuared pressure of liquid {pressure}')

    try:
        gen.send('stop')
    except StopIteration as e:
        pass


if __name__ == '__main__':
    valve()

