# здесь старт игры

#Автозамена с добавлением кавычек

    #В Найти: (.*), в Заменить: "$1" и ставим галку в "Регуляр. выражен."

# перенести концовку 1 дня в отдельный лейбл, дабы уменьшить кол во строк кода!!!!!!!!!!!

init python hide:

    class KonamiListener(renpy.Displayable):
        
        def __init__(self, target):
            
            renpy.Displayable.__init__(self)
            
            import pygame
            
            
            self.target = target
            
            
            
            self.state = 0
            
            
            self.code = [
                pygame.K_n,
                pygame.K_i,
                pygame.K_g,
                pygame.K_g,
                pygame.K_e,
                pygame.K_r,
                pygame.K_s
                ]
        
        
        def event(self, ev, x, y, st):
            import pygame
            
            
            if ev.type != pygame.KEYDOWN:
                return
            
            
            
            if ev.key != self.code[self.state]:
                self.state = 0
                return
            
            
            self.state += 1
            
            
            
            if self.state == len(self.code):
                self.state = 0
                renpy.call_in_new_context(self.target)
            
            return
        
        
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)



    store.konami_listener = KonamiListener('test0')


    def konami_overlay():
        ui.add(store.konami_listener)

    config.overlay_functions.append(konami_overlay)


label test0:
    $ persistent.chnomer = True



label start:

    th "Как же я не хочу вставать… Ну еще пять минуточек… "

    if persistent.chnomer == True:
        jump secret_ending

    th "Ладно, через силу, через боль, встаем!"
    th "В такую погоду  не то, что на улицу, с кровати не хочется вставать!"
    th "Но делать нечего…"
    th "Хотя может…"
    "выбор - идти на 1 пару или нет"
    menu:
        "Иду на 1 пару!":
            $ is_go_to_first_seminar = True
            $ zakolka = True
            jump go_to_first_seminar_first_day
        "Не иду на 1 пару":
            $ is_go_to_sec_seminar = True
            $ zakolka = True
            jump go_to_sec_seminar_first_day 
        "А может в принципе дома остаться?":
            $ is_stay_home_homie = True
            $ zakolka = False
            jump stay_home_first_day


