import vk_api, vk
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import requests
import urllib3
from threading import Thread
import asyncio
import aiohttp
import re
import aiosqlite as sql
from bs4 import BeautifulSoup
import datetime
import socket
import json

vk_session = vk_api.VkApi(token='vk1.a.fW6xhIXyLDwog_FX1fRTMiyEoVZL_b0ENm2J4y5lBKZ0hefDhJylNknLzd4I72GJ6--1rNhspg41efbhbJYPX1osNLmRCi9QBKo5v2AhBszehAZKPFUCby-7EeOkHOXXl_2Cp6Z8-0Hqo3yU9FF-B5811qznwiJq-uFEq_rOmUXkHde-9RvMTvm_T4WyFFNWsCd1baqaZA1mwaB69y9TSg')
longpoll = VkBotLongPoll(vk_session, '218320118')
vk = vk_session.get_api()
reminder = []
week = 11111
week_correct = "0"
list_week=["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье"]
list_week = {
    "понедельник":0,
    "вторник":1,
    "среда":2,
    "четверг":3,
    "пятница":4,
    "суббота":5,
    "воскресенье":6
    }
lesson_type = {
            "lesson-color-type-1" : "📗",
            "lesson-color-type-2" : "📘",
            "lesson-color-type-3" : "📕",
            "lesson-color-type-4" : "📙"
            }

def send(message, id):
    vk.messages.send(
        key=('f25124946931a230031d57ddd73e4e0efcec4b7b'),  # ВСТАВИТЬ ПАРАМЕТРЫ
        server=('https://lp.vk.com/wh218320118'),
        ts=('42'),
        random_id=get_random_id(),
        message=message,
        chat_id=id,
    )
with open("instract.txt", "r") as f:
    instruct = f.read()
#print(instruct)

