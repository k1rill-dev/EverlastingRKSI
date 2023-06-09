label secret_ending:
    "Вы разблокировали секретную концовку!"
    "Наслаждайтесь)"
    $ renpy.movie_cutscene("audio/music/secret.webm")
    "И ещё"
    $ renpy.movie_cutscene("audio/music/rei.webm")
    $ persistent.chnomer = False
    return


label good_ending:
    $ persistent.good_ending = True
    scene home gg morning with dissolve
    play music samurai
    al "Проснись самурай, нам пора сжечь этот город."
    hero "А?"
    hero "Что?"

    scene home gg morning with dissolve
    window hide
    show blinking
    window show

    al "Бэ! Вставай давай, пора выбираться. Я поняла как нам это сделать."
    al "А вообще, ещё ты спал долго, а я завтрак приготовила, ну и вот как бы…"
    hero "О, спасибо большое!"
    al "Давай умывайся иди, а то стынет!"
    
    window hide
    $ timeskip_short()
    scene home gg morning with bkrr_timeskip_transition()
    window show

    hero "Итак, как нам выбраться?"

    show al seriuos with dspr

    al "Смотри, у нас есть две заколки."
    hero "И что? Надевать их на себя мы уже пробовали."
    al "Верно."
    al "Мы всё перепробовали."
    al smile "Кроме одного."
    hero "И что же это?"
    al "Выбросить их в Дон. Потом самим прыгнуть в то же место, куда бросили заколки."
    hero "Ты серьёзно? Почему именно в Дон?"
    hero "И зачем?"
    al "Мы перепробовали всё. Банально таки, это единственный вариант, как выбраться отсюда."
    al "Тем более, если не сработает, то мы не умрём в любом случае. Так что всё будет хорошо"
    hero "Думаешь?"
    al "Уверена. Давай доедай, и пойдем."
    al "Кстати, тебе понравилось?"
    hero "Да, было вкусно, спасибо."
    al "Не за что, пошли уже!"
    stop music fadeout 1.0

    scene most with dissolve
    show cube shade1 at right with dspr
    play music dovakin fadein 2.0
    play sound ulitsa

    nn "Ну здравствуйте, гости дорогие. Вы думали так легко от меня избавиться?"
    nn "Неа, ребятки, я тут оставаться не желаю"
    nn "Я ждал этого четыре, НЕТ ПЯТЬ ТЫСЯЧ лет!"
    nn "Вторая заколка найдена."
    nn "Отдай."
    hero "Ты случаем не охренел? Дружище, иди спокойно куда шёл, а нам не мешай."
    nn "Да-да, никогда ничего не бывает легкого… " with vpunch

    show al grin at left with dspr

    al "Оп, а это мне. И теперь заколки у меня, что ты сделаешь?"
    nn "Ты сейчас серьёзно?"
    nn "Ты угрожаешь мне?"
    nn "Отдай их. Сейчас же."
    al "Ага, много хочешь."
    
    al "Ну теперь всё зависит от тебя."
    nn "Ты уже от стольких лет с катушек слетела?"
    nn "С кем ты говоришь?"
    al "С моей головой всё в порядке. А вот с твоей, секунд через 10 случится кое-что."
    nn "Ты о чём?"
    
    show cube shade1 at right with dspr
    hide cube shade1 with hpunch 

    al "А разговоров то было."
    hero "И теперь что? Пусть здесь лежит?"
    al "Смерти он не заслуживает. Пусть вечно будет в этом цикле. То есть, пусть лежит."
    al "А нам пора, мы уже сильно задержались тут."
    stop music fadeout 1.0
    stop sound fadeout 2.0

    $ renpy.pause(1.0)
    play music den fadein 2.0

    hero "Страшно."
    al "Мне тоже… "
    hero "Всё хорошо будет. На счёт “три” прыгаем."
    al "Раз."
    hero "Два."
    "Три!"

    scene black with dissolve


    al "Доктор, он кажется, в себя приходит!"
    doc "Слава богу…"
    doc "Ты слышишь меня?"
    
    window hide
    show blinking
    scene hospital with dissolve
    show blinking
    $ renpy.pause(1.5)
    window show

    show doc browraised with dspr

    doc "Александр?"
    hero "Где я?.."

    show al sadness close eyes at right with dspr 

    al "Он очнулся… Я так рада…"
    doc "Ты в больнице. Ты попал в аварию."
    hero "Что?.. Лин, мы выбрались?"
    al "Откуда? Вот ты выбрался - с того света… Дурак…"
    al "Зачем надо было закрывать меня?.."
    hero "Мне все приснилось…"
    doc "Ты лежал в коме месяц. Вот тебе наверное и приснилось что-то."
    hero "Месяц?.."
    al smile "Да. Мне повезло, отделалась ушибами. А ты… Дурак… Зачем?.. Если бы ты не выжил?.."
    doc "Я вас оставлю лучше. Приду через полчаса где-то."

    hide doc with moveoutleft

    hero "Ты бы знала, какой сон мне приснился… Слава богу, что это всего лишь сон."
    hero "Всего лишь сон."

    stop music fadeout 1.0
    window auto

    scene black with dissolve
    play music achievement
    show achievement_good: 
        xalign 0.95 
        yalign 0.95
    # play sound achievement
    $ renpy.pause(2.5)
    stop music

    jump titr
    


