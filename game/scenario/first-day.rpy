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
    stop music fadeout 1.0

    play sound budilnik

    th "Как же я не хочу вставать… Ну еще пять минуточек… "

    stop sound fadeout 1.0 

    if persistent.chnomer == True:
        jump secret_ending

    scene home gg morning with dissolve
    show blinking

    play music intro_games

    th "Ладно, через силу, через боль, встаем!"
    th "В такую погоду  не то, что на улицу, с кровати не хочется вставать!"
    th "Но делать нечего…"
    th "Хотя может…"
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
    th "Не не, я что, прогульщик? Идем в колледж, выбора нет, да и вроде пары должны быть интересные…"
    th "Так, первой стоит облачные технологии- отлично. Второй парой у нас основы программирования… Третьей - физра…"
    th "Ладно, жить можно."
    th "Ну, пора собираться."

    stop music fadeout 1

    $ timeskip_short()
    scene bus stop with bkrr_timeskip_transition()

    play sound avtobus

    "Главный герой стоит на остановке и ждёт свой 78 автобус."
    th "Эх, а ведь я не хотел поступать в этот колледж на программиста, но кто меня спрашивал? "
    th "Кто бы знал, как могла бы сложиться моя жизнь, поступив я на сценариста, возможно, даже подъём с утра давался бы мне намного легче. "
    th "Хотел бы я написать сценарий для собственной игры… Ну кто знает, может однажды удастся не только написать, но и создать игру. "
    th "Эх, мечты…"

    scene abobus with dissolve

    th "Дорога с Западного будет долгой. Что там нового мне предложит музыка?"

    play music avtobus_musik

    th "С такой спокойной музыкой только “Спокойной ночи малыши” не хватает. Но даже без них спать хочется, ужас."

    stop sound fadeout 1.5

    window hide
    show blink
    $ renpy.pause(1.5)
    hide blink
    show unblink
    $ renpy.pause(1.0)
    window show

    th "Я, уснул? Слава богу хоть остановку не проехал."

    stop music fadeout 2.0

    $ timeskip_short()
    scene college hallway with bkrr_timeskip_transition()    

    play sound koridor

    hero "Всем привет!"

    show jeka normal at left with dspr 

    jeka smirk "Привет."

    show oleg smile at right with dspr

    oleg smile "О, привет. Как дела?"
    hero "Ну ничего себе Олег, и ты тоже пришёл на пары, несмотря на то, что сегодня есть пара программирования?"
    oleg "Ну не начинай хоть ты, сам знаешь, что не было возможности прийти на пары из-за этой Большой перемены."
    hero "Да знаю, но всё-таки, ты пропустил практически месяц учёбы, как собираешься закрывать все долги?"
    oleg "Честно, пока сам не знаю."
    hero "Ну, ты с этим не затягивай главное."
    oleg "Да знаю я."

    hide jeka
    hide oleg
    show cube happy
    with dspr

    cube "О, привет!"
    hero "Привет-привет. Ты в кои-то веки пришла вовремя?"
    cube "Прикинь, я пришла вовремя!"
    hero "Умница, получается, эпоха опозданий пришла к концу?"
    cube "Ахахах, получается что так."
    cube normal "Кстати, тут какой-то человек странный отдал мне заколку…"
    hero "А зачем она мне?"
    cube "Она похожа на заколку, которая у Алины, вот я и подумала, что лучше тебе отдать. Ты же с ней вроде хорошо общаешься?"
    cube "В любом случае, учитывая длину твоих волос, то скорее всего ты эту заколку будешь использовать, а не Алина."
    hero "Ха-ха, смешно. Ты как там вообще, что нового?"
    cube "Ну знаешь, в принципе всё хорошо, вот с подружками из ИС-22 гуляла."
    hero "Снова променяла нас на ИС-22?"
    cube "Ну не правда, не меняла я вас."
    hero "Да да, не меняла."
    play sound steps
    cube surprised  "Ой, там ИС-22!"
    hide cube surprised with moveoutleft
    hero "Что и требовалось доказать…"
    stop sound fadeout 0.5

    $ renpy.pause(0.5)
    
    play sound koridor

    hero "Кстати, а какая у нас сейчас пара по расписанию?"

    show an normal with dspr 

    an "Облачные технологии вроде."
    hero "О, Настя, привет."
    an "Ага, привет."
    an "В доту сегодня собираем стак?"
    hero "Почему нет, я только за. Жень?"

    show jeka normal at right with dspr

    jeka "Конечно, тогда сегодня день авантюрного манки кинга."
    jeka smirk "у а у а абезьяна прыгать"
    an surprise "Дурак?"
    jeka serious "Да за что?"
    hero "Ахахаха, как всегда, никто и ничто не меняется. И это радует."
    an normal "А?"
    an "Что с тобой? На какую то ваниль тебя пробило."
    jeka normal "Он вроде всегда был такой."
    an "Он раньше так не говорил."
    hero "Да ну ладно вам, просто в кои-то веки задумался, что в моей жизни наконец-то стало спокойно."
    hide jeka
    hide an
    with dspr
    th "Особенно после всего того, что было… {w}Ну ничего, справимся. И не с таким справлялись."

    $ renpy.pause(0.5)
    show an angry with dspr

    an "Хватит в облаках витать!"
    hero "ААААА!!"
    hero "Не пугай так."
    an normal "Чтобы не втыкал."

    show jeka serious at right with dspr
    
    jeka "Настя, не издевайся над человеком."
    jeka "И вообще, уже звонок по идее должен быть."
    play sound rksi
    hero "А вот и он. Вспомни лучик…"
    jeka "Вот и солнце, да?"
    hero "Учитывая нашу погоду сейчас, то за солнце говорить не приходится. Его попросту нет."

    stop sound fadeout 2.0

    hide jeka
    show an happy
    with dspr

    hero_na "Три дня дождей!"

    scene aud 1 with dissolve

    play sound koridor

    hero "В целом, если подумать, то сегодняшний день в колледже не такой уж и сложный."
    hero "Скорее наоборот, сейчас будет пара облачных технологий с Алиной Алексеевной, а она всегда очень интересно объясняет тему."
    
    show oleg _2 at right with dspr
    
    oleg "Уверен? Я думаю, что мне будет плохо…"
    hero "Это еще почему?"
    oleg "Знаешь, сколько у меня долгов?"
    hero "Даже знать не хочу."
    oleg "Ну вот и я о том же."

    show ship neutral at left with dspr
    # show ma neutral

    ship "Всем здравствуйте! О, Филиппов, наконец-то вернулся. Ну рассказывай, как съездил, где побывал, что видел?"
    oleg "Здравствуйте Алина Алексеевна, да всё хорошо, много чего видел."
    ship "Это, конечно,  всё хорошо, но знаешь, что ты не сможешь увидеть?)"
    oleg "Не… Не знаю..."
    ship "Зачёт по моему предмету, если не сдашь мне все практические за 1 семестр)."

    scene black with dissolve

    ship "Так, и сегодня мы начинаем изучать докер и все, связанные с ним команды."

    stop sound fadeout 3.0

    $ timeskip_short()
    scene college hallway with bkrr_timeskip_transition()    

    play sound rksi

    hero "Блин, уже прошло 15 минут, а преподавателя всё нет, может быть уйти с пары?"

    stop sound fadeout 1.5

    show jeka serious with dspr

    play sound koridor

    jeka "Может всё таки дождемся преподавателя?"
    hero "Правило 15 минут, помните?"

    show an normal at left with dspr

    an "Поддерживаю, как говорится, кто куда, а я домой."
    jeka "Я всё таки подожду, мало ли, потом влетит ещё."
    oleg "Ну ребята, давайте, до завтра, я в принципе не собирался оставаться на эту пару."
    hero "Дилемма… Уйти или остаться?"

    hide an
    hide jeka
    with dspr

    menu:
        "Уходим":
            $ svalil = True
            show jeka serious with dspr
            show an happy at left with dspr
            an "Единственно верное решение."
            jeka "Ну ладно, давайте тогда, до завтра."

            scene black with dspr

            play sound uved
            th "Вот чёрт, препод всё таки пришел… Придется возвращаться…"
            stop sound fadeout 0.5
        "Остаемся":
            $ svalil = False
            th "Нет, я не должен так поступать, ведь это неправильно."
            th "Я больше не могу ждать, нужно убедить других, чтобы не я один потом получил за то, что ушёл."

            show jeka serious with dspr
            show an happy at left with dspr

            an "Единственно верное решение."
            jeka "Ну ладно, давайте тогда, до завтра."
            play sound uved
            th "Вот чёрт, препод всё таки пришел… Придется возвращаться…"
            stop sound fadeout 0.5

    $ timeskip_short()
    scene college hallway with bkrr_timeskip_transition()
    
    show jeka serious with dspr
    show an normal at left with dspr
    play sound koridor
    jeka "А я говорил, что не стоит уходить. Сейчас бы не писали всей группой объяснительную."
    an "Ну, ничего. Как то всё равно, знаешь?"
    hero "В следующий раз я тебя обязательно послушаю. Но это не точно."
    jeka normal "Ты что то сказал?"
    hero "Говорю что ты прав, молодец."
    hero "Лично я не горю желанием оставаться на физру"
    hero "Так что всем до свидания, увидимся завтра!"
    jeka "Бывай, удачи."
    an "Пока."

    hide jeka
    hide an
    with dspr
    $ timeskip_short()
    scene bus stop evening with bkrr_timeskip_transition()


    play sound rington
    stop sound fadeout 0.5
    hero "Алло, да, здравствуйте."
    play music smert
    hero "В смысле? Этого не может быть!"
    hero "Буду через 5 минут."
    hero "Это просто невозможно…"
    hero "Почему именно она?"


    $ timeskip_short()
    scene home al morning with bkrr_timeskip_transition()
    show ma normal with dspr

    ma "Саша..."
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
    stop music fadeout 2.0

    scene park with dissolve
    play sound ulitsa
    th "Нужно срочно ехать домой, обдумать все."
    stop sound fadeout 0.5
    th "Осень будет холодной, да?"

    scene bus stop al with dspr
    $ renpy.pause(1.5)
    scene abobus with dspr
    $ timeskip_short()
    scene home gg evening with bkrr_timeskip_transition()


    play music despair

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
    th "Не сработало…"
    th "Вот же блин, я настолько сильно зациклился на эту ситуацию, что не заметил, как наступила глубокая ночь."
    th "Мне нужно отдохнуть, сегодня был слишком насыщенный день."
    stop music fadeout 3.0

    window hide
    $ renpy.pause(1.0)
    play music intro fadein 1.0
    scene black with dissolve
    $ renpy.pause(13.3, hard=True)
    show logo: 
        xalign 0.5 yalign 0.5 
    $ renpy.pause(7.8, hard=True)
    stop music fadeout 1.5
    window show

    jump second_day