label go_to_first_seminar_first_day:
    "пошел на 1 пару"
    th "Не не, я что, прогульщик? Идем в колледж, выбора нет, да и вроде пары должны быть интересные…"
    th "Так, первой стоит облачные технологии- отлично. Второй парой у нас основы программирования… Третьей - физра…"
    th "Ладно, жить можно."
    th "Ну, пора собираться."
    "Главный герой стоит на остановке и ждёт свой 78 автобус."
    th "Эх, а ведь я не хотел поступать в этот колледж на программиста, но кто меня спрашивал? "
    th "Кто бы знал, как могла бы сложиться моя жизнь, поступив я на сценариста, возможно, даже подъём с утра давался бы мне намного легче. "
    th "Хотел бы я написать сценарий для собственной игры… Ну кто знает, может однажды удастся не только написать, но и создать игру. "
    th "Эх, мечты…"
    "Автобус подъехал и главный герой садится на место у окна.(Эта вся сцена)"
    th "Дорога с Западного будет долгой. Что там нового мне предложит музыка?"
    th "С такой спокойной музыкой только “Спокойной ночи малыши” не хватает. Но даже без них спать хочется, ужас."
    th "Я, уснул? Слава богу хоть остановку не проехал."
    hero "Всем привет!"
    jeka "Привет."
    oleg "О, привет. Как дела?"
    hero "Ну ничего себе Олег, и ты тоже пришёл на пары, несмотря на то, что сегодня есть пара программирования?"
    oleg "Ну не начинай хоть ты, сам знаешь, что не было возможности прийти на пары из-за этой Большой перемены."
    hero "Да знаю, но всё-таки, ты пропустил практически месяц учёбы, как собираешься закрывать все долги?"
    oleg "Честно, пока сам не знаю."
    hero "Ну, ты с этим не затягивай главное."
    oleg "Да знаю я."
    cube "О, привет!"
    hero "Привет-привет. Ты в кои-то веки пришла вовремя?"
    cube "Прикинь, я пришла вовремя!"
    hero "Умница, получается, эпоха опозданий пришла к концу?"
    cube "Ахахах, получается что так."
    cube "Кстати, тут какой-то человек странный отдал мне заколку…"
    hero "А зачем она мне?"
    cube "Она похожа на заколку, которая у Алины, вот я и подумала, что лучше тебе отдать. Ты же с ней вроде хорошо общаешься?"
    cube "В любом случае, учитывая длину твоих волос, то скорее всего ты эту заколку будешь использовать, а не Алина."
    hero "Ха-ха, смешно. Ты как там вообще, что нового?"
    cube "Ну знаешь, в принципе всё хорошо, вот с подружками из ИС-22 гуляла."
    hero "Снова променяла нас на ИС-22?"
    cube "Ну не правда, не меняла я вас."
    hero "Да да, не меняла."
    cube "Ой, там ИС-22!"
    "*типо убегает*"
    hero "Что и требовалось доказать…"
    hero "Кстати, а какая у нас сейчас пара по расписанию?"
    an "Облачные технологии вроде."
    hero "О, Настя, привет."
    an "Ага, привет."
    an "В доту сегодня собираем стак?"
    hero "Почему нет, я только за. Жень?"
    jeka "Конечно, тогда сегодня день авантюрного манки кинга."
    jeka "у а у а абезьяна прыгать"
    an "Дурак?"
    jeka "Да за что?"
    hero "Ахахаха, как всегда, никто и ничто не меняется. И это радует."
    an "А?"
    an "Что с тобой? На какую то ваниль тебя пробило."
    jeka "Он вроде всегда был такой."
    an "Он раньше так не говорил."
    hero "Да ну ладно вам, просто в кои-то веки задумался, что в моей жизни наконец-то стало спокойно."
    th "Особенно после всего того, что было… Ну ничего, справимся. И не с таким справлялись."
    an "Хватит в облаках витать!(тут она щелкает пальцами перед лицом типо)"
    hero "ААААА!!"
    hero "Не пугай так."
    an "Чтобы не втыкал."
    jeka "Настя, не издевайся над человеком."
    jeka "И вообще, уже звонок по идее должен быть."
    "*Звенит звонок*"
    hero "А вот и он. Вспомни лучик…"
    jeka "Вот и солнце, да?"
    hero "Учитывая нашу погоду сейчас, то за солнце говорить не приходится. Его попросту нет."
    hero_na "Три дня дождей :DDD"
    "и все заходят в кабинет."
    th "В целом, если подумать, то сегодняшний день в колледже не такой уж и сложный."
    th "Скорее наоборот, сейчас будет пара облачных технологий с Алиной Алексеевной, а она всегда очень интересно объясняет тему."
    oleg "Уверен? Я думаю, что мне будут бить лицо…"
    th "Это еще почему?"
    oleg "Знаешь, сколько у меня долгов?"
    th "Даже знать не хочу."
    oleg "Ну вот тогда молчи."
    ship "Всем здравствуйте! О, Филиппов, наконец-то вернулся. Ну рассказывай, как съездил, где побывал, что видел?"
    oleg "Здравствуйте Алина Алексеевна, да всё хорошо, много чего видел."
    ship "Это, конечно,  всё хорошо, но знаешь, что ты не сможешь увидеть?)"
    oleg "Не… Не знаю..."
    ship "Зачёт по моему предмету, если не сдашь мне все практические за 1 семестр)."
    "*здесь вот этот прикол из ace attorney, по типу, take that!*"
    oleg "(Хз по идеи он сидит в ахуе, но хз, чтобы он сказал в такой ситуации)"
    "*Чёрный экран и закадровый голос щипанкиной"
    ship "Так, и сегодня мы начинаем изучать докер и все, связанные с ним команды."
    th "Пара пролетела довольно быстро и мы пошли на перерыв."
    th "На перемене, как обычно ничего интересного не произошло."
    "*Звенит звонок на 2 пару.*"
    th "Блин, уже прошло 15 минут, а преподавателя всё нет, может быть уйти с пары?"
    jeka "Может всё таки дождемся преподавателя?"
    th "Правило 15 минут, помните?"
    an "Поддерживаю, как говорится, кто куда, а я домой."
    jeka "Я всё таки подожду, мало ли, потом влетит ещё."
    oleg "Ну ребята, давайте, до завтра, я в принципе не собирался оставаться на эту пару."
    hero "Дилемма… Уйти или остаться?"
    "выбор уйти или остаться"
    menu:
        "Уходим":
            $ svalil = True
            "уйти"
            an "Единственно верное решение."
            jeka "Ну ладно, давайте тогда, до завтра."
            "*в раздевалке*"
            "*звук уведомления*"
            th "Вот чёрт, препод всё таки пришел… Придется возвращаться…"
        "Остаемся":
            $ svalil = False
            "остаться"
            th "Нет, я не должен так поступать, ведь это неправильно."
            "к:Прошла 1 минута."
            th "Я больше не могу ждать, нужно убедить других, чтобы не я один потом получил за то, что ушёл."
            an "Единственно верное решение."
            jeka "Ну ладно, давайте тогда, до завтра."
            "*в раздевалке*"
            "*звук уведомления*"
            th "Вот чёрт, препод всё таки пришел… Придется возвращаться…"
    "*спустя 1 пару* перед кабинетом манаковой"
    jeka "А я говорил, что не стоит уходить. Сейчас бы не писали всей группой объяснительную."
    an "Ну, ничего. Как то всё равно, знаешь?"
    th "В следующий раз я тебя обязательно послушаю. Но это не точно.(шепотом)"
    jeka "Ты что то сказал?"
    th "Говорю что ты прав, молодец."
    "*на выходе из шараги*"
    th "Лично я не горю желанием оставаться на физру после такой душной пары."
    th "Так что всем до свидания, увидимся завтра!"
    jeka "Бывай, удачи."
    an "Пока."
    "*тут что-то вроде таймскипа до автобуса*"
    "*звонок телефона*"
    th "Алло, да, здравствуйте."
    th "В смысле? Этого не может быть!"
    th "Буду через 5 минут."
    "*таймскип до дома пидружки(не в квартире)*"
    th "Это просто невозможно…"
    th "Почему именно она?"
    "*таймскип в квартиру пидружки*"
    "тут я хз, мне впадлу расписывать диалог с матерью подруги. Допустим, они поговорили, она ему отдала заколку. Вот именно с этого момента он официально в цикле."
    ma "%юзернейм%..."
    hero "Что случилось?"
    hero "Почему она умерла?"
    ma "НЕ ЗНАЮ!"
    ma "Я ничего не знаю…"
    ma "У всех такие вопросы…"
    ma "Просто…"
    ma "Отстаньте…"
    hero "Простите, не стоило мне так нападать с вопросами…"
    ma "Это ты меня прости, не стоило срываться…"
    ma "Я действительно не знаю, что произошло…"
    ma "Она просто не выходила из комнаты…"
    ma "Я…"
    ma "Я зашла туда, а она лежит…"
    ma "Бедная моя Алиночка…"
    hero "Мне очень жаль… "
    ma "Все хорошо. Иди домой."
    hero "Точно? "
    ma "Да, мне нужно побыть одной."
    th "Интересно, почему заколка?"
    th "У меня вроде волосы не длинные…"
    th "Боже, о чем я думаю, у меня подруга погибла так то… "
    th "Нужно срочно ехать домой, обдумать все."
    "*тут типо он вздрогнул от холода*"
    th "Осень будет холодной, да?"
    "*таймскип до дома*"
    th "Это просто…"
    th "Не знаю, что делать теперь?"
    th "Кто мог сделать с ней нечто подобное?"
    th "Ладно, отставить панику. Разберемся. Выхода другого нет."
    th "Да как тут спокойным то оставаться можно?!"
    th "Я ОСТАЛСЯ БЕЗ ПОДРУГИ!"
    th "И по неизвестной ни мне, ни её матери причине."
    th "А вдруг её отравили?"
    th "Нет, бред."
    th "Это всё полный бред."
    th "Может, это вообще сон? Я сейчас проснусь?"
    th "Надо себя ущипнуть вроде, дабы проснуться…"
    "*щипает себя*"
    th "Не сработало…"
    th "Вот же блин, я настолько сильно зациклился на эту ситуацию, что не заметил, как наступила глубокая ночь."
    th "Мне нужно отдохнуть, сегодня был слишком насыщенный день."
    jump second_day