async def timetable(url, weekday, event):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        ans = await response.text()
    soup = BeautifulSoup(ans, 'html.parser')
    a = soup.find_all('div', class_='schedule__item')
    b = soup.find_all('div', class_='schedule__time-item')
    ###################################################################################
    # c = soup.find_all("div", {"class": "schedule__discipline"})
    # print("=====", a)
    # for i in c:
    #     print(i["class"][-1])
    #print("------>",c["class"][-1])
    ##################################################################################
    if b != []:
        timetable = []
        clock = []
        for i in b:
            clock.append(i.text)
        for i in a:
            timetable.append(i.text)
        str_timetable = ""
        #print("====>", type(weekday), "and", weekday)
        if weekday < 6:
            if len(timetable) == 49:
                if timetable[weekday + 7] == timetable[weekday + 13] == timetable[weekday + 19] == timetable[
                    weekday + 25] == timetable[weekday + 31] == timetable[weekday + 37] == timetable[
                    weekday + 343] == "":
                    str_timetable = "Кайфуем))\nПар нет"
                else:
                    str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[weekday + 7] + '\n\n' + \
                                    clock[2] + " - " + clock[3] + '\n' + timetable[weekday + 13] + '\n\n' + \
                                    clock[4] + " - " + clock[5] + '\n' + timetable[weekday + 19] + '\n\n' + \
                                    clock[6] + " - " + clock[7] + '\n' + timetable[weekday + 25] + '\n\n' + \
                                    clock[8] + " - " + clock[9] + '\n' + timetable[weekday + 31] + '\n\n' + \
                                    clock[10] + " - " + clock[11] + '\n' + timetable[weekday + 37] + '\n\n' + \
                                    clock[12] + " - " + clock[13] + '\n' + timetable[weekday + 43] + '\n\n'
                weekday = timetable[weekday + 1]
            if len(timetable) == 43:
                if timetable[weekday + 7] == timetable[weekday + 13] == timetable[weekday + 19] == timetable[
                    weekday + 25] == timetable[weekday + 31] == timetable[weekday + 37] == "":
                    str_timetable = "Кайфуем))\nПар нет"
                else:
                    str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[weekday + 7] + '\n\n' + \
                                    clock[2] + " - " + clock[3] + '\n' + timetable[weekday + 13] + '\n\n' + \
                                    clock[4] + " - " + clock[5] + '\n' + timetable[weekday + 19] + '\n\n' + \
                                    clock[6] + " - " + clock[7] + '\n' + timetable[weekday + 25] + '\n\n' + \
                                    clock[8] + " - " + clock[9] + '\n' + timetable[weekday + 31] + '\n\n' + \
                                    clock[10] + " - " + clock[11] + '\n' + timetable[weekday + 37] + '\n\n'
                weekday = timetable[weekday + 1]
            if len(timetable) == 37:
                if timetable[weekday + 7] == timetable[weekday + 13] == timetable[weekday + 19] == timetable[
                    weekday + 25] == timetable[weekday + 31] == "":
                    str_timetable = "Кайфуем))\nПар нет"
                else:
                    str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[weekday + 7] + '\n\n' + \
                                    clock[2] + " - " + clock[3] + '\n' + timetable[weekday + 13] + '\n\n' + \
                                    clock[4] + " - " + clock[5] + '\n' + timetable[weekday + 19] + '\n\n' + \
                                    clock[6] + " - " + clock[7] + '\n' + timetable[weekday + 25] + '\n\n' + \
                                    clock[8] + " - " + clock[9] + '\n' + timetable[weekday + 31] + '\n\n'
                weekday = timetable[weekday + 1]
            if len(timetable) == 31:
                if timetable[weekday + 7] == timetable[weekday + 13] == timetable[weekday + 19] == timetable[
                    weekday + 25] == "":
                    str_timetable = "Кайфуем))\nПар нет"
                else:
                    str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[weekday + 7] + '\n\n' + \
                                    clock[2] + " - " + clock[3] + '\n' + timetable[weekday + 13] + '\n\n' + \
                                    clock[4] + " - " + clock[5] + '\n' + timetable[weekday + 19] + '\n\n' + \
                                    clock[6] + " - " + clock[7] + '\n' + timetable[weekday + 25] + '\n\n'
                weekday = timetable[weekday + 1]
            if len(timetable) == 25:
                if timetable[weekday + 7] == timetable[weekday + 13] == timetable[weekday + 19] == "":
                    str_timetable = "Кайфуем))\nПар нет"
                else:
                    str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[weekday + 7] + '\n\n' + \
                                    clock[2] + " - " + clock[3] + '\n' + timetable[weekday + 13] + '\n\n' + \
                                    clock[4] + " - " + clock[5] + '\n' + timetable[weekday + 19] + '\n\n'
                weekday = timetable[weekday + 1]
            if len(timetable) == 19:
                if timetable[weekday + 7] == timetable[weekday + 13] == "":
                    str_timetable = "Кайфуем))\nПар нет"
                else:
                    str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[weekday + 7] + '\n\n' + \
                                    clock[2] + " - " + clock[3] + '\n' + timetable[weekday + 13] + '\n\n'
                weekday = timetable[weekday + 1]
            if len(timetable) == 13:
                if timetable[weekday + 7] == "":
                    str_timetable = "Кайфуем))\nПар нет"
                else:
                    str_timetable = clock[0] + " - " + clock[1] + '\n' + timetable[weekday + 7] + '\n\n'
                weekday = timetable[weekday + 1]
        if weekday == 6:
            weekday = "Воскресенье"
            str_timetable = "Отдыхай))\nПар нет😄"
        if str_timetable == -1:
            str_timetable = "На это время не существует расписания"
    else:
        weekday = "На эту дату расписания не существует"
        str_timetable = "Ничего не могу с этим сделать(((\nОбратитесь к программисьам сайта Самарского университета"
    return "📅"+weekday, str_timetable


