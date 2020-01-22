import os,time,sys,signal, subprocess
from colorama import Fore, Back, Style , init
from getch import _Getch
from config import config
from grid import grid
from mandalorian import mandalorian
from stats import stats
from coins import coins
from extraFunctions import *
from bullet import bullet
from magnet import magnet
from obstacles import obstaclesH,obstaclesV,obstaclesD1,obstaclesD2
from dragon import dragon,bulletd
from speed import speed
from random import randint
from math import floor

def alarmhandler():
    raise TimeOutException("alarm went off")

def Pesudoalarmhandler():
    return

def uinput(timeout):
    try:
        starttime = time.time()
        signal.setitimer(signal.ITIMER_REAL,timeout,0)
        command = _Getch()()
        if ((timeout - (time.time() - starttime)) - 0.001) > 0:
            time.sleep((timeout - (time.time() - starttime)) - 0.001)
        signal.alarm(0)
        return command
    except:
        for i in range(100):
            print(Back.BLACK + " ",end="")
        pass


signal.signal(signal.SIGALRM,alarmhandler)
os.system('clear')
os.system("stty -echo")
Coins = []
Obstacles = []
Config = config()
Stats = stats()
game_grid = grid(Config.dimensions()[0],Config.dimensions()[1])
Hero = mandalorian(Config.dimensions()[0],Config.dimensions()[1]-30)
i = 0
t = time.time()
lt = t
st = t - 60
slt = 0
Bullet = []
Magnet = []
Speed = None
# mag = randint(200,Config.length())
mag = randint(200,300)
while Stats.GetDistance() + Hero.GetPos()[0] < Config.length():
    flag = 0
    cmove(Config.dimensions()[0]+6,0)
    command = uinput(1/Config.framerate())
    cmove(0,0)
    if command is 'q' or command is 'Q':
        exit()
    elif command is ' ' and time.time() - lt > 4 and Stats.GetScore() + Stats.GetDistance()+Hero.GetPos()[0] < Config.winCond():
        Bullet.append(bullet(Hero))
        lt = time.time()
    elif (command is 'e' or command is 'E') and time.time() - st > 60:
        Hero.ActivatShield()
        st = time.time()
    else:
        Hero.MoveMandalorian(command)

    if (i+10)%20 == 0 and Stats.GetScore() + Stats.GetDistance()+Hero.GetPos()[0] < Config.winCond():
        x = randint(1,4)
        if x%4 == 0:
            Obstacles.append(obstaclesH(Config.dimensions()[0]-4))
        elif x%4 == 1:
            Obstacles.append(obstaclesD1(Config.dimensions()[0]-4))
        elif x%4 == 2:
            Obstacles.append(obstaclesD2(Config.dimensions()[0]-4))
        else:
            Obstacles.append(obstaclesV(Config.dimensions()[0]-4))

    for l in Obstacles:
        l.MoveLeft()
        if l.GetPos()[1] < -13:
            Obstacles.remove(l)
            continue
        if l.Overlap(Hero):
            flag = 1
            Obstacles.remove(l)
        l.AddObject(game_grid)

    if (i+1)%300 == 0 and Stats.GetScore() + Stats.GetDistance()+Hero.GetPos()[0] < Config.winCond():
        Speed = speed(Config.dimensions()[0]-4)
        for l in Coins:
            if l.Overlap(Speed):
                Speed = None
        for l in Obstacles:
            if l.Overlap(Speed):
                Speed = None

    if not Speed:
        pass
    else:
        for l in Coins:
            if l.Overlap(Speed):
                Speed = None
        if not Speed:
            pass
        for l in Obstacles:
            if l.Overlap(Speed):
                Speed = None
        if not Speed:
            pass
        if Speed.GetPos()[1] < 0:
            Speed = None
        if not Speed:
            pass
        else:
            Speed.MoveLeft()
            if Hero.Overlap(Speed):
                Speed = None
                slt = time.time()
            else:
                Speed.AddObject(game_grid)

    if time.time() - slt < 10:
        Config.incframerate()
    else:
        Config.decframerate()

    if i%20 == 0 and Stats.GetScore() + Stats.GetDistance()+Hero.GetPos()[0] < Config.winCond():
        Coins.append(coins(Config.dimensions()[0]-4))

    for l in Coins:
        l.MoveLeft()
        if l.GetPos()[1] <= 0:
            Coins.remove(l)
            continue
        if l.Overlap(Hero):
            Stats.UpdateScore()
            Coins.remove(l)
            continue
        klflag = 0
        for k in Obstacles:
            if k.Overlap(l):
                klflag = 1
                Coins.remove(l)
        if i%3 is 0 or klflag == 1:
            continue
        else:
            l.AddObject(game_grid)

    for l in Bullet:
        l.MoveRight()
        if l.GetPos()[1] > Config.dimensions()[1]- 30:
            Bullet.remove(l)
            continue
        for k in Obstacles:
            if l.Overlap(k):
                Stats.UpdateScore()
                Obstacles.remove(k)
                Bullet.remove(l)
                break
        l.AddObject(game_grid)

    if not Magnet and i == mag:
        Magnet.append(magnet())

    for l in Magnet:
        l.MoveLeft()
        if l.GetPos()[1] <= 0:
            Magnet.remove(l)
        if l.GetPos()[1] > Hero.GetPos()[1] and l.GetPos()[1] < 100:
            Hero.MoveRight()
        if l.GetPos()[1] < Hero.GetPos()[1] and l.GetPos()[1] < 100:
            Hero.MoveLeft()
        l.AddObject(game_grid)

    Hero.AddObject(game_grid)
    game_grid.printgrid()
    game_grid.ClearGrid()
    cmove(Config.dimensions()[0]+5,0)
    Stats.UpdateDistance()
    print("SCORE :" + str(Stats.GetScore() + Stats.GetDistance()+Hero.GetPos()[0]) + "   Lives :" + str(Stats.GetLives()) + "   Time Left :" + str(floor(Config.time() - (time.time() - t))))
    i = i + 1
    if flag == 1 and time.time() - st > 10:
        Stats.UpdateLives()
    if time.time() - st > 10:
        Hero.DeactivateShield()
    if Stats.GetLives() <= 0 or (time.time() - t) > Config.time():
        cmove(Config.dimensions()[0]+3,0)
        print('\t\t\t\t\t  Game Over!!!')
        exit()
    if Stats.GetScore() + Stats.GetDistance()+Hero.GetPos()[0] > Config.winCond() and not Obstacles and not Coins :
        break
