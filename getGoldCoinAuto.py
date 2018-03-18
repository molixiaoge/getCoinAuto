# coding: utf-8
# 
import os
import logging
from random import uniform
from time import sleep

device_x, device_y = 1920, 1080

logging.basicConfig(format='%(asctime)s %(message)s',
					datefmt='%m/%d/%Y %I:%M:%S %p',
					level=logging.DEBUG)

def tap_screen(pos):
	base_x, base_y = 1920, 1080
	x = int(float(pos[0]) / base_x * device_x + uniform(0, 10) - 5)
	y = int(float(pos[1]) / base_y * device_y + uniform(0, 10) - 5)
	os.system("adb shell input tap {} {}".format(x, y))


autoPos = [1780, 40]
skipPos = [1720, 80]
againPos = [1600, 980]
startPos = [1600, 970]
continuePos = [960, 540]

def work(times):
	logging.debug('第1次刷副本...')
	logging.debug('点击闯关按钮...')
	tap_screen(startPos)
	sleep(15)

	logging.debug('点击跳过按钮...')
	tap_screen(skipPos)
	sleep(2)

	logging.debug('点击自动按钮...')
	tap_screen(autoPos)
	sleep(65)

	logging.debug('点击跳过按钮...')
	tap_screen(skipPos)
	sleep(10)

	logging.debug('点击跳过按钮...')
	tap_screen(skipPos)
	sleep(7)

	logging.debug('点击任意处继续...')
	tap_screen(continuePos)
	sleep(5)

	for i in xrange(1, times):
		logging.debug('第{}次刷副本...'.format(i+1))
		logging.debug('点击再次挑战按钮...')
		tap_screen(againPos)
		sleep(3)

		logging.debug('点击闯关按钮...')
		tap_screen(startPos)
		sleep(15)

		logging.debug('点击跳过按钮...')
		tap_screen(skipPos)
		sleep(2)

		logging.debug('点击自动按钮...')
		tap_screen(autoPos)
		sleep(65)

		logging.debug('点击跳过按钮...')
		tap_screen(skipPos)
		sleep(10)

		logging.debug('点击跳过按钮...')
		tap_screen(skipPos)
		sleep(5)

		logging.debug('点击任意处继续...')
		tap_screen(continuePos)
		sleep(3)


if __name__ == '__main__':
	work(20)
	
		