async def teacher_timetable(url, week):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        ans = await response.text()
    soup = BeautifulSoup(ans, 'html.parser')
    b = soup.find_all('div', class_='schedule__item')
    c = soup.find_all('div', class_="schedule__time-item")
    teach_timetable = ""
    for i in range(0, 6):
        try:
            teach_timetable += "⚠" + (str(b[i + 1].text)
                                      + "\n\n" + str(c[0].text) + "-" + str(c[1].text) + "\n" + str(b[i + 7].text)
                                      + "\n\n" + str(c[2].text) + "-" + str(c[3].text) + "\n" + str(b[i + 13].text)
                                      + "\n\n" + str(c[4].text) + "-" + str(c[5].text) + "\n" + str(b[i + 19].text)
                                      + "\n\n" + str(c[6].text) + "-" + str(c[7].text) + "\n" + str(b[i + 25].text)
                                      + "\n\n" + str(c[8].text) + "-" + str(c[9].text) + "\n" + str(b[i + 31].text)
                                      + "\n\n" + str(c[10].text) + "-" + str(c[11].text) + "\n" + str(b[i + 37].text)
                                      + "\n\n" + str(c[12].text) + "-" + str(c[13].text) + "\n" + str(b[i + 43].text)
                                      + "\n\n\n")
        except IndexError:
            try:
                teach_timetable += "⚠" + (str(b[i + 1].text)
                                          + "\n\n" + str(c[0].text) + "-" + str(c[1].text) + "\n" + str(b[i + 7].text)
                                          + "\n\n" + str(c[2].text) + "-" + str(c[3].text) + "\n" + str(b[i + 13].text)
                                          + "\n\n" + str(c[4].text) + "-" + str(c[5].text) + "\n" + str(b[i + 19].text)
                                          + "\n\n" + str(c[6].text) + "-" + str(c[7].text) + "\n" + str(b[i + 25].text)
                                          + "\n\n" + str(c[8].text) + "-" + str(c[9].text) + "\n" + str(b[i + 31].text)
                                          + "\n\n" + str(c[10].text) + "-" + str(c[11].text) + "\n" + str(
                            b[i + 37].text)
                                          + "\n\n\n")
            except IndexError:
                try:
                    teach_timetable += "⚠" + (str(b[i + 1].text)
                                              + "\n\n" + str(c[0].text) + "-" + str(c[1].text) + "\n" + str(
                                b[i + 7].text)
                                              + "\n\n" + str(c[2].text) + "-" + str(c[3].text) + "\n" + str(
                                b[i + 13].text)
                                              + "\n\n" + str(c[4].text) + "-" + str(c[5].text) + "\n" + str(
                                b[i + 19].text)
                                              + "\n\n" + str(c[6].text) + "-" + str(c[7].text) + "\n" + str(
                                b[i + 25].text)
                                              + "\n\n" + str(c[8].text) + "-" + str(c[9].text) + "\n" + str(
                                b[i + 31].text)
                                              + "\n\n\n")
                except IndexError:
                    try:
                        teach_timetable += "⚠" + (str(b[i + 1].text)
                                                  + "\n\n" + str(c[0].text) + "-" + str(c[1].text) + "\n" + str(
                                    b[i + 7].text)
                                                  + "\n\n" + str(c[2].text) + "-" + str(c[3].text) + "\n" + str(
                                    b[i + 13].text)
                                                  + "\n\n" + str(c[4].text) + "-" + str(c[5].text) + "\n" + str(
                                    b[i + 19].text)
                                                  + "\n\n" + str(c[6].text) + "-" + str(c[7].text) + "\n" + str(
                                    b[i + 25].text)
                                                  + "\n\n\n")
                    except IndexError:
                        try:
                            teach_timetable += "⚠" + (str(b[i + 1].text)
                                                      + "\n\n" + str(c[0].text) + "-" + str(c[1].text) + "\n" + str(
                                        b[i + 7].text)
                                                      + "\n\n" + str(c[2].text) + "-" + str(c[3].text) + "\n" + str(
                                        b[i + 13].text)
                                                      + "\n\n" + str(c[4].text) + "-" + str(c[5].text) + "\n" + str(
                                        b[i + 19].text)
                                                      + "\n\n\n")
                        except IndexError:
                            try:
                                teach_timetable += "⚠" + (str(b[i + 1].text)
                                                          + "\n\n" + str(c[0].text) + "-" + str(c[1].text) + "\n" + str(
                                            b[i + 7].text)
                                                          + "\n\n" + str(c[2].text) + "-" + str(c[3].text) + "\n" + str(
                                            b[i + 13].text)
                                                          + "\n\n\n")
                            except IndexError:
                                try:
                                    teach_timetable += "⚠" + (str(b[i + 1].text)
                                                              + "\n\n" + str(c[0].text) + "-" + str(
                                                c[1].text) + "\n" + str(b[i + 7].text)
                                                              + "\n\n\n")
                                except IndexError:
                                    teach_timetable += "распсиания нет\n"
    return teach_timetable