cmove(Config.dimensions()[0]/2,0)
print("\t\t\t\t\t  Boss Level")
time.sleep(3)
BossHP = 10
drag = dragon(Config.dimensions()[0])
Bulletd = []
Hero.BossLevel()
i = 0
lt = time.time()
while time.time() - t < Config.time() and BossHP > 0:
    cmove(Config.dimensions()[0]+6,0)
    command = uinput(1/Config.framerate())
    cmove(0,0)
    if command is 'q' or command is 'Q':
        exit()
    elif command is ' ' and time.time() - lt > 0.3:
        lt = time.time()
        Bullet.append(bullet(Hero))
    else:
        Hero.MoveMandalorian(command)

    drag.MoveDrag(Hero)
    drag.AddObject(game_grid)
    Hero.AddObject(game_grid)

    for l in Bullet:
        l.MoveRight()
        if l.GetPos()[1] > Config.dimensions()[1]- 30:
            Bullet.remove(l)
            continue
        if l.Overlap(drag):
            Bullet.remove(l)
            BossHP = BossHP - 1
            continue
        l.AddObject(game_grid)

    if (i+1)%10 == 0:
        Bulletd.append(bulletd(drag))

    for l in Bulletd:
        falg = 0
        for k in Bullet:
            if l.GetPos()[0] == k.GetPos()[0] and l.GetPos()[1] == k.GetPos()[1] - 38:
                Bulletd.remove(l)
                Bullet.remove(k)
                flag = 1
                break
        if flag == 1:
            continue

    for l in Bulletd:
        l.MoveLeft()
        if l.GetPos()[1] < 0:
            Bulletd.remove(l)
            continue
        if l.Overlap(Hero):
            Stats.UpdateLives()
            Bulletd.remove(l)
        l.AddObject(game_grid)

    game_grid.printgrid()
    game_grid.ClearGrid()
    if Stats.GetLives() <= 0 or (time.time() - t) > Config.time():
        cmove(Config.dimensions()[0]+3,0)
        print('\t\t\t\t\t  Game Over!!!')
        exit()
    cmove(Config.dimensions()[0]+5,0)
    print("SCORE :" + str(Stats.GetScore() + Stats.GetDistance()) + "Lives :" + str(Stats.GetLives()) + "   Time Left :" + str(floor(Config.time() - (time.time() - t))) + "  Boss Lives :" + str(BossHP))
    i = i+1

cmove(Config.dimensions()[0]+3,0)
print('\t\t\t\t\t  You Win!!!')
exit()