label bad_ending:  
    $ persistent.bad_ending = True
    scene home gg morning with dissolve
    window hide
    show blinking
    window show
    play music samurai

    al "Проснись самурай, нам пора сжечь этот город."
    hero "А?"
    hero "Что?"

    show al smile with dspr

    al "С новым днём цикла!"
    hero "Тебя тоже…"
    al "Что такой грустный?"
    hero "А ты больно весёлая я погляжу."
    al "Ну а чего грустить?"
    al seriuos "Я кажется поняла как выбраться!"
    hero "О, и как?"
    al cringe "”О, и как?”"
    al "Вот и вся реакция?"
    al smile "Давай ешь, пойдем потом выбираться отсюда."
    hero "Итак, как нам выбраться?"
    al seriuos "Смотри, у нас есть заколка."
    hero "И что? Что мы только с ними не делали..."
    al "Верно."
    al "Мы всё перепробовали."
    al normal "Кроме одного."
    hero "И что же это?"
    al "Выбросить в Дон. Потом самим прыгнуть в то же место, куда бросили заколку."
    hero "Ты серьёзно? Почему именно в Дон?"
    hero "И зачем?"
    al "Мы перепробовали всё. Банально таки, это единственный вариант, как выбраться отсюда."
    al "Тем более, если не сработает, то мы не умрём в любом случае. Так что всё будет хорошо"
    hero "Думаешь?"
    al "Уверена. Давай доедай, и пойдем."
    al smile "Кстати, тебе понравился завтрак?"
    hero "Да, было вкусно, спасибо."
    al "Не за что, пошли уже!"
    stop music fadeout 1.0
    
    scene most with dissolve
    play sound ulitsa

    hero "Не уверен я в этом…"

    show al smile at left with dspr
    
    al "Всё будет хорошо!"
    al "Не переживай."
    al "В любом случае, есть мы друг для друга. Не пропадём!"
    hero "Тогда давай закончим поскорее."
    
    $ renpy.pause(1.5)

    hero "Страшно."
    al "Мне тоже… "
    hero "Всё хорошо будет. На счёт “три” прыгаем."
    al "Раз."
    hero "Два."
    "Три!"
    stop sound fadeout 1.0

    scene black with dissolve
    $ renpy.pause(2.0, hard=True)
    scene home gg morning with dissolve
    show blinking
    $ renpy.pause(2.0, hard=True)
    play music nkr

    hero "Новый день?"

    show al sad with dspr

    al "Старый."
    hero "Не получилось?"
    al sadness close eyes "Нет. Прости… Я была уверена что получится, но будто бы чего-то не хватает… "
    hero "Да ладно уже. Наверное найдем выход."
    al sad "Наверное…"
    al "Другого выхода нет!"
    al "И не будет!"
    al sadness close eyes "Нам с тобой некуда бежать, понимаешь?"
    al "Выхода нет!"
    hero "Разберемся, не переживай."
    hero "Все будет хорошо."
    
    window hide
    $ timeskip_short()
    scene home gg day with bkrr_timeskip_transition()
    window show

    hero "Я устал, Алин…"

    show al sadness close eyes with dspr

    al "Я тоже."
    hero "Что будем делать?"
    al normal "Пытаться дальше. Ещё и незнакомец пропал куда-то."
    hero "Прорвёмся!"
    
    window hide
    $ timeskip_short()
    scene naberezhnaya with bkrr_timeskip_transition()
    window show
    show al smile with dspr

    al "Знаешь…"
    hero "Что?"
    al "Я тут подумала…"
    play sound bulk fadein 2.0
    hero "И что же ты надумала?"
    stop sound fadeout 1.5
    hero "Зачем?!"
    al "Всё равно она бесполезна."
    al "Провести вечность вот так?"
    al "Звучит неплохо…"
    hero "Что?"
    al normal "Не, ничего."
    hero "Знаешь, я кажется понял."
    al "Что ты понял?"
    hero "Нам с тобой некуда бежать. Судьба такая наверное."
    al smile "Фаталистом стал?"
    hero "Ну почти."
    hero "Думаю, что нас выпустят отсюда, когда придет время. Надо просто подождать."
    al "У нас с тобой в запасе вечность, некуда торопиться."
    al "И бежать тоже…"

    scene black with dissolve
    stop music fadeout 0.5

    scene tv without news with dissolve
    $ renpy.pause(1.5, hard=True)
    scene tv news with dissolve

    tv "Здравствуйте, время новостей на 7-8 канале, о самых важных событиях расскажем вам прямо сейчас."
    tv "Сегодня утром произошла страшная авария на перекрестке Ворошиловского и Большой Садовой в городе Ростове-на-Дону."
    tv "Столкнулся автобус и фура. Выжили только двое, парень и девушка. Девушка пришла в сознание, а парень лежит в коме."

    window hide

    scene black with dissolve
    play music achievement
    show achievement_bad: 
        xalign 0.95 
        yalign 0.95
    # play sound achievement
    $ renpy.pause(2.5)
    stop music

    jump titr