async def bot(event):
    global reminder
    global week_correct
    try:
        tt=''
        with open("list_id.json") as j:
            data = j.read()
            data = json.loads(data)
            # vk_id = data["vk_id"]
        with open("general_config.json") as j:
            gen = j.read()
            gen = eval(gen)
            teachers = gen["teachers"]
            fam = list(teachers.keys())
            week_correct = gen["week_correct"]
            #print(datetime.datetime.now().month)
            if datetime.datetime.now().month > 7:
                week_correct = week_correct["1"]
            else:
                week_correct = week_correct["2"]
            #print("=======\n",week_correct)
        if event.type == VkBotEventType.MESSAGE_NEW:
            message = event.object.message.get('text').lower()
            person_id = list(event.object.values())[0].get('from_id')
            for i in data:
                if person_id in data[i]:
                    group_config=f"{i}.json"
                    group_number=i
                    break
            else:
                if event.from_user:
                    vk.messages.send(peer_id=person_id,message="Вы неопознаннный шакал",random_id=0)
                if event.from_chat:
                    send("Вы неопознаннный шакал",event.chat_id)
                return
            with open(group_config) as j:
                config = j.read()
                config = eval(config)
            # if person_id in vk_id:
            if re.match('jarvis', message) or re.match('джарвиз', message) or re.match('jarvis,',message) or re.match('джарвиз,', message) or re.match('бот', message) or re.match('bot', message) or re.match('бот,',message) or re.match('bot,', message):
                if re.match('джарвиз', message) or re.match('jarvis,', message):
                    message = message[7:]
                elif re.match('jarvis', message):
                    message = message[6:]
                elif re.match('джарвиз,', message):
                    message = message[8:]
                elif re.match('бот,', message) or re.match('bot,', message):
                    message = message[4:]
                elif re.match('бот', message) or re.match('bot', message):
                    message = message[3:]
                message = message.strip()
                message = message.replace("ё", "е")
                print(message)
                if re.match("инструкция", message):
                    if event.from_chat:
                        if event.chat_id == config["chat_id"]:
                            send(instruct, event.chat_id)
                    if event.from_user:
                        vk.messages.send(peer_id=person_id, message=instruct, random_id=0)
                elif re.match("расписание препода", message) or re.match("расписание преподавателя",message) or re.match("расписание учителя",message):
                    if re.match("расписание препода", message) or re.match("расписание учителя", message):
                        message = message[18:]
                    if re.match("расписание преподавателя", message):
                        message = message[23:]
                    message = message.strip()
                    mes = message.split(" ")
                    pmweek = mes[::-1][0]
                    week = datetime.datetime.today().isocalendar()[1] + int(week_correct)
                    if pmweek[0] == "+":
                        week += int(pmweek[1])
                        mes.remove(pmweek)
                    if pmweek[0] == "-":
                        week -= int(pmweek[1])
                        mes.remove(pmweek)
                    message = ""
                    for i in mes:
                        message += i
                    try:
                        url = teachers[str(message)]
                        url = url.replace("11111", str(week))
                        tt = await teacher_timetable(url, week)
                        if event.from_user:
                            vk.messages.send(peer_id=person_id, message=tt, random_id=0)
                        if event.from_chat:
                            if event.chat_id == config["chat_id"]:
                                send(tt, event.chat_id)
                    except KeyError:
                        if event.from_user:
                            vk.messages.send(peer_id=person_id,
                                             message="Проверь название предмета или фамилию преподавателя(если забыл фамилии - напиши 'бот преподы'😉)",
                                             random_id=0)
                        if event.from_chat:
                            if event.chat_id == config["chat_id"]:
                                send("Проверь название предмета или фамилию преподавателя(если забыл фамилии - напиши 'бот преподы'😉)",
                                    event.chat_id)
                elif re.search('расписание', message) or re.search('timetable', message) or re.search('таймтэйбэл',message) or re.search('расп', message):
                    message = message.strip()
                    message = message.replace("расписание", "")
                    message = message.replace("timetable", "")
                    message = message.replace("таймтэйбэл", "")
                    message = message.replace("расп", "")
                    message = message.strip()
                    message = message.replace("\\", "/")
                    message = message.replace(".", "/")
                    message = message.replace(" ", "/")
                    with open(group_config) as j:
                        data = j.read()
                        data = json.loads(data)
                        url = data["student_url"]
                    if message != '':
                        #print(message)
                        if message == "сегодня" or message == "на/сегодня":
                            weekday = datetime.datetime.today()
                            week = weekday.isocalendar()[1] + int(week_correct)
                            weekday = weekday.weekday()
                        elif message == "завтра" or message == "на/завтра":
                            weekday = datetime.datetime.today()
                            weekday = weekday + datetime.timedelta(days=1)
                            week = weekday.isocalendar()[1] + int(week_correct)
                            weekday = weekday.weekday()
                        elif message == "послезавтра" or message == "на/послезавтра":
                            weekday = datetime.datetime.today()
                            weekday = weekday + datetime.timedelta(days=2)
                            week = weekday.isocalendar()[1] + int(week_correct)
                            weekday = weekday.weekday()
                        elif message == "вчера":
                            weekday = datetime.datetime.today()
                            weekday = weekday - datetime.timedelta(days=1)
                            week = weekday.isocalendar()[1] + int(week_correct)
                            weekday = weekday.weekday()
                        elif "на/неделю" in message or "неделя" in message:
                            #print("nedela")
                            message = message.replace("на/неделю", "")
                            message = message.replace("неделя", "")
                            if "+" in message or "-" in message:
                                #print("!")
                                message = message.replace("/", "")
                                weekday = datetime.datetime.today()
                                week = weekday.isocalendar()[1] + int(week_correct) + int(message)
                                weekday = 0
                                url = url.replace("11111", str(week))
                                message = "неделя"
                                # for i in range(weekday, 6):
                                #     weekday, str_timetable = await timetable(url, i, event)
                                #     vk.messages.send(peer_id=person_id, message=weekday, random_id=0)
                                #     vk.messages.send(peer_id=person_id, message=str_timetable, random_id=0)
                            else:
                                #print("@")
                                weekday = datetime.datetime.today()
                                week = weekday.isocalendar()[1] + int(week_correct)
                                weekday = weekday.weekday()
                                url = url.replace("11111", str(week))
                                message = "неделя"
                                # for i in range(weekday, 6):
                                #     weekday, str_timetable = await timetable(url, i, event)
                                #     vk.messages.send(peer_id=person_id, message=weekday, random_id=0)
                                #     vk.messages.send(peer_id=person_id, message=str_timetable, random_id=0)
                        elif message.split("/")[0] in fam:
                            #print("!!!")
                            url = teachers[message.split("/")[0]]
                            week = datetime.datetime.today().isocalendar()[1] + int(week_correct)
                            #print(message)
                            if "+" in message:
                                f = message.split("+")
                                message = f[0].strip()
                                week += int(f[1])
                            elif "-" in message:
                                f = message.split("-")
                                message = f[0].strip()
                                week -= int(f[1])
                            else:
                                message=message.strip()
                            tt = await teacher_timetable(url, week)
                            #now_weekday = datetime.datetime.today()
                            #now_weekday = now_weekday.weekday()

                        elif message in list_week:
                            #print("=weekday=")
                            now_weekday = datetime.datetime.today()
                            week = now_weekday.isocalendar()[1] + int(week_correct)
                            now_weekday = now_weekday.weekday()
                            weekday = list_week[message]
                            if now_weekday > weekday:
                                week+=1
                        else:
                            if "/" in message:
                                try:
                                    weekday = datetime.datetime.strptime(message, "%d/%m")
                                    weekday = weekday.replace(year=datetime.datetime.today().year)
                                    week = weekday.isocalendar()[1] + int(week_correct)
                                    # print("---", weekday)
                                except ValueError:
                                    try:
                                        weekday = datetime.datetime.strptime(message, "%d/%m/%Y")
                                    except ValueError:
                                        weekday = datetime.datetime.strptime(message, "%d/%m/%y")
                                    week = weekday.isocalendar()[1] + int(week_correct)
                                    # print("^^", weekday)
                                weekday = weekday.weekday()
                            else:
                                if event.from_chat:
                                    send("неправильная команда, уточни провильность в разделе инструкции",event.chat_id)
                                if event.from_user:
                                    vk.messages.send(peer_id=person_id,
                                                     message="неправильная команда, уточни провильность в разделе инструкции",
                                                     random_id=0)
                                return
                    else:
                        weekday = datetime.datetime.today().weekday()
                        week = datetime.datetime.today().isocalendar()[1] + int(week_correct) #     2 семестр
                    #url = "https://ssau.ru/rasp?groupId=530994177&selectedWeek=" + str(week) + "&selectedWeekday=1"
                    #print(week)
                    url = url.replace("11111", str(week))
                    if event.from_user:
                        if message == "на/неделю" or message == "неделя":
                            for i in range(weekday, 6):
                                weekday, str_timetable = await timetable(url, i, event)
                                vk.messages.send(peer_id=person_id, message=weekday, random_id=0)
                                vk.messages.send(peer_id=person_id, message=str_timetable, random_id=0)
                        else:
                            # print("---")
                            # print(weekday)
                            if tt != '':
                                tt = await teacher_timetable(url, week)
                                vk.messages.send(peer_id=person_id, message=tt, random_id=0)
                            else:
                                weekday, str_timetable = await timetable(url, weekday, event)
                                vk.messages.send(peer_id=person_id, message=weekday, random_id=0)
                                vk.messages.send(peer_id=person_id, message=str_timetable, random_id=0)
                    if event.from_chat:
                        if message == "на/неделю" or message == "неделя":
                            for i in range(weekday, 6):
                                weekday, str_timetable = await timetable(url, i, event)
                                send(weekday, event.chat_id)
                                send(str_timetable, event.chat_id)
                        else:
                            # print("---")
                            # print(weekday)
                            if tt != '':
                                tt = await teacher_timetable(url, week)
                                send(tt, event.chat_id)
                            else:
                                weekday, str_timetable = await timetable(url, weekday, event)
                                send(weekday, event.chat_id)
                                send(str_timetable, event.chat_id)
                        # # print(event.chat_id)
                        # if message == "на/неделю" or message == "неделя":
                        #     for i in range(weekday, 6):
                        #         if event.chat_id == config["chat_id"]:
                        #             weekday, str_timetable = await timetable(url, i, event)
                        #             send(f"{weekday}", event.chat_id)
                        #             send(str_timetable, event.chat_id)
                        # else:
                        #     weekday, str_timetable = await timetable(url, weekday, event)
                        #     send(f"{weekday}", event.chat_id)
                        #     send(str_timetable, event.chat_id)
                elif re.search("посмотреть дедлайны", message) or re.search("посмотреть дэдлайны", message) or re.search("дэдлайны", message):
                    async with sql.connect("deadline.db") as db:
                        deadlines = await db.execute("SELECT * FROM deadline")
                        deadlines = await deadlines.fetchall()
                    message = ""
                    if event.from_user:
                        if deadlines != []:
                            for i in deadlines:
                                message = message + i[0] + "\n" + i[1] + "\n" + i[2] + "\n\n"
                            vk.messages.send(peer_id=person_id, message=message, random_id=0)
                        else:
                            vk.messages.send(peer_id=person_id, message="Дэдлайнов нет", random_id=0)
                    if event.from_chat:
                        if event.chat_id == config["chat_id"]:
                            if deadlines != []:
                                for i in deadlines:
                                    message = message + i[0] + "\n" + i[1] + "\n" + i[2] + "\n\n"
                                send(message, event.chat_id)
                            else:
                                send("Дэдлайнов нет", event.chat_id)
                elif re.search("дедлайн", message) or re.search("дэдлайн", message):  # формат
                    message = message[7:]  # дата и время
                    message = message.lstrip('\n')  # предмет
                    message = message.strip(" ")
                    message = message.lstrip('\n')
                    message = message.split('\n')  # задача
                    message[0] = message[0].replace("\\", "-")
                    message[0] = message[0].replace(".", "-")
                    message[0] = message[0].replace("/", "-")
                    message[0] = message[0].strip(" ")
                    try:
                        deadline = datetime.datetime.strptime(message[0], "%d-%m %H:%M")
                        deadline = deadline.replace(year=datetime.datetime.today().year)
                    except ValueError:
                        try:
                            deadline = datetime.datetime.strptime(message[0], "%d-%m-%Y %H:%M")
                        except ValueError:
                            deadline = datetime.datetime.strptime(message[0], "%d-%m")
                            deadline = deadline.replace(year=datetime.datetime.today().year)
                            deadline = deadline.replace(hour=7, minute=0)
                    if event.from_chat:
                        if event.chat_id == config["chat_id"]:
                            if deadline < datetime.datetime.now():
                                send('Дедлай назначается на прошедшую дату. Измените дату.', event.chat_id)
                            else:
                                reminder.append(datetime.datetime(deadline.year, deadline.month, deadline.day, deadline.hour, deadline.minute, 0))
                                async with sql.connect("deadline.db") as db:
                                    await db.execute("INSERT INTO deadline VALUES (?,?,?,?)", (str(deadline), message[1], message[2], config["chat_id"]))
                                    await db.commit()
                                send("Записал", event.chat_id)
                    if event.from_user:
                        if deadline < datetime.datetime.now():
                            vk.messages.send(peer_id=person_id,
                                             message='Дедлай назначается на прошедшую дату. Измените дату.',
                                             random_id=0)
                        else:
                            reminder.append(datetime.datetime(deadline.year, deadline.month, deadline.day, deadline.hour,deadline.minute, 0))
                            async with sql.connect("deadline.db") as db:
                                await db.execute("INSERT INTO deadline VALUES (?,?,?,?)", (str(deadline), message[1], message[2], config["chat_id"]))
                                await db.commit()
                                # a = await db.execute("SELECT * FROM deadline")
                                # a = await a.fetchall()
                            vk.messages.send(peer_id=person_id, message="Записал", random_id=0)
                elif re.search("преподы", message) or re.search("преподаватели", message) or re.search("учителя",message) or re.search("список преподов", message) or re.search("список преподавателей", message) or re.search("список учителей", message):
                    with open(group_config) as j:
                        now_teachers = j.read()
                        now_teachers = json.loads(now_teachers)
                        now_teachers = now_teachers["now_teachers"]
                    if event.from_chat:
                        if event.chat_id == config["chat_id"]:
                            send(now_teachers, event.chat_id)
                    if event.from_user:
                        vk.messages.send(peer_id=person_id, message=now_teachers, random_id=0)
                else:
                    if event.from_chat:
                        if event.chat_id == config["chat_id"]:
                            send("Проверь правильность команды", event.chat_id)
                    if event.from_user:
                        vk.messages.send(peer_id=person_id, message="Проверь правильность команды", random_id=0)
    except Exception as e:
        now = datetime.datetime.now()
        print(str(now) + "\n" + str(e))
        raise e
        if event.from_chat:
            send("Неизвестная ошибка\nОбратитесь к разработчику отправив сообщение в группе https://vk.com/public218320118",event.chat_id)
            vk.messages.send(peer_id=210242776,message=str(now) + "\n" + "chat id - " + str(event.chat_id) + "\n" + str(e), random_id=0)
        if event.from_user:
            vk.messages.send(peer_id=person_id,
                             message="Неизвестная ошибка\nОбратитесь к разработчику отправив сообщение в группе https://vk.com/public218320118",
                             random_id=0)
            vk.messages.send(peer_id=210242776, message=str(now) + "\n" + "user id - " + str(person_id) + "\n" + str(e),
                             random_id=0)
    await asyncio.sleep(1)