label go_to_sec_seminar_first_day:
    th "Не не не, нет ничего важнее сна!"
    th " Я думаю, что если опоздаю на 1 пару, то ничего страшного не случится, ведь так? Ладно, это риторический вопрос."
    scene black with dspr
    show an angry with dspr
    
    an "КАК ТЕБЕ НЕ СТЫДНО ПРОГУЛИВАТЬ 1 ПАРУ?!"

    scene home gg morning with vpunch

    th " Вот чёрт, я опаздываю!"
    th "Ну вот, как знал, что нужно было идти в колледж… Ладно, опоздаю немного."
    stop music fadeout 1.0

    scene bus stop with dissolve

    play sound avtobus

    th "Мда уж, день начался очень и очень “хорошо”, в следующий раз сто процентов встаю и иду на первую пару!"

    scene abobus with dspr


    hero "Жесть, я еле успеваю к второй паре… Надо написать, что могу опоздать."


    $ timeskip_short()
    scene college stairs with bkrr_timeskip_transition()
    stop sound fadeout 1.5

    play sound koridor

    hero "Ничего себе, я еще и не опоздал!"

    ship "Посмотрите-ка, кто всё таки пришёл! Саша, ты ли это?"

    show ship surprised with dspr

    hero "Здравствуйте, Алина Алексеевна…"
    ship neutral "Ну здравствуй, скажешь, почему на паре не было?"
    hero "Нуууу…"
    ship happy "А ладно, я не настолько старая и ворчливая. Пока что."
    ship "Возьмешь у ребят задание, сделаешь дома и всё."
    hero "Хорошо, обязательно."
    th "Кто поверил…"
    ship neutral "Ты что-то сказал?"
    hero "Не не, вам послышалось наверное."
    ship "Ну ладно, поверю."
    
    play sound rksi

    stop sound fadeout 2.0


    $ timeskip_short()
    scene aud 2 people with bkrr_timeskip_transition()
    show jeka happy with dspr

    play sound koridor


    jeka "Здарова, ну ты и соня конечно."
    hero "Был бы я Соней, пришёл бы к первой паре."
    jeka normal "Да ладно, я не осуждаю же. Но ты побил рекорд Кубары, можешь гордиться собой."
    hero "Ха-ха-ха, как смешно."

    hide jeka
    show cube happy
    with dspr

    cube "О, привет!"
    hero "Привет-привет. Ты в кои-то веки пришла вовремя?"
    cube "Прикинь, я пришла вовремя!"
    hero "Умница, получается, эпоха опозданий пришла к концу?"
    cube "Ахахах, получается что так."
    cube normal "Кстати, тут какой-то человек странный отдал мне заколку…"
    hero "А зачем она мне?"
    cube "Она похожа на заколку, которая у Алины, вот я и подумала, что лучше тебе отдать. Ты же с ней вроде хорошо общаешься?"
    cube "В любом случае, учитывая длину твоих волос, то скорее всего ты эту заколку будешь использовать, а не Алина."
    hero "Ха-ха, смешно. Ты как там вообще, что нового?"
    cube "Ну знаешь, в принципе всё хорошо, вот с подружками из ИС-22 гуляла."
    hero "Снова променяла нас на ИС-22?"
    cube "Ну не правда, не меняла я вас."
    hero "Да да, не меняла."
    play sound steps
    cube surprised  "Ой, там ИС-22!"
    hide cube surprised with moveoutleft
    hero "Что и требовалось доказать…"

    stop sound fadeout 1.5

    $ renpy.pause(0.5)
    play sound koridor
    hero "Кстати, а какая у нас сейчас пара по расписанию?"

    show an normal with dspr 

    an "Программирование вроде."
    hero "О, Настя, привет."
    an "Ага, привет."
    an "В доту сегодня собираем стак?"
    hero "Почему нет, я только за. Жень?"

    show jeka normal at right with dspr

    jeka "Конечно, тогда сегодня день авантюрного манки кинга."
    jeka smirk "у а у а абезьяна прыгать"
    an surprise "Дурак?"
    jeka serious "Да за что?"
    hero "Ахахаха, как всегда, никто и ничто не меняется. И это радует."
    an normal "А?"
    an "Что с тобой? На какую то ваниль тебя пробило."
    jeka normal "Он вроде всегда был такой."
    an "Он раньше так не говорил."
    hero "Да ну ладно вам, просто в кои-то веки задумался, что в моей жизни наконец-то стало спокойно."
    hide jeka
    hide an
    with dspr
    th "Особенно после всего того, что было… {w}Ну ничего, справимся. И не с таким справлялись."

    $ renpy.pause(0.5)
    show an angry with dspr

    an "Хватит в облаках витать!"
    hero "ААААА!!"
    hero "Не пугай так."
    an normal "Чтобы не втыкал."

    show jeka serious at right with dspr
    
    jeka "Настя, не издевайся над человеком."
    jeka "И вообще, уже звонок по идее должен быть."
    play sound rksi
    hero "А вот и он. Вспомни лучик…"
    stop sound fadeout 1.0
    jeka "Вот и солнце, да?"
    hero "Учитывая нашу погоду сейчас, то за солнце говорить не приходится. Его попросту нет."

    hide jeka
    show an happy
    with dspr

    hero_na "Три дня дождей!"

    scene aud 2 people with dissolve

    hero "В целом, если подумать, то сегодняшний день в колледже не такой уж и сложный."
    hero "Скорее наоборот, сейчас будет пара программирования, а там в принципе интересно."
    
    show oleg _2 at right with dspr
    
    oleg "Уверен? Я думаю, что мне будет плохо…"
    hero "Это еще почему?"
    oleg "Знаешь, сколько у меня долгов?"
    hero "Даже знать не хочу."
    oleg "Ну вот и я о том же."

    $ renpy.pause(1.0)

    oleg "Ой, преподаватель пришел, все, потом поговорим."

    # show ship neutral at left with dspr
    # show ma neutral

    # ship "Всем здравствуйте! О, Филиппов, наконец-то вернулся. Ну рассказывай, как съездил, где побывал, что видел?"
    # oleg "Здравствуйте Алина Алексеевна, да всё хорошо, много чего видел."
    # ship "Это, конечно,  всё хорошо, но знаешь, что ты не сможешь увидеть?)"
    # oleg "Не… Не знаю..."
    # ship "Зачёт по моему предмету, если не сдашь мне все практические за 1 семестр)."


    scene black with dissolve

    # ship "Так, и сегодня мы начинаем изучать докер и все, связанные с ним команды."

    $ timeskip_short()
    scene college hallway with bkrr_timeskip_transition()  
    play sound rksi fadein 0.5  

    # hero "Блин, уже прошло 15 минут, а преподавателя всё нет, может быть уйти с пары?"
    # stop sound fadeout 1.0
    # show jeka serious with dspr
    # play sound koridor

    # jeka "Может всё таки дождемся преподавателя?"
    # hero "Правило 15 минут, помните?"

    # show an normal at left with dspr

    # an "Поддерживаю, как говорится, кто куда, а я домой."
    # jeka "Я всё таки подожду, мало ли, потом влетит ещё."
    # oleg "Ну ребята, давайте, до завтра, я в принципе не собирался оставаться на эту пару."
    # hero "Дилемма… Уйти или остаться?"

    # hide an
    # hide jeka
    # with dspr

    # $ timeskip_short()
    # scene college hallway with bkrr_timeskip_transition()
    
    show jeka serious with dspr
    show an normal at left with dspr
    play sound koridor

    hero "Лично я не горю желанием оставаться на физру"
    hero "Так что всем до свидания, увидимся завтра!"
    jeka "Бывай, удачи."
    an "Пока."
    stop sound fadeout 1.0

    hide jeka
    hide an
    with dspr
    $ timeskip_short()
    play sound rington
    scene bus stop evening with bkrr_timeskip_transition()

    hero "Алло, да, здравствуйте."
    stop sound fadeout 1.0
    hero "В смысле? Этого не может быть!"
    play music smert
    hero "Буду через 5 минут."
    hero "Это просто невозможно…"
    hero "Почему именно она?"

    $ timeskip_short()
    scene home al morning with bkrr_timeskip_transition()
    show ma normal with dspr

    ma "Саша..."
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
    stop music fadeout 1.0

    scene park with dissolve
    play sound ulitsa
    th "Нужно срочно ехать домой, обдумать все."
    th "Осень будет холодной, да?"
    stop sound fadeout 1.0

    scene bus stop al with dspr
    $ renpy.pause(1.5)
    scene abobus with dspr
    $ timeskip_short()
    scene home gg evening with bkrr_timeskip_transition()

    play music despair
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
    th "Не сработало…"
    th "Вот же блин, я настолько сильно зациклился на эту ситуацию, что не заметил, как наступила глубокая ночь."
    th "Мне нужно отдохнуть, сегодня был слишком насыщенный день."
    stop music fadeout 1.0

    window hide
    $ renpy.pause(1.0)
    play music intro fadein 1.0
    scene black with dissolve
    $ renpy.pause(13.3, hard=True)
    show logo: 
        xalign 0.5 yalign 0.5 
    $ renpy.pause(7.8, hard=True)
    stop music fadeout 1.5
    window show

    jump second_day

