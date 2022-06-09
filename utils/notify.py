#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 4:10 下午
# @File    : notify.py
# @Project : jd_scripts
# @Desc    : 通知模块
import telegram
from config import TG_BOT_TOKEN, TG_USER_ID
from utils.console import println
from utils.logger import logger


def notify(message):
    """
    消息推送
    :param message:
    :return:
    """
    if TG_BOT_TOKEN and TG_USER_ID:
        try:
            bot = telegram.Bot(TG_BOT_TOKEN)
            bot.send_message(TG_USER_ID, message)
            println('\n成功推送消息到TG!')
        except Exception as e:
            logger.info('TG通知异常:{}'.format(e.args))
            println('\nTG消息通知异常!')
    else:
        println("\n未配置TG_BOT_TOKEN和TG_USER_ID, 不推送TG消息...")

    # 更多推送方式