async def listener(loop):
    with open("list_id.json") as j:
            data = j.read()
            data = json.loads(data)
    for i in data:
        async with sql.connect("deadline.db") as db:
            await db.execute(f"CREATE TABLE IF NOT EXISTS 'deadline'('Date_and_Time' STRING, 'subject' STRING, 'task' STRING, 'chatID' INT)")
            await db.commit()
            bd = await db.execute(f"SELECT * FROM deadline")
            bd = await bd.fetchall()
        if bd != []:
            reminder = datetime.datetime.strptime(bd[0][0], "%Y-%m-%d %H:%M:%S")
            for i in bd:
                if datetime.datetime.strptime(i[0], "%Y-%m-%d %H:%M:%S") < reminder:
                    reminder = datetime.datetime.strptime(i[0], "%Y-%m-%d %H:%M:%S")
    while True:
        for event in longpoll.listen():
            try:
                await asyncio.wait([loop.create_task(bot(event))])
            except socket.timeout:
                continue
            except urllib3.exceptions.ReadTimeoutError:
                continue
            except vk_api.exceptions.ApiError:
                continue
            except requests.exceptions.ReadTimeout:
                continue
            except requests.exceptions.ConnectionError:
                continue


async def sender():
    try:
        global reminder
        now = datetime.datetime.now()
        week = datetime.datetime.today().isocalendar()[1] + int(week_correct)
        #отправка расписания
        if now.hour == 7 and now.minute == 0:
            with open("list_id.json") as j:
                data = j.read()
                data = json.loads(data)
            for i in data:
                try:
                    with open(f"{i}.json") as j:
                        data = j.read()
                        data = json.loads(data)
                        url = data["student_url"]
                    url = url.replace("11111", str(week))
                    weekday = datetime.datetime.today().weekday()
                    weekday, str_timetable = await timetable(url, weekday, 1)
                    if weekday != "На эту дату расписания не существует":
                        send(f"{weekday}", int(data["chat_id"]))
                        send(str_timetable, int(data["chat_id"]))
                    else:
                        pass
                except FileNotFoundError:
                    continue
        #отправка уведомления
        for i in reminder:
            if now.date() == i.date():
                if now.hour == 7 and now.minute == 0:
                    async with sql.connect("deadline.db") as db:
                        info = await db.execute("SELECT * FROM deadline WHERE Date_and_Time = ?", (i,))
                        info = await info.fetchone()
                    messsage = info[1] + '\n' + info[2]
                    send(messsage, info[3])
                if now.hour == i.hour and now.minute == i.minute:
                    async with sql.connect("deadline.db") as db:
                        info = await db.execute("SELECT * FROM deadline WHERE Date_and_Time = ?", (i,))
                        info = await info.fetchone()
                        await db.execute("DELETE FROM deadline WHERE Date_and_Time = ?", (i,))
                        await db.commit()
                    messsage = info[1] + '\n' + info[2]
                    send(messsage, info[3])
    except Exception as e:
        now = datetime.datetime.now()
        print(str(now) + "\n" + str(e))
        vk.messages.send(peer_id=210242776, message=str(now) + "\n" + str(e),
                         random_id=0)
    await asyncio.sleep(60)


def main(func):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        try:
            if func == 0:
                loop.run_until_complete(listener(loop))
            if func == 1:
                loop.run_until_complete(sender())
        except socket.timeout:
            continue
        except vk_api.exceptions.ApiError:
            continue
        except urllib3.exceptions.ReadTimeoutError:
            continue
        except requests.exceptions.ReadTimeout:
            continue
        except requests.exceptions.ConnectionError:
            continue


if __name__ == '__main__':
    threads = []
    for i in range(0, 2):
        print(f"Запускаю поток {i}")
        t = Thread(target=main, args=[i])
        threads.append(t)
        t.start()
    for i in threads:
        i.join()