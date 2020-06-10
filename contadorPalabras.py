#!/usr/bin/python3
import sys

def main():
    try:
        count = 0

        archivo = sys.argv[1]

        with open(archivo, 'r') as ar:
            for w in ar.read().split(' '):
                count += 1

        print(archivo + ' tiene ' + str(count) + ' palabra(s)')

    except FileNotFoundError:
        print('Nombre de archivo incorrecto')

    except IndexError:
        print('Nombre de archivo ausente')

if __name__ == '__main__':
    main()
