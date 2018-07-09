#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by @sevadinator


"""Simple Bot to send timed Telegram messages.
# This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot and the JobQueue to send
timed messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Time Remaining Bot , sends a message after a called function.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler
import logging

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

#Cálculo de días
def dias_restantes(dia, mes, anno):
    d=7
    m=12
    a=2018
    dd=0
    m30=[9,11]
    m31=[7,8,10,12]
    if dia >= d and mes == m or anno > a:
        return "SSBU ya está disponible!"
    if mes in m30:
        dd=30-dia
    elif mes in m31:
        dd=31-dia
    else:
        return "Error: mes inválido (1)"
    ma=mes+1
    while ma < m:
        if ma in m30:
            dd+=30
        elif ma in m31:
            dd+=31
        else:
            return "Error (2)"
        ma+=1
    dd+=7
    return "Quedan "+str(dd)+" días para SSBU!"

def meses_restantes(dias):
    dia=float(dias)
    meses=(dia*12.0)/365.0
    return meses

def start(bot, update):
    update.message.reply_text('Hola! Usa /dias o /meses para mostrar cuanto tiempo queda para el lanzamiento de SSBU')


def alarm(bot, job):
    """Mensaje de alarma"""
    bot.send_message(job.context, text='SSBU ya está disponible!')

#Fecha Actual
def hoy():
    import time
    fechaa = time.strftime("%d/%m/%y")
    date = fechaa.split("/")
    return date

def set_timer(bot, update, args, job_queue, chat_data):

    chat_id = update.message.chat_id
    
    #Ordenamiento de datos
    lista=hoy()
    dia=lista[0]
    mes=lista[1]
    anno=lista[2]
    texto=dias_restantes(int(dia), int(mes), int(anno))

    #Respuesta
    update.message.reply_text(texto)

def set_timer2(bot, update, args, job_queue, chat_data):

    chat_id = update.message.chat_id
    
    #Ordenamiento de datos
    lista=hoy()
    dia=lista[0]
    mes=lista[1]
    anno=lista[2]
    textopro=dias_restantes(int(dia), int(mes), int(anno))
    incom=textopro.split()
    texto1=meses_restantes(incom[1])
    texto="Quedan "+str(texto1)+" meses para SSBU"

    #Respuesta
    update.message.reply_text(texto)

def waaa(bot, update, chat_data):
    update.message.reply_text('Waa... :c')


def error(bot, update, error):
    """Errores de log causados por Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Correr el bot"""
    updater = Updater("612451037:AAE_UEhsDXqFUgjNDfFaIDcE7pqBQ9jHo8g")

    #registro de handlers por dispatcher
    dp = updater.dispatcher

    # a diferentes comandos - responde en Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("dias", set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("meses", set_timer2,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    #Easter Eggs
    dp.add_handler(CommandHandler("waluigi", waaa, pass_chat_data=True))

    #Log de todos los errores
    dp.add_error_handler(error)

    #Inicio del bot
    updater.start_polling()

    # Blockeo con Ctrl-C o errores de TIMEOUT.
    updater.idle()


if __name__ == '__main__':
    main()

input()