label stay_home_first_day:
    th " Да не, не хочу я сегодня идти на пары, уж лучше посплю, а там уже можно и постримить любимый валорант."

    
    scene black with dissolve
    show cube shade1 with dspr

    
    nn " Лучше иди в колледж, иначе ты пожалеешь!"

    scene home gg day with vpunch
    th "ААААААА"
    th "Что это было?!"
    th "Ладно, это же всего лишь сон, просто фантазия моего мозга."
    th "Пойду досыпать своё."

    $ timeskip_short()
    scene home gg day with bkrr_timeskip_transition()

    th "Сна ни в одном глазу. Особенно после того кошмара, что в общем-то и неудивительно."
    th "Ладно, пойду поиграю что-ли."


    $ timeskip_short()
    scene home gg evening with bkrr_timeskip_transition()

    th "Отлично сыграл, поднял себе золото, можно и отвлечься я думаю."
    th "А сколько время то?"
    "*на часах 19:34*"
    th "..."
    th "Ну…"
    th "Зато золото поднял."
    play sound rington
    hero "Алло, да, здравствуйте."
    stop sound fadeout 0.5
    stop music fadeout 1.0
    hero "В смысле? Этого не может быть!"
    play music smert
    hero "Буду через 5 минут."
    hero "Это просто невозможно…"
    hero "Почему именно она?"


    $ timeskip_short()
    scene home al morning with bkrr_timeskip_transition()
    show ma normal with dspr

    ma "Саша..."
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
    stop music fadeout 1.0

    scene park with dissolve
    play sound ulitsa

    th "Нужно срочно ехать домой, обдумать все."
    th "Осень будет холодной, да?"
    stop sound fadeout 1.5

    scene bus stop al with dspr
    $ renpy.pause(1.5)
    scene abobus with dspr
    $ timeskip_short()
    scene home gg evening with bkrr_timeskip_transition()
    play music despair


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
    th "Не сработало…"
    th "Вот же блин, я настолько сильно зациклился на эту ситуацию, что не заметил, как наступила глубокая ночь."
    th "Мне нужно отдохнуть, сегодня был слишком насыщенный день."
    stop music fadeout 1.5

    window hide
    $ renpy.pause(1.0)
    play music intro fadein 1.0
    scene black with dissolve
    $ renpy.pause(13.3, hard=True)
    show logo: 
        xalign 0.5 yalign 0.5 
    $ renpy.pause(7.8, hard=True)
    stop music fadeout 1.5
    window show

    jump second_day
