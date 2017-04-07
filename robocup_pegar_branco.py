#!/usr/bin/env python3

import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from time   import sleep

m_esquerdo = ev3.LargeMotor('outA')
m_direito = ev3.LargeMotor('outB')
m_garra = ev3.Motor('outC')
cl = ev3.ColorSensor('in1')
cl.mode='COL-AMBIENT'
tempo_voltar = 0

while cl.value() > 4:
    m_esquerdo.run_timed(time_sp=100, speed_sp=-600, stop_action='brake')
    m_direito.run_timed(time_sp=100, speed_sp=-600, stop_action='brake')
    m_esquerdo.wait_while('running')
    m_direito.wait_while('running')
    tempo_voltar += 100

m_garra.run_timed(time_sp=700, speed_sp=500, stop_action='brake')
m_garra.wait_while('running')
sleep(3)
cl.mode='COL-COLOR'
sleep(3)

if cl.value() == 6:
    ev3.Sound.beep()
    m_garra.run_timed(time_sp=800, speed_sp=500, stop_action='brake')
    m_garra.wait_while('running')
    m_esquerdo.run_timed(time_sp=tempo_voltar, speed_sp=500, stop_action='brake')
    m_direito.run_timed(time_sp=tempo_voltar, speed_sp=500,  stop_action='brake')
    m_esquerdo.wait_while('running')
    m_direito.wait_while('running')
    m_garra.run_timed(time_sp=1500, speed_sp=-500, stop_action='brake')
    m_garra.wait_while('running')

elif cl.value() == 0 or cl.value() == 1:
    ev3.Sound.speak('Welcome to the E V 3 dev project!').wait()
    m_garra.run_timed(time_sp=600, speed_sp=500, stop_action='brake')
    m_garra.wait_while('running')
    m_esquerdo.run_timed(time_sp=3000, speed_sp=-500, stop_action='brake')
    m_direito.run_timed(time_sp=500, speed_sp=-500, stop_action='brake')
    m_esquerdo.wait_while('running')
    m_direito.wait_while('running')
    m_garra.run_timed(time_sp=1500, speed_sp=-500, stop_action='brake')
    m_garra.wait_while('running')
    m_esquerdo.run_timed(time_sp=3000, speed_sp=500, stop_action='brake')
    m_direito.run_timed(time_sp=500, speed_sp=500, stop_action='brake')
    m_esquerdo.wait_while('running')
    m_direito.wait_while('running')
    m_esquerdo.run_timed(time_sp=tempo_voltar, speed_sp=500, stop_action='brake')
    m_direito.run_timed(time_sp=tempo_voltar, speed_sp=500, stop_action='brake')