init:
    transform txt_up:
        yalign -0.5
        linear 90.0 yalign 1.5
    

label titr:
    play music end fadein 2.0
    scene black with dissolve
    show text 'Идея: Лютый Николай, Белокобыльский Кирилл{p} \n Продюсер, Режиссёр: Лютый Николай, Белокобыльский Кирилл{p}\n Программисты: Лютый Николай, Белокобыльский Кирилл{p} \nГлавные сценаристы: Лютый Николай, Белокобыльский Кирилл{p} \nСценаристы: Лютый Николай, Белокобыльский Кирилл{p} \nЗвукорежиссёр: Лютый Николай{p} \nВ визуальной новелле использовалась данная музыка:{p} \nPyrokinesis, МУККА - Днями-ночами;{p} \nPyrokinesis - Цветами радуги;{p} \nМУККА - Интро;{p} \nPyrokinesis, МУККА, Booker - Некуда бежать;{p} \nDora - Осень пьяная;{p} \nDora - Втюрилась;{p} \nPyrokinesis - Я приду к тебе с клубникой в декабре;{p} \nТДД - Демоны;{p} \nPyrokinesis - Вечно 17;{p} \nPyrokinesis - Молот ведьм(Remastered);{p} \nPyrokinesis - Терновый венец эволюции;{p} \nThe Cat Empire - The Lost Song{p} \nАвторы благодарят за помощь в создании визуальной новеллы{p} \nМанакову Ольгу Петровну за возможность реализовать данную идею и получить за неё автомат{p} \nСоздателей Renpy за упрощение в написании игры данного жанра{p} \nБлагодарим всех, кто прошёл данную игру и желаем никогда не сдаваться и идти до конца, ведь{p} \nвойн без потерь не бывает, и иногда победа приносит столько потерь, что больше похоже на поражение.{p} \nВойна всегда непредсказуема — твой противник может стать твоим союзником, если у вас двоих появляются общие интересы.{p} \nБольше всего от войны страдают невинные, которые оказались втянуты в сражение против своей воли.{p} \nВойна — это путь обмана. И порой обманутым оказываешься ты сам.{p} \nИ в заключение хочется сказать, что у каждой истории есть начало и конец.{p} \nУ каждой истории есть своя канва, синопсис, содержание, ключевые моменты, прологи и эпилоги. И нет такой книги, в которой при каждом новом прочтении не открывались бы вещи, на которые раньше не обращал внимания.{p} \nУ каждой истории есть начало и конец. \nПочти у каждой...{p} \n' at txt_up
    pause 100
    return