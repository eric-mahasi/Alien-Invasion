import pygame
from alien import Alien
import game_functions as gf
from ship import Ship
from settings import Settings
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def rungame():
    # Initialize game,settings and create screen object
    pygame.init()
    sett=Settings()    
    screen=pygame.display.set_mode((sett.screen_width,sett.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    """"Instance initialization"""
    #make instance of game stats
    stats=GameStats(sett)
    #Make instance of scoreboard
    sb=ScoreBoard(sett,screen,stats)
    #Make the play button
    b_play=Button(sett,screen,"PLAY")
    
    #make instance of ship
    ship=Ship(sett,screen)
    #make a group to store bullets and aliens
    aliens=Group()
    bullets=Group()
    #make instance of alien
    alien=Alien(sett,screen)
    gf.create_fleet(sett,screen,ship,aliens)
    
    
    #start the main loop for the game
    while True:
        #watch for keyboard and mouse events
        gf.check_events(sett,screen,stats,sb,b_play,ship,aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(sett,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(sett,stats,sb,screen,ship,aliens,bullets)

        #Redraw the screen during each pass through the loop
        gf.update_screen(sett,screen,stats,sb,ship,aliens,bullets,b_play)
        
        
rungame()