label go_to_sec_seminar_first_day:
    th "Не не не, нет ничего важнее сна!"
    th " Я думаю, что если опоздаю на 1 пару, то ничего страшного не случится, ведь так? Ладно, это риторический вопрос."
    "Провалившись в свой сон, главный герой вспоминает свою старую знакомую, которая собиралась перейти к ним в ЛУЧШИЙ РОСТОВСКИЙ КОЛЛЕДЖ СВЯЗИ И ИНФОРМАТИКИ. Он видит её силуэт. Далее он видит Настю Антонову, она говорит ему:"
    an "КАК ТЕБЕ НЕ СТЫДНО ПРОГУЛИВАТЬ 1 ПАРУ?!"
    th " Вот чёрт, я опаздываю!"
    th "Ну вот, как знал, что нужно было идти в колледж… Ладно, опоздаю немного."
    "*играет https://vk.com/audio-2001426275_116426275*"
    th "Мда уж, день начался очень и очень “хорошо”, в следующий раз 100% встаю и иду на первую пару!!"
    "*автобус*"
    hero "Жесть, я еле успеваю к второй паре… Надо написать, что могу опоздать."
    "*на остановке*"
    "*гг смотрит на телефон*"
    hero "Ничего себе, я еще и не опоздал!"
    hero "Теперь бежим в колледж."
    "*в колледже*"
    ship "Посмотрите-ка, кто всё таки пришёл! %юзернейм%, ты ли это?"
    th "Здравствуйте, Алина Алексеевна…"
    ship "Ну здравствуй, скажешь, почему на паре не было?"
    th "Нуууу…"
    ship "А ладно, я не настолько старая и ворчливая. Пока что."
    ship "Возьмешь у ребят задание, сделаешь дома и всё."
    th "Хорошо, обязательно."
    hero "Кто поверил…"
    ship "Ты что-то сказал?"
    th "Не не, вам послышалось наверное."
    ship "Ну ладно, поверю."
    "*звонок на пару*"
    "*таймскип в аудиторию манаковой*"
    jeka "Здарова, ну ты и соня конечно."
    th "Был бы я Соней, пришёл бы к первой паре.(Типо Горожий)"
    jeka "Да ладно, я не осуждаю же. Но ты побил рекорд Кубары, можешь гордиться собой."
    th "Ха-ха-ха, как смешно."
    cube "О, привет!"
    hero "Привет-привет. Ты в кои-то веки пришла вовремя?"
    cube "Прикинь, я пришла вовремя!"
    hero "Умница, получается, эпоха опозданий пришла к концу?"
    cube "Ахахах, получается что так."
    cube "Кстати, тут какой-то человек странный отдал мне заколку…"
    hero "А зачем она мне?"
    cube "Она похожа на заколку, которая у Алины, вот я и подумала, что лучше тебе отдать. Ты же её близкий друг."
    cube "В любом случае, учитывая длину твоих волос, то скорее всего ты эту заколку будешь использовать, а не Алина."
    hero "Ха-ха, смешно. Ты как там вообще, что нового?"
    cube "Ну знаешь, в принципе всё хорошо, вот с подружками из ИС-22 гуляла."
    hero "Снова променяла нас на ИС-22?"
    cube "Ну не правда, не меняла я вас."
    hero "Да да, не меняла."
    cube "Ой, там ИС-22!"
    "*типо убегает*"
    hero "Что и требовалось доказать…"
    oleg "Привет!"
    jeka "Сегодня точно рак на горе свистнет…"
    oleg "Почему?"
    jeka "А, забей."
    th "Привет, Олег. Всё таки пришел на программирование?"
    oleg "А почему не прийти то?"
    th "Тоже верно."
    an "Ну вообще даете, даже я себе так не позволяю."
    th "Во-первых, привет. Во-вторых, что не позволяешь?"
    an "Не приходить на первую пару, ужас какой вообще."
    th "Ну проспал, ну что теперь сделать."
    an "Да нормально всё, просто уходи пораньше спать."
    th "Хорошо, постараюсь."
    "тут короче вот эта сцена перед выбором, сваливать чи не, дальше идет по такой же ветке, как и пойти на все пары."
    "*Звенит звонок на 2 пару.*"
    "к:15 минут спустя"
    th "Блин, уже прошло 15 минут, а преподавателя всё нет, может быть уйти с пары?"
    jeka "Может всё таки дождемся преподавателя?"
    th "Правило 15 минут, помните?"
    an "Поддерживаю, как говорится, кто куда, а я домой."
    jeka "Я всё таки подожду, мало ли, потом влетит ещё."
    oleg "Ну ребята, давайте, до завтра, я в принципе не собирался оставаться на эту пару."
    hero "Дилемма… Уйти или остаться?"
    menu:
        "Уходим":
            $ svalil = True
            "уйти"
            an "Единственно верное решение."
            jeka "Ну ладно, давайте тогда, до завтра."
            "*в раздевалке*"
            "*звук уведомления*"
            th "Вот чёрт, препод всё таки пришел… Придется возвращаться…"
        "Остаемся":
            $ svalil = False
            "остаться"
            th "Нет, я не должен так поступать, ведь это неправильно."
            "к:Прошла 1 минута."
            th "Я больше не могу ждать, нужно убедить других, чтобы не я один потом получил за то, что ушёл."
            an "Единственно верное решение."
            jeka "Ну ладно, давайте тогда, до завтра."
            "*в раздевалке*"
            "*звук уведомления*"
            th "Вот чёрт, препод всё таки пришел… Придется возвращаться…"
    "*спустя 1 пару* перед кабинетом манаковой"
    jeka "А я говорил, что не стоит уходить. Сейчас бы не писали всей группой объяснительную."
    an "Ну, ничего. Как то всё равно, знаешь?"
    th "В следующий раз я тебя обязательно послушаю. Но это не точно.(шепотом)"
    jeka "Ты что то сказал?"
    th "Говорю что ты прав, молодец."
    "*на выходе из шараги*"
    th "Лично я не горю желанием оставаться на физру после такой душной пары."
    th "Так что всем до свидания, увидимся завтра!"
    jeka "Бывай, удачи."
    an "Пока."
    "*тут что-то вроде таймскипа до автобуса*"
    "*звонок телефона*"
    th "Алло, да, здравствуйте."
    th "В смысле? Этого не может быть!"
    th "Буду через 5 минут."
    "*таймскип до дома пидружки(не в квартире)*"
    th "Это просто невозможно…"
    th "Почему именно она?"
    "*таймскип в квартиру пидружки*"
    "тут я хз, мне впадлу расписывать диалог с матерью подруги. Допустим, они поговорили, она ему отдала заколку. Вот именно с этого момента он официально в цикле."
    ma "%юзернейм%..."
    hero "Что случилось?"
    hero "Почему она умерла?"
    ma "НЕ ЗНАЮ!"
    ma "Я ничего не знаю…"
    ma "У всех такие вопросы…"
    ma "Просто…"
    ma "Отстаньте…"
    hero "Простите, не стоило мне так нападать с вопросами…"
    ma "Это ты меня прости, не стоило срываться…"
    ma "Я действительно не знаю, что произошло…"
    ma "Она просто не выходила из комнаты…"
    ma "Я…"
    ma "Я зашла туда, а она лежит…"
    ma "Бедная моя Алиночка…"
    hero "Мне очень жаль… "
    ma "Все хорошо. Иди домой."
    hero "Точно? "
    ma "Да, мне нужно побыть одной."
    th "Интересно, почему заколка?"
    th "У меня вроде волосы не длинные…"
    th "Боже, о чем я думаю, у меня подруга погибла так то… "
    th "Нужно срочно ехать домой, обдумать все."
    "*тут типо он вздрогнул от холода*"
    th "Осень будет холодной, да?"
    "*таймскип до дома*"
    th "Это просто…"
    th "Не знаю, что делать теперь?"
    th "Кто мог сделать с ней нечто подобное?"
    th "Ладно, отставить панику. Разберемся. Выхода другого нет."
    th "Да как тут спокойным то оставаться можно?!"
    th "Я ОСТАЛСЯ БЕЗ ПОДРУГИ!"
    th "И по неизвестной ни мне, ни её матери причине."
    th "А вдруг её отравили?"
    th "Нет, бред."
    th "Это всё полный бред."
    th "Может, это вообще сон? Я сейчас проснусь?"
    th "Надо себя ущипнуть вроде, дабы проснуться…"
    "*щипает себя*"
    th "Не сработало…)"
    th "Вот же блин, я настолько сильно зациклился на эту ситуацию, что не заметил, как наступила глубокая ночь."
    th "Мне нужно отдохнуть, сегодня был слишком насыщенный день."
    jump second_day

