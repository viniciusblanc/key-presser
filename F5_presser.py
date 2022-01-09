import time
import keyboard

def f5_presser():
    n = 0
    while 1:
        m, s = divmod(n, 60)
        print('{:02}:{:02}'.format(m, s), end='\r')
        time.sleep(1)
        n += 1
        if s == 0 and m % 10 == 0:
            keyboard.press_and_release('F5')

def main():
    print('Refresher 1.2')
    f5_presser()

if __name__ == '__main__':
    main()
