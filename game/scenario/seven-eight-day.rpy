label seven_eight_day:

    scene home gg morning with dissolve

    th "Уже неделя?"
    th "Или больше?"
    th "Каждый день как дубликат…"
    th "Еще и Алина куда-то исчезла."
    th "Она 100% связана со всей этой чертовщиной."
    th "Ещё и эта заколка…"
    th "Зачем она мне? Просто бесполезная вещица."
    th "Хотя…"
    th "Не, сомневаюсь что она будет нужна в будущем."
    th "Хотя как напоминание о ней…"
    
    menu:
        "Выбросить":
            $ zakolka = False
            th "Нет, зачем она мне?"
            "*Кидает в мусор*"
            th "Ну и поделом ей, смысла от неё не было."
        "Оставить":
            $ zakolka = True
            th "Нет, оставлю."
            th "Вдруг, понадобится ещё. Хотя сомневаюсь…"

    th "Я… Нет, я её найду и расспрошу обо всём."
    th "Нельзя опускать руки, вдруг я всё таки найду её."
    th "Хотя после недели безрезультатных поисков как-то надежда уже лежит на аппарате искусственного поддержания жизни."
    th "Ещё и этот силуэт… Кто это?"
    th "Он так со мной и не связался до сих пор."
    th "Он тоже что-то знает, я уверен!"
    hero "А… Алина?!"
    hero "Алло, Алина?! Ты где, нам срочно надо встретиться!"
    al "Через час в парке Горького. Без опозданий"
    hero "Алина, что…"
    th "Не похоже это на неё. Она никогда так не делала. И не сделала бы, я уверен."
    th "Хотя учитывая то, что происходит сейчас, я не берусь утверждать, что знаю человека хорошо."
    th "Идти ли мне на встречу?"
    "итак, тут по факту уже финалОчка, все выйдет в страниц 40 я думаю. Я сначала фулл распишу ветку самой самой аху… Кхм, крутой концовки с главным сюжетным твистом."
    th "Это не Алина."
    th "Уж за 10 лет я её хоть немного, но знаю."
    th "И что теперь делать?"

    $ timeskip_short()
    scene home gg morning with bkrr_timeskip_transition()

    th "А вдруг это всё таки была Алина?"
    th "Ладно, я всё равно ничего не теряю, надо пойти и проверить."
    # "*собирается*"
    # "бля у меня была гачи гифка, где ван даркхолм одевается, но я её потерял"
    # "*на выходе из дома, в коридоре*"

    

    th "Так, надеюсь, это действительно Алина."
    th "Я очень надеюсь что с ней всё хорошо…"
    "*выходит из двери подъезда*"
    al "ОЙ!"
    hero "А? Что?"
    hero "Алина?"
    al "Что? Будто призрака увидел, ей богу."
    hero "Так и есть. Я призрака увидел."
    al "Ха-ха-ха, как смешно."
    hero "Что ты тут делаешь? Ты же мне звонила, приглашала в парк на встречу…"
    al "Ты таблетки выпить забыл или у тебя уже глюки пошли? Я тебе не звонила."
    hero "А кто тогда мне звонил?"
    al "Я что, знаю?"
    hero "Давай ты зайдешь может?"
    al "Слава богу ты догадался, давай, зайду."
    "*в комнате*"
    hero "Итак, что ты тут делаешь, что тут происходит, почему я в каком то…"
    al "Тише, тише. По одному вопросу, пожалуйста. Я отлично понимаю твои чувства, но если бы не я - ты бы уже плавал в реке Дон."
    hero "Почему ещё?"
    al "А, ты ещё с ним не сталкивался…"
    hero "С кем?"
    al "С ним. Больше тебе знать не надо, поверь, я не причиню тебе вреда."
    hero "..."
    hero "Лин, как давно ты так живёшь?"
    al "Не знаю. Долго. Очень долго."
    al "Я потеряла счет пару лет назад."
    hero "Л-лет?.."
    al "Да, что ты думал? Тот незнакомец уже тысячелетия ищет способ выбраться. "
    al "А я пытаюсь от него сбежать. Мне не справиться с ним в одиночку."
    al "И скажу на опережение - нам вдвоём тоже не справиться."
    al "Так пусть он убивает меня, чем нас двоих. Была надежда на тебя, вдруг ты что-то придумал бы."
    al "Не думай, я на тебя не наговариваю."
    al "Я за столько лет не смогла, а ты за неделю… Так что всё хорошо."
    hero "Алина, так нельзя! Мы бы вместе что-то придумали, мы обязательно выберемся."
    al "Наивный был, наивным и остался. Ни у кого нет ключа."
    al "Просто нет. Отсутствует."
    al "Может, его и не существует…"
    "БЛЯ Я ХОЧУ ВАНИЛИ ИДИ НАХУЙ"
    "так сказать некоторого рода предупреждение, щас будет ванилька"
    al "Я устала…"
    al "Я не хочу ничего. Просто убейте меня уже."
    al "Я даже умереть не могу."
    al "Я просыпаюсь в новом дне. Каждый. Мать его. Раз."
    al "Это пытка, пожалуйста, прекратите…"
    al "За что это мне?"
    al "ПОЧЕМУ Я?"
    al "ПОЧЕМУ ТЫ?"
    hero "Всё будет хорошо, мы вместе справимся со всем. Не переживай, Лин. Мы вдвоем справимся со всем."
    al "Ты не понимаешь…"
    hero "И что? Благодаря твоему опыту мы сможем что-то придумать. Не унывай, ещё не всё потеряно."
    th "Вряд-ли что-то выйдет, ну да ладно, унывать тоже не вариант."
    al "Я хочу тебе ещё кое-что рассказать…"
    al "Лет так 7-8 назад я поговорила с ним. Он сказал, что единственный способ выбраться - убить тебя"
    al "Я не смогла."
    al "И не смогу."
    al "Я уверена, что есть другой способ!"
    hero "Ну… Ладно."
    hero "Ты нашла этот способ?"
    al "Я знаю, что есть ключи. Но не знаю как они выглядят."
    hero "Значит, нам их надо найти? Есть идея, где искать?"
    al "Есть пара идей, но…"
    hero "Никаких “но”, давай, идём!"
    al "Идти никуда не надо, пошли обыскивать твой дом."
    hero "А? Зачем?"
    al "За шкафом, давай открывай и ищи все подозрительные вещи."
    "*таймскип*"
    al "Боже, зачем тебе PSP?"
    hero "Отдай, это вообще-то память!"
    al "Ох… Ты не меняешься никогда. Это и хорошо."
    hero "Ты что-то сказала?"
    al "Нет, ищи давай!"
    "*еще через время*"
    hero "Стой…"
    al "М? Ты что-то нашел?"

    if zakolka:
        jump is_zakolka_true
    else:
        jump is_zakolka_false

label is_zakolka_true:
    hero "Вот она! Заколка!"
    al "Заколка? Ты серьёзно? И откуда она у тебя?"
    al "У тебя есть девушка?!"
    hero "Неет, мне Кубара отдала, так как сказала что это твоя заколка. Попросила передать так-то."
    al "Хм…"
    al "Стоять."
    al "Быстро собираемся и ко мне домой."
    hero "Зачем?"
    al "Без лишних разговоров. Быстрее я сказала!"
    "*дома у Алины*"
    al "Узнаешь?"
    hero "Заколка… Та же самая…"
    al "Кажется, мы нашли ключ. Эту заколку мне также отдала Кубара. "
    hero "Теперь осталось понять, как нам их использовать?"
    al "Ага."
    
    jump good_ending

label is_zakolka_false:
    al "Лично я в твоём бардаке ничего не нашла."
    hero "Я тоже…"
    hero "Что делать будем?"
    al "Продолжим поиски в другом месте."
    hero "Каком?"
    al "У меня есть пара идей, пошли."
    hero "Давай потом перепроверим твою квартиру, может что-то упустили?"

    jump bad_ending

