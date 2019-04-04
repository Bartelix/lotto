import pyautogui, time, pyperclip, re, openpyxl
from pynput.mouse import Button, Controller
from datetime import date, timedelta, datetime

'''
cordinates:
date: -1130,250
start numbers: -1059, 403    end: -884, 403,   dx = 175, dy = 0
notepad: -210, 995
'''
flag = True
mouse = Controller()

dates = '2019-01-24'

def mark_numbers(m):
    m.position = (-1060,600)
    m.press(Button.left)
    m.move(175,0)
    m.release(Button.left)


def copy():
    pyautogui.hotkey('ctrl', 'c')


def change_date(m, d):
    '''
    m - mouse controller
    d - date
    '''

    m.position = (-1130,447)
    m.click(Button.left, 1)
    time.sleep(0.8)
    pyautogui.press('enter')
    time.sleep(0.5)

    for i in range(10):
        pyautogui.press('backspace')
        time.sleep(0.01)
    
    time.sleep(0.2)

    for char in d:
        pyautogui.press(char)
        time.sleep(0.01)
    
    pyautogui.press('enter')


def lotto_date_generator(num, p=0):
    #lotto_days = [1, 3, 5]
    #lotto_days = [2, 5]
    lotto_days = [6]
    return [str(date.today() - timedelta(days = p) - timedelta(days = n)) for n in num if (date.today() - timedelta(days = p) - timedelta(days = n)).weekday() in lotto_days]


def main():
    wb = openpyxl.load_workbook('lotto.xlsx')
    sheet = wb['Dane']
    dates = lotto_date_generator(range(0, 500), 13167)
    row = sheet.max_row + 1
    index = 1
    pattern = re.compile(r'[0-9]{1,2}')
    for date in dates:
        start_time = time.time()
        change_date(mouse, date)
        time.sleep(4)
        mark_numbers(mouse)
        time.sleep(0.05)
        copy()
        numbers_copied = str(pyperclip.paste())
        numbers_list = pattern.findall(numbers_copied)
        sheet.cell(row = row, column = 1).value = date
        for col in range(2,8):
            sheet.cell(row = row, column = col).value = int(numbers_list[col - 2])
        row += 1
        print(index, '/', len(dates), date, numbers_list, time.time() - start_time, 's')
        index += 1
        wb.save('lotto.xlsx')


while(flag):
    start_time = time.time()
    main()
    flag = False
    print(time.time() - start_time)
# działa 9,5 sekundy jeden obieg