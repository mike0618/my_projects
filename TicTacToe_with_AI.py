from random import randint
from TTT_AI import ai
from time import sleep


def startttt():
    print('Welcome to the game tic-tac-toe!')
    ans = input("Are you ready to play? (Y/n): ").lower()
    if ans == '' or ans[0] == 'y' or ans[0] == 'д':
        game()
    else:
        print("Good bye!")


def again():
    ans1 = input("Would you like to play again? (Y/n): ").lower()
    if ans1 == '' or ans1[0] == 'y' or ans1[0] == 'д':
        game()
    else:
        print("Good bye!")


def display_board(b):
    print('\n' * 100)
    for i in range(5):
        if i % 2:
            print('---|---|---')
        else:
            rowpr = ''
            r = i // 2
            for c in b[2 - r]:
                if c == -1:
                    rowpr += ' X |'
                elif c == 1:
                    rowpr += ' O |'
                else:
                    rowpr += '   |'
            print(rowpr[:-1])


def game():
    ansai = input("Woudl you like to play with AI? (Y/n): ").lower()
    withai = ansai == '' or ansai[0] == 'y' or ansai[0] == 'д'
    if withai:
        level = 0
        lv = input('Choose AI level (0-Easy, 1-middle, 2-hard): ')
        if lv == '1' or lv == '2':
            level = int(lv)

    f = randint(0, 1)
    if f:
        print('X turns first')
    else:
        print('O turns first')
    cnt = f

    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def win():
        d1 = []
        d2 = []
        for i in range(3):
            cols = [r[i] for r in board]
            d1.append(board[i][i])
            d2.append(board[2 - i][i])
            if abs(sum(board[i])) == 3 or abs(sum(cols)) == 3:
                return True
        return abs(sum(d1)) == 3 or abs(sum(d2)) == 3

    def play(n, brd):
        if n == 1:
            player = 'O'
        else:
            player = 'X'

        if withai and n == 1:
            display_board(brd)
            print(f'Waiting for AI level {level}')
            sleep(0.5)
            ai(brd, level)
        else:
            position = 10
            r = 3
            c = 0
            while position not in range(1, 10) or brd[r][c] != 0:
                display_board(brd)
                print(player + ' turns...')
                try:
                    position = int(input("Enter your number 1-9: "))
                    r, c = divmod(position - 1, 3)
                except ValueError:
                    print('! Enter a NUMBER !')
            brd[r][c] = n
        if win():
            display_board(brd)
            print(player + ' - winner!!!')
            again()
            return True

    while True:
        if cnt % 2:
            cnt += 1
            if play(-1, board):
                break
        else:
            cnt += 1
            if play(1, board):
                break
        if cnt == 9 + f:
            display_board(board)
            print('DRAW!')
            again()
            break


if __name__ == "__main__":
    startttt()