label stay_home_first_day:
    th " Да не, не хочу я сегодня идти на пары, уж лучше посплю, а там уже можно и постримить любимый валорант."
    "Главный герой засыпает."
    "Провалившись в свой сон, главный герой вспоминает свою старую знакомую, которая собиралась перейти к ним в ЛУЧШИЙ РОСТОВСКИЙ КОЛЛЕДЖ СВЯЗИ И ИНФОРМАТИКИ. Он видит чей-то силует и тот говорит ему:"
    nn " Лучше иди в колледж, иначе ты пожалеешь!"
    "*проснулся с криком*"
    th "Что это было?!"
    th "Ладно, это же всего лишь сон, просто фантазия моего мозга."
    th "Пойду досыпать своё."
    "*спустя 5 минут*"
    th "Сна ни в одном глазу. Особенно после того кошмара, что в общем-то и неудивительно."
    th "Ладно, пойду поиграю что-ли."
    "*таймскип до вечера*"
    th "Отлично сыграл, поднял себе золото, можно и отвлечься я думаю."
    th "А сколько время то?"
    "*на часах 19:34*"
    th "..."
    th "Ну…"
    th "Зато золото поднял."
    "*звонок телефона*"
    th "Алло, да, здравствуйте."
    th "В смысле? Этого не может быть!"
    th "Буду через 5 минут."
    "*таймскип до дома пидружки(не в квартире)*"
    th "Это просто невозможно…"
    th "Почему именно она?"
    "*таймскип в квартиру пидружки*"
    ma "%юзернейм%..."
    hero "Что случилось?"
    hero "Почему она умерла?"
    ma "НЕ ЗНАЮ!"
    ma "Я ничего не знаю…"
    ma "У всех такие вопросы…"
    ma "Просто…"
    ma "Отстаньте…"
    hero "Простите, не стоило мне так нападать с вопросами…"
    ma "Это ты меня прости, не стоило срываться…"
    ma "Я действительно не знаю, что произошло…"
    ma "Она просто не выходила из комнаты…"
    ma "Я…"
    ma "Я зашла туда, а она лежит…"
    ma "Бедная моя Алиночка…"
    hero "Мне очень жаль… "
    ma "Все хорошо. Иди домой."
    hero "Точно? "
    ma "Да, мне нужно побыть одной."
    th "Нужно срочно ехать домой, обдумать все."
    "*тут типо он вздрогнул от холода*"
    th "Осень будет холодной, да?"
    "*таймскип до дома*"
    th "Это просто…"
    th "Не знаю, что делать теперь?"
    th "Кто мог сделать с ней нечто подобное?"
    th "Ладно, отставить панику. Разберемся. Выхода другого нет."
    th "Да как тут спокойным то оставаться можно?!"
    th "Я ОСТАЛСЯ БЕЗ ПОДРУГИ!"
    th "И по неизвестной ни мне, ни её матери причине."
    th "А вдруг её отравили?"
    th "Нет, бред."
    th "Это всё полный бред."
    th "Может, это вообще сон? Я сейчас проснусь?"
    th "Надо себя ущипнуть вроде, дабы проснуться…"
    "*щипает себя*"
    th "Не сработало…"
    th "Вот же блин, я настолько сильно зациклился на эту ситуацию, что не заметил, как наступила глубокая ночь."
    th "Мне нужно отдохнуть, сегодня был СЛИШКОМ насыщенный день."

    jump second_day