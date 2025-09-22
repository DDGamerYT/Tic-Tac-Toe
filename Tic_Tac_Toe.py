import pygame
import random
import os
import time
import json

pygame.init()

width, height = 300, 300
WIDTH = 330
HEIGHT = 595
screen = pygame.display.set_mode((330, 595))
pygame.display.set_caption("Tic Tac Toe")
icon_img = pygame.image.load('data/icon.png')
pygame.display.set_icon(icon_img)

bg_img = pygame.image.load('data/bg.jpg')
sylish_font = pygame.font.Font('data/sylishfont.ttf', 50)
button_font = pygame.font.Font('data/sylish.ttf', 24)
setting_font = pygame.font.Font('data/sylishfont.ttf', 18)
profile_font = pygame.font.Font('data/sylishfont.ttf', 12)
o_img = pygame.image.load('data/o.png')
x_img = pygame.image.load('data/x.png')
lobby_img = pygame.image.load('data/lobbyimage.png')
play_img = pygame.image.load('data/play-button.png')
setting_img = pygame.image.load('data/setting.png')
back_img = pygame.image.load('data/back.png')
coin_img = pygame.image.load('data/coin.png')
coin_font = pygame.font.Font('data/numberfont.ttf',32)
number_font = pygame.font.Font('data/numberfont.ttf',18)
message_font = pygame.font.Font('data/sylishfont.ttf', 20)
normal_font = pygame.font.Font(None, 32)
money_img = pygame.image.load('data/money.png')
edit_img = pygame.image.load('data/edit.png')
search_img = pygame.image.load('data/search.png')

profile_img = 'data/user.png'
profile_banner = 'data/profile_banner.png'

user_img = pygame.image.load(profile_img)
user_banner = pygame.image.load(profile_banner)
shop_img = pygame.image.load('data/shop.png')

dub_profile_img = 'data/dub_user.png'

user_1_img = pygame.image.load('data/user_1.png')
user_2_img = pygame.image.load('data/user_2.png')
user_3_img = pygame.image.load('data/user_3.png')

dub_user_img = pygame.image.load('data/dub_user.png')
dub_user_1_img = pygame.image.load('data/dub_user_1.png')
dub_user_2_img = pygame.image.load('data/dub_user_2.png')
dub_user_3_img = pygame.image.load('data/dub_user_3.png')

user_rect_1 = pygame.Rect(100, 100, 33, 33)
user_rect_2 = pygame.Rect(140, 100, 33, 33)
user_rect_3 = pygame.Rect(180, 100, 33, 33)

user_banner_1 = pygame.image.load('data/banner_1.png')
user_banner_2 = pygame.image.load('data/banner_2.png')

dub_banner = pygame.image.load('data/dub_banner.png')
dub_banner_1 = pygame.image.load('data/dub_banner_1.png')
dub_banner_2 = pygame.image.load('data/dub_banner_2.png')

banner_rect_1 = pygame.Rect(40, 180, 32, 25)
banner_rect_2 = pygame.Rect(80, 180, 32, 25)


edit_close_rect_1 = pygame.Rect(130, 190, 70, 40)
edit_close_rect_2 = pygame.Rect(180, 90, 70, 40)
dub_banner_rect = pygame.Rect(165, 125, 31, 25)
dub_user_rect = pygame.Rect(40, 170, 33, 33)
edit_user_banner_rect_1 = pygame.Rect(46,105,100,64)


run = True
winner = None

rows, cols = 3, 3
box_width = width // cols
box_height = height // rows
black = (0, 0, 0)

# edit screen rect's
edit_user_rect = pygame.Rect(165,155,66,66)
edit_user_banner_rect = pygame.Rect(46,155,100,64)
ok_rect = pygame.Rect(142, 290, 40, 25)
won_screen = True

search_text = ''
input_active = False
search_icon = u'\U0001F50D'


font = pygame.font.Font(None, 74)
grid = [['' for _ in range(cols)] for _ in range(rows)]
chance =  ['O','X']
first_chance = chance[random.randint(0, 1)]

mt = 0
input_box = pygame.Rect(35, 115, 2, 35)
edit_close_rect = pygame.Rect(130, 110, 70, 40)
WHITE = (0, 0, 0)
BLACK = (200, 200, 200)
GRAY = (255, 255, 255)

grey = (220, 220, 220)
light_grey = (240, 240, 240)

color_inactive = GRAY
color_active = WHITE
color = color_inactive
active = False
MAX_CHARS = 7
max_chars = 12
error_message = ''

game_in = 'lobby'
setting_status = 'off'
coins = 500
winner_processed = False
money = 25
level = 1

user_name = ''

change_users = False
change_banners = False

#level increse

xp = 0

player = 'O'
computer = 'X'


edit_screen = False
user_id_digits = [str(random.randint(0, 9)) for _ in range(12)]
user_id = ''.join(user_id_digits)

name = 'player'

search_result = ''

text = name
search_bar = 'off'


def draw_rounded_rect(surface, color, rect, radius):
    x, y, w, h = rect
    pygame.draw.rect(surface, color, (x + radius, y, w - 2 * radius, h))
    pygame.draw.rect(surface, color, (x, y + radius, w, h - 2 * radius))
    pygame.draw.circle(surface, color, (x + radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + w - radius, y + radius), radius)
    pygame.draw.circle(surface, color, (x + radius, y + h - radius), radius)
    pygame.draw.circle(surface, color, (x + w - radius, y + h - radius), radius)

def draw_search_bar():
    global search_text
    # Measure the width of the search text
    text_width = sum(number_font.size(char)[0] for char in search_text)
    
    # Adjust the width of the search bar
    search_bar_width = max(115, text_width + 7)  # Minimum width 100, padding 40

    search_bar_rect = pygame.Rect(20, 70, search_bar_width, 25)
    draw_rounded_rect(screen, light_grey, search_bar_rect, 2)
    pygame.draw.rect(screen, grey, search_bar_rect, 2, border_radius=20)

    # Draw the search text
    x_offset = 25
    for char in search_text:
        char_surface = number_font.render(char, True, black)
        screen.blit(char_surface, (x_offset, 70))
        x_offset += number_font.size(char)[0]



def draw_grid():
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * box_width+10, row * box_height+120, box_width, box_height)
            pygame.draw.rect(screen, black, rect, 1)
            if grid[row][col] == 'O':
                text_rect = o_img.get_rect(center=(col * box_width + box_width // 2+10, row * box_height + box_height // 2+120))
                screen.blit(o_img, text_rect)
                
            if grid[row][col] == 'X':               
                text_rect = x_img.get_rect(center=(col * box_width + box_width // 2+10, row * box_height + box_height // 2+120))
                screen.blit(x_img, text_rect)

def draw_grid_pvc():
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * box_width+10, row * box_height+120, box_width, box_height)
            pygame.draw.rect(screen, black, rect, 1)
            if grid[row][col] == 'O' and chances == 'O':
                text_rect = o_img.get_rect(center=(col * box_width + box_width // 2+10, row * box_height + box_height // 2+120))
                screen.blit(o_img, text_rect)

            if grid[row][col] == 'X' and chances != 'X':
                text_rect = x_img.get_rect(center=(col * box_width + box_width // 2+10, row * box_height + box_height // 2+120))
                screen.blit(x_img, text_rect)
                
            if grid[row][col] == 'X' and chances == 'X':                
                text_rect = x_img.get_rect(center=(col * box_width + box_width // 2+10, row * box_height + box_height // 2+120))
                screen.blit(x_img, text_rect)

            if grid[row][col] == 'O' and chances != 'O':
                text_rect = o_img.get_rect(center=(col * box_width + box_width // 2+10, row * box_height + box_height // 2+120))
                screen.blit(o_img, text_rect)

def get_box_at_pos(pos):
    x, y = pos
    col = (x-10) // box_width
    row = (y-120)// box_height
    return row, col

def draw_restart_button():
    restart_rect = pygame.Rect(115, 450, 100, 50)
    pygame.draw.rect(screen, black, restart_rect, 2)
    text = button_font.render('Restart', True, black)
    text_rect = text.get_rect(center=(restart_rect.x + restart_rect.width // 2, restart_rect.y + restart_rect.height // 2))
    screen.blit(text, text_rect)
    return restart_rect

def draw_play_button():
    play_rect = pygame.Rect(80, 440, 170, 80)
    pygame.draw.rect(screen, black, play_rect, 5)
    text = sylish_font.render("PvP", True, black)
    text_rect = text.get_rect(center=(play_rect.x + play_rect.width // 2, play_rect.y + play_rect.height // 2))
    screen.blit(text, text_rect)
    return play_rect

def draw_pvc():
    play_rect = pygame.Rect(80, 350, 170, 80)
    pygame.draw.rect(screen, black, play_rect, 5)
    text = sylish_font.render("PvC", True, black)
    text_rect = text.get_rect(center=(play_rect.x + play_rect.width // 2, play_rect.y + play_rect.height // 2))
    screen.blit(text, text_rect)
    return play_rect

def draw_setting_button():
    setting_rect = pygame.Rect(10,10, 30, 30)
    pygame.draw.rect(screen, black, setting_rect, 3)
    text_rect = setting_img.get_rect(center=(setting_rect.x + setting_rect.width // 2, setting_rect.y + setting_rect.height // 2))
    screen.blit(setting_img, text_rect)
    return setting_rect

def draw_back_button():
    back_rect = pygame.Rect(10,10, 40, 40)
    pygame.draw.rect(screen, black, back_rect, 3)
    text_rect = back_img.get_rect(center=(back_rect.x + back_rect.width // 2, back_rect.y + back_rect.height // 2))
    screen.blit(back_img, text_rect)
    return back_rect

def draw_coin_button():
    coin_rect = pygame.Rect(50,10,30,30)
    pygame.draw.rect(screen, black,coin_rect, 3)
    text_rect = coin_img.get_rect(center=(coin_rect.x + coin_rect.width // 2, coin_rect.y + coin_rect.height // 2))
    screen.blit(coin_img, text_rect)

def show_coins():
    text = coin_font.render(f'-{coins}',True,black)
    screen.blit(text,(80,7))

def draw_money_button():
    money_rect = pygame.Rect(170,10,30,30)
    pygame.draw.rect(screen, black,money_rect, 3)
    text_rect = money_img.get_rect(center=(money_rect.x + money_rect.width // 2, money_rect.y + money_rect.height // 2))
    screen.blit(money_img, text_rect)

def show_money():
    text = coin_font.render(f'-{money}',True,black)
    screen.blit(text,(200,7))

def draw_profile():
    user_rect = pygame.Rect(20,100,66,66)
    user_banner_rect = pygame.Rect(96,100,100,64)
    pygame.draw.rect(screen, black, user_rect, 3)
    pygame.draw.rect(screen, black, user_banner_rect,18)
    text_img_rect= user_img.get_rect(center=(user_rect.x + user_rect.width // 2 , user_rect.y + user_rect.height // 2))
    text_banner_rect = user_banner.get_rect(center=(user_banner_rect.x + user_banner_rect.width // 2, user_banner_rect.y + user_banner_rect.height // 2))
    screen.blit(user_img, text_img_rect)
    screen.blit(user_banner, text_banner_rect)

def show_profile_data():
    global level
    if xp >= 300 and xp < 600:
        level = 2
    if xp >=600 and xp < 850:
        level = 3
    if xp >= 850 and xp <1050:
        level = 4
    if xp >= 1050 and xp < 1350:
        level = 5
    if xp >= 1350 and xp < 1600:
        level = 6
    if xp >= 1600 and xp < 1900:
        level = 7
    if xp >=1900 and xp < 2300:
        level = 8
    name_rect = pygame.Rect(76, 90, 80, 40)
    level_rect = pygame.Rect(73, 110, 80, 40)
    lev_rect = pygame.Rect(93,110,80,40)
    id_rect = pygame.Rect(103,130,80,40)
    text_name = profile_font.render(name, True, 'white')
    text_level = profile_font.render(f'Level-',True, 'white')
    level_num = number_font.render(f'{level}',True,'white')
    text_id = number_font.render(f'{user_id}',True,'white')
    text_name_rect = text_name.get_rect(center=(name_rect.x + name_rect.width // 2, name_rect.y + name_rect.height//2))
    text_level_rect = text_level.get_rect(center=(level_rect.x + level_rect.width // 2, level_rect.y + level_rect.height//2))
    num_level_rect = level_num.get_rect(center=(lev_rect.x + lev_rect.width // 2, lev_rect.y + lev_rect.height//2))
    text_id_rect = text_id.get_rect(center=(id_rect.x+id_rect.width//2, id_rect.y+id_rect.height//2))
    if not edit_screen:
        screen.blit(text_name,text_name_rect)
        screen.blit(text_level,text_level_rect)
        screen.blit(level_num,num_level_rect)
        screen.blit(text_id,text_id_rect)

def draw_edit_button():
    edit_rect = pygame.Rect(180, 100, 24, 24)
    pygame.draw.rect(screen, 'black', edit_rect, 2)
    text_edit_rect = edit_img.get_rect(center=(edit_rect.x + edit_rect.width // 2, edit_rect.y + edit_rect.height // 2))
    screen.blit(edit_img, text_edit_rect)
    return edit_rect


def draw_settings_screen():
    settings_rect = pygame.Rect(10, 40, 100, 200)
    pygame.draw.rect(screen, (200, 200, 200), settings_rect)
    text = setting_font.render('Settings', True, black)
    screen.blit(text, (20, 50))
    option1_rect = pygame.Rect(20, 80, 80, 30)
    option2_rect = pygame.Rect(20, 120, 80, 30)
    option3_rect = pygame.Rect(20, 160, 80, 30)
    close_rect = pygame.Rect(20, 200, 80, 30)
    pygame.draw.rect(screen, black, option1_rect, 2)
    pygame.draw.rect(screen, black, option2_rect, 2)
    pygame.draw.rect(screen, black, option3_rect, 2)
    pygame.draw.rect(screen, black, close_rect, 2)
    text1 = setting_font.render('Volume +', True, black)
    text2 = setting_font.render('Volume -', True, black)
    text3 = setting_font.render('More', True, black)
    text4 = setting_font.render('Close', True, black)
    screen.blit(text1, (25, 85))
    screen.blit(text2, (25, 125))
    screen.blit(text3, (25, 165))
    screen.blit(text4, (25, 205))
    return settings_rect, option1_rect, option2_rect, close_rect

def check_win():
    global winner
    for row in grid:
        if row[0]==row[1]==row[2] and row[0] != '':
            winner = row[0]
            return True
    for col in range(cols):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != '':
            winner = grid[0][col]
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '':
        winner = grid[0][0]
        return True

    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '':
        winner = grid[0][2]
        return True

    if mt == 9:
        winner = 'draw'

    return False

def restart_game(): 
    global grid, first_chance, winner, mt, winner_processed
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    first_chance = chance[random.randint(0, 1)]
    winner = None
    mt = 0
    winner_processed = False

def play_game():
    global game_in
    game_in = 'play'

def setting():
    global setting_status
    setting_status = 'on'

def back():
    global game_in, grid, first_chance, winner, mt
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    first_chance = chance[random.randint(0, 1)]
    winner = None
    mt = 0
    game_in = 'lobby'


def show_edit_screen():
    global name, profile_img ,profile_banner
    txt_surface = setting_font.render(text, True, black)
    width = max(100, txt_surface.get_width() + 10)
    input_box.w = width
    profile_name_rect = pygame.Rect(20, 90, 230, 140)
    pygame.draw.rect(screen, (200, 200, 200), profile_name_rect)
    pygame.draw.rect(screen, BLACK, edit_close_rect, 2)
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    text_1 = setting_font.render('EDIT:-', True, black)
    text_2 = setting_font.render('Close', True, black)
    text_2_rect = text_2.get_rect(center=(edit_close_rect.x + edit_close_rect.width // 2, edit_close_rect.y + edit_close_rect.height // 2))
    screen.blit(text_1, (25, 95))
    screen.blit(text_2, text_2_rect)
    pygame.draw.rect(screen, color, input_box, 2)

    pygame.draw.rect(screen, black, edit_user_rect, 3)
    pygame.draw.rect(screen, black, edit_user_banner_rect,18)
    text_img_rect= user_img.get_rect(center=(edit_user_rect.x + edit_user_rect.width // 2 , edit_user_rect.y + edit_user_rect.height // 2))
    text_banner_rect = user_banner.get_rect(center=(edit_user_banner_rect.x + edit_user_banner_rect.width // 2, edit_user_banner_rect.y + edit_user_banner_rect.height // 2))
    screen.blit(user_img, text_img_rect)
    screen.blit(user_banner, text_banner_rect)


    show_profile_data()


def restart_cvp():
    global grid, first_chance, winner, mt, won_screen, winner_processed
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    first_chance = chance[random.randint(0, 1)]
    winner = None
    mt = 0
    won_screen = True
    winner_processed = False

def find_winning_move(player):
    # Check rows
    for row in range(rows):
        if grid[row][0] == grid[row][1] == player and grid[row][2] == '':
            return row, 2
        if grid[row][1] == grid[row][2] == player and grid[row][0] == '':
            return row, 0
        if grid[row][0] == grid[row][2] == player and grid[row][1] == '':
            return row, 1
    # Check columns
    for col in range(cols):
        if grid[0][col] == grid[1][col] == player and grid[2][col] == '':
            return 2, col
        if grid[1][col] == grid[2][col] == player and grid[0][col] == '':
            return 0, col
        if grid[0][col] == grid[2][col] == player and grid[1][col] == '':
            return 1, col
    # Check diagonals
    if grid[0][0] == grid[1][1] == player and grid[2][2] == '':
        return 2, 2
    if grid[1][1] == grid[2][2] == player and grid[0][0] == '':
        return 0, 0
    if grid[0][0] == grid[2][2] == player and grid[1][1] == '':
        return 1, 1
    if grid[0][2] == grid[1][1] == player and grid[2][0] == '':
        return 2, 0
    if grid[1][1] == grid[2][0] == player and grid[0][2] == '':
        return 0, 2
    if grid[0][2] == grid[2][0] == player and grid[1][1] == '':
        return 1, 1
    return None

def computer_move():
    available_moves = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '']
    if available_moves:
        move = find_winning_move(player)
        if not move:
            move = find_winning_move(computer)
        if not move:
            empty_cells = [(row, col) for row in range(rows) for col in range(cols) if grid[row][col] == '']
            if empty_cells:
                move = random.choice(empty_cells)
        if move:
            row, col = move
            grid[row][col] = computer


def draw_shop_img():
    shop_rect = pygame.Rect(270, 10, 30, 30)
    pygame.draw.rect(screen, black, shop_rect, 3)
    text_shop_rect = shop_img.get_rect(center=(shop_rect.x + shop_rect.width // 2, shop_rect.y + shop_rect.height // 2))
    screen.blit(shop_img, text_shop_rect)
    return shop_rect

def change_user():
    user_rect = pygame.Rect(30,100,66,66)
    profile_name_rect = pygame.Rect(20, 90, 230, 140)
    pygame.draw.rect(screen, (255, 255, 255), profile_name_rect)
    pygame.draw.rect(screen, black, user_rect, 2)
    pygame.draw.rect(screen, black, user_rect_1, 2)
    pygame.draw.rect(screen, black, user_rect_2, 2)
    pygame.draw.rect(screen, black, user_rect_3, 2)
    pygame.draw.rect(screen, BLACK, edit_close_rect_1, 2)
    pygame.draw.rect(screen, black, dub_user_rect, 2)
    text_close = setting_font.render("Close", True, black)
    text_profile_rect = user_img.get_rect(center=(user_rect.x + user_rect.width // 2, user_rect.y + user_rect.height // 2))
    text_profile_rect_1 = dub_user_1_img.get_rect(center=(user_rect_1.x + user_rect_1.width // 2, user_rect_1.y + user_rect_1.height // 2))
    text_profile_rect_2 = dub_user_2_img.get_rect(center=(user_rect_2.x + user_rect_2.width // 2, user_rect_2.y + user_rect_2.height // 2))
    text_profile_rect_3 = dub_user_3_img.get_rect(center=(user_rect_3.x + user_rect_3.width // 2, user_rect_3.y + user_rect_3.height // 2))
    text_close_rect = text_close.get_rect(center=(edit_close_rect_1.x + edit_close_rect_1.width // 2, edit_close_rect_1.y + edit_close_rect_1.height // 2))
    text_dub_rect = dub_user_img.get_rect(center=(dub_user_rect.x + dub_user_rect.width // 2, dub_user_rect.y + dub_user_rect.height // 2))
    screen.blit(user_img, text_profile_rect)
    screen.blit(dub_user_1_img, text_profile_rect_1)
    screen.blit(dub_user_2_img, text_profile_rect_2)
    screen.blit(dub_user_3_img, text_profile_rect_3)
    screen.blit(text_close, text_close_rect)
    screen.blit(dub_user_img, text_dub_rect)

def change_banner():
    profile_name_rect = pygame.Rect(20, 90, 230, 140)
    pygame.draw.rect(screen, (255, 255, 255), profile_name_rect)
    pygame.draw.rect(screen, black, edit_user_banner_rect_1, 2)
    pygame.draw.rect(screen, black, banner_rect_1, 2)
    pygame.draw.rect(screen, black, banner_rect_2, 2)
    pygame.draw.rect(screen, black, dub_banner_rect, 2)
    text_close = setting_font.render("Close", True, black)
    text_dub_banner_rect = dub_banner.get_rect(center=(dub_banner_rect.x + dub_banner_rect.width // 2, dub_banner_rect.y + dub_banner_rect.height // 2))
    text_banner_rect = user_banner.get_rect(center=(edit_user_banner_rect_1.x + edit_user_banner_rect_1.width // 2, edit_user_banner_rect_1.y + edit_user_banner_rect_1.height // 2))
    text_banner_rect_1 = dub_banner_1.get_rect(center=(banner_rect_1.x + banner_rect_1.width // 2, banner_rect_1.y + banner_rect_1.height // 2))
    text_banner_rect_2 = dub_banner_2.get_rect(center=(banner_rect_2.x + banner_rect_2.width // 2, banner_rect_2.y + banner_rect_2.height // 2))    
    text_close_rect = text_close.get_rect(center=(edit_close_rect_2.x + edit_close_rect_2.width // 2, edit_close_rect_2.y + edit_close_rect_2.height // 2))
    screen.blit(user_banner, text_banner_rect)
    screen.blit(dub_banner_1, text_banner_rect_1)
    screen.blit(dub_banner_2, text_banner_rect_2)
    screen.blit(text_close, text_close_rect)
    screen.blit(dub_banner, text_dub_banner_rect)

def draw_search():
    search_rect = pygame.Rect(140, 70, 25, 25)
    pygame.draw.rect(screen, 'white', search_rect, 2)
    text_search = search_img.get_rect(center=(search_rect.x + search_rect.width // 2 , search_rect.y + search_rect.height // 2))
    screen.blit(search_img, text_search)
    return search_rect

def search():
    global user_name
    pass

def check_even():
    global coins, winner_processed, xp
    if winner == 'O' and not winner_processed:
        if level == 1:
            xp += 100
        elif level ==2:
            xp += 90
        elif level == 3:
            xp += 85
        elif level == 4:
            xp += 80
        elif level == 5:
            xp += 75
        elif level == 6 or level == 7 or level == 8:
            xp += 70
        elif level == 9 or level == 10 or level == 11 or level == 12 or level == 13 or level == 14 or level == 15 or level == 16:
            xp += 65
        elif level == 17 or level == 18 or level == 19 or level == 20 or level == 21 or level == 22 or level == 23 or level == 24 or level == 25:
            xp += 60
        elif level == 26 or level == 27 or level == 28 or level == 29 or level == 30 or level == 31 or level == 32 or level == 33 or level == 34 or level == 35:
            xp += 55
        else :
            xp +=50

        coins += 100
        winner_processed = True
    rect = pygame.Rect(115, 245, 100, 50)
    pygame.draw.rect(screen, black, rect, 2)
    rect_1 = pygame.Rect(0, 230, 400, 100)
    pygame.draw.rect(screen, (0, 255, 0), rect_1)
    text = sylish_font.render("You Win", True, black)
    rect_text = text.get_rect(center=(rect.x + rect.width //2, rect.y + rect.height // 2))
    screen.blit(text, rect_text)

def won_money():
    global won_screen, ok_rect
    if won_screen and winner == 'O':
        won_text = message_font.render("You Won Hundred Coins!", True, black)
        ok_text = message_font.render("OK", True, black)
        won_rect = pygame.Rect(45, 245, 250, 50)
        won_rect_1 = pygame.Rect(45, 245, 250, 80)
        pygame.draw.rect(screen, (255, 0, 0), won_rect_1)
        pygame.draw.rect(screen, (0, 255, 255), ok_rect)
        won_text_rect = won_text.get_rect(center=(won_rect.x + won_rect.width //2, won_rect.y + won_rect.height // 2))
        ok_text_rect = ok_text.get_rect(center=(ok_rect.x + ok_rect.width // 2, ok_rect.y + ok_rect.height // 2))
        screen.blit(won_text, won_text_rect)
        screen.blit(ok_text, ok_text_rect)
        

def ok():
    global won_screen
    won_screen = False

def check_odd():
    global coins, winner_processed
    if winner == 'X' and not winner_processed:
        coins = coins - 50
        winner_processed = True
    rect = pygame.Rect(115, 245, 100, 50)
    pygame.draw.rect(screen, black, rect, 2)
    rect_1 = pygame.Rect(0, 230, 400, 100)
    pygame.draw.rect(screen, (255, 0, 0), rect_1)
    text = sylish_font.render("You Lost", True, black)
    rect_text = text.get_rect(center=(rect.x + rect.width //2, rect.y + rect.height // 2))
    screen.blit(text, rect_text)


while run:
    screen.fill((255, 255, 255))
    if game_in == 'lobby':
        screen.blit(lobby_img,(0, 0))
        draw_play_button()
        draw_coin_button()
        show_coins()
        draw_money_button()
        show_money()
        draw_profile()
        show_profile_data()
        draw_edit_button()
        draw_pvc()
        draw_shop_img()
        draw_search_bar()
        draw_search()
        setting_rect = draw_setting_button()
        if setting_status == 'on':
            settings_rect, option1_rect, option2_rect,close_rect =  draw_settings_screen()
        if edit_screen:
            show_edit_screen()
        if change_users:
            change_user()
        if change_banners:
            change_banner()
        if winner_processed:
            won_money()
        search_bar = 'on'

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            restart_rect = draw_restart_button()
            play_rect = draw_play_button()
            setting_rect = draw_setting_button()
            settings_rect, option1_rect, option2_rect,close_rect= draw_settings_screen()
            back_rect = draw_back_button()
            edit_rect = draw_edit_button()
            com_rect = draw_pvc()
            shop_rect = draw_shop_img()
            search_bar_rect = draw_search_bar()
            search_rect = draw_search()
            pos = pygame.mouse.get_pos()
            row, col = get_box_at_pos(pos)
            if game_in == 'play':
                if 0 <= row < rows and 0 <= col < cols:
                    if grid[row][col] == '' and winner is None:
                        mt = mt+1
                        grid[row][col] = first_chance
                        first_chance = 'X' if first_chance == 'O' else 'O'
                if restart_rect.collidepoint(pos):
                    restart_game()
                if back_rect.collidepoint(pos):
                    back()
            
            if game_in == 'lobby':
                if setting_rect.collidepoint(pos):
                    setting()
                if edit_rect.collidepoint(pos):
                    edit_screen = True
                if play_rect.collidepoint(pos):
                    play_game()
                if com_rect.collidepoint(pos):
                    game_in = 'PvC'
                    won_screen = True
                    winner_processed = False
                if input_box.collidepoint(pos):
                    active = not active
                    text = ''
                else:
                    active = False
                color = color_active if active else color_inactive
                if edit_close_rect.collidepoint(pos):
                    if edit_screen:
                        edit_screen = False
                if edit_user_rect.collidepoint(pos):
                    change_users = True
                if edit_user_banner_rect.collidepoint(pos):
                    change_banners = True
                if setting_status == 'on':
                    if option1_rect.collidepoint(pos):
                        print('Option 1 clicked')
                    if option2_rect.collidepoint(pos):
                        print('Option 2 clicked')
                    if close_rect.collidepoint(pos):
                        setting_status = 'off'
                if user_rect_1.collidepoint(pos):
                    if change_users:
                        profile_img = 'data/user_1.png'
                        user_img = pygame.image.load(profile_img)
                if user_rect_2.collidepoint(pos):
                    if change_users:
                        profile_img = 'data/user_2.png'
                        user_img = pygame.image.load(profile_img)
                if user_rect_3.collidepoint(pos):
                    if change_users:
                        profile_img = 'data/user_3.png'
                        user_img = pygame.image.load(profile_img)
                if dub_user_rect.collidepoint(pos):
                    if change_users:
                        profile_img = 'data/user.png'
                        user_img = pygame.image.load(profile_img)
                if banner_rect_1.collidepoint(pos):
                    if change_banners:
                        profile_banner = 'data/banner_1.png'
                        user_banner = pygame.image.load(profile_banner)
                if banner_rect_2.collidepoint(pos):
                    if change_banners:
                        profile_banner = 'data/banner_2.png'
                        user_banner = pygame.image.load(profile_banner)
                if dub_banner_rect.collidepoint(pos):
                    if change_banners:
                        profile_banner = 'data/profile_banner.png'
                        user_banner = pygame.image.load(profile_banner)
                if edit_close_rect_1.collidepoint(pos):
                    if change_users:
                        change_users = False
                if edit_close_rect_2.collidepoint(pos):
                    if change_banners:
                        change_banners = False
                if shop_rect.collidepoint(pos):
                    game_in = 'shop'
                if search_rect.collidepoint(pos):
                    search()
                if pygame.Rect(20, 70, max(100, sum(font.size(char)[0] if not char.isdigit() else number_font.size(char)[0] for char in search_text) + 40), 30).collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
                if ok_rect.collidepoint(pos):
                    ok()
            if game_in == 'PvC':
                if winner is None:
                    if 0 <= row < rows and 0 <= col < cols:
                        if grid[row][col] == '' and first_chance == player:
                            grid[row][col] = player
                        first_chance = computer
                        mt = mt+1
                if check_win():
                    show_winner_img = sylish_font.render(f'{winner} Winner', True, black)
                    screen.blit(show_winner_img,(60, 40))
                elif winner == 'draw':
                    show_draw_img = sylish_font.render(f'DRAW', True, black)
                    screen.blit(show_draw_img, (50, 30))
                if winner == 'O':
                    check_even()
                if winner == 'X':
                    check_odd()

                if back_rect.collidepoint(pos):
                    back()
                if restart_rect.collidepoint(pos):
                    restart_cvp()
                
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    if len(text) <= 7:
                        name = text
                        text = 'Saved'
                        error_message = ''
                    else:
                        error_message = 'Minimum seven characters required.'
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    error_message = ''
                else:
                    if len(text) <= MAX_CHARS:
                        text += event.unicode
                        error_message = ''
                    else:
                        error_message = 'Only seven characters allowed.'
            if input_active:
                if event.key == pygame.K_BACKSPACE:
                    search_text = search_text[:-1]
                    user_name = ''
                elif event.key == pygame.K_RETURN:
                    if search_text in id_dict:
                        user_name = id_dict[search_text]
                    else:
                        user_name = ''
                elif event.unicode.isdigit() and len(search_text) < max_chars:
                    search_text += event.unicode

    if game_in == 'lobby':
        if user_name:
            name_surface = setting_font.render(f'{user_name}', True, black)
            screen.blit(name_surface, (100, 250))
    if error_message:
        error_surface = setting_font.render(error_message, True, black)
        screen.blit(error_surface, (input_box.x, input_box.y + input_box.height))
        if not edit_screen:
            error_message = ''

    if game_in == 'play':
        screen.blit(bg_img, (0, 200))
        screen.blit(bg_img, (0, 0))
        if winner is None:
            show_chance_img = sylish_font.render(f"'{first_chance}' Turn", True, black)
            screen.blit(show_chance_img, (50, 30))
        elif winner == 'draw':
            show_draw_img = sylish_font.render(f'DRAW', True, black)
            screen.blit(show_draw_img, (50, 30))
        if check_win():
            show_winner_img = sylish_font.render(f'{winner} Winner', True, black)
            screen.blit(show_winner_img,(60, 40))
        draw_grid()
        draw_restart_button()
        draw_back_button()

    if game_in == 'PvC':
        screen.blit(bg_img, (0, 200))
        screen.blit(bg_img, (0, 0))
        if winner is None and first_chance == computer:
            computer_move()
            first_chance = player
            mt = mt+1

        if winner is None:
            show_chance_img = sylish_font.render(f"'{first_chance}' Turn", True, black)
            screen.blit(show_chance_img, (50, 30))
        elif winner == 'draw':
            show_draw_img = sylish_font.render(f'DRAW', True, black)
            screen.blit(show_draw_img, (50, 30))
        if check_win():
            show_winner_img = sylish_font.render(f'{winner} Winner', True, black)
            screen.blit(show_winner_img,(60, 40))
        draw_grid()
        if winner == 'O':
            check_even()
        if winner == 'X':
            check_odd()
        draw_restart_button()
        draw_back_button()

    if game_in == 'shop':
        print('game in shop')

    pygame.display.update()
    

pygame.quit()
