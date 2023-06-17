# обозначаем персонажей

# г - Черил Кирякукин(мысля)
# гг - Черил Кирякукин
# фз(френдзона, френдзона) - подружка по имени Алина(то есть я)))90))990))))))
# н - незнакомец   
# ж - жека
# куб - кубарОчка
# о - олег      
# щ - щипанкина   
# на - АНАСТАСИЯ АНТОНОВА 
# к - киря       
# ма - мать Алины
# вр -  врач			
init python:
    BKRR_ROOT_DIR = ""
    BKRR_ES_IMAGES = "images/"
    BKRR_IMAGES = BKRR_ROOT_DIR + "images/"

    bkrr_circlein_transition = ImageDissolve(BKRR_IMAGES + "transitions/circle.png", 0.5, ramplen=5, reverse = True, alpha=True)
    bkrr_circleout_transition = ImageDissolve(BKRR_IMAGES + "transitions/circle.png", 0.5, ramplen=5, reverse = False, alpha=True)
    bkrr_star_falling_transition = ImageDissolve(BKRR_IMAGES + "transitions/star_falling.png", 1.0, ramplen=5, reverse = False, alpha=True)

    bkrr_blindstoleft_transition = ImageDissolve(BKRR_IMAGES + "transitions/blinds_h.png", 1.0, ramplen=25, reverse = False, alpha=True)
    bkrr_blindstoright_transition = ImageDissolve(BKRR_IMAGES + "transitions/blinds_h.png", 1.0, ramplen=25, reverse = True, alpha=True)
    bkrr_blindstotop_transition = ImageDissolve(BKRR_IMAGES + "transitions/blinds_v.png", 1.0, ramplen=25, reverse = False, alpha=True)
    bkrr_blindstobottom_transition = ImageDissolve(BKRR_IMAGES + "transitions/blinds_v.png", 1.0, ramplen=25, reverse = True, alpha=True)

    def bkrr_timeskip_transition(t=1.0):
            return ImageDissolve(BKRR_IMAGES + "transitions/timeskip.png", t, ramplen=0, reverse=False, alpha=True)

    def timeskip_short():
            renpy.play(clock_transition_sound, channel="sound")
            renpy.scene()
            renpy.show("black")
            renpy.with_statement(bkrr_timeskip_transition())
            renpy.music.stop(channel="sound", fadeout=1.0)

init 1:
    
    $ dspr = Dissolve(time=0.2)

    # переменные-флаги
    $ is_go_to_first_seminar = False
    $ is_go_to_sec_seminar = False
    $ svalil = False
    $ zakolka = False
    $ is_stay_home_homie = False
    $ persistent.chnomer = False

    #потом поменять цвета
    $ th = Character(u'Мысли', color="#FFA500", what_color="#ffffff")
    $ hero = Character(u'Саша', color="#7ec557", what_color="#ffffff")
    $ al = Character(u'Алина', color="#55a9c1", what_color="#ffffff", image='al')
    $ nn = Character(u'Незнакомец', color="#351868", what_color="#ffffff", image='nn')
    $ jeka = Character(u'Женя', color="#41c59d", what_color="#ffffff", image='jeka')
    $ cube = Character(u'Кубара', color="#d5c91c", what_color="#ffffff", image='cube')
    $ oleg = Character(u'Олег', color="#06851c", what_color="#ffffff", image='oleg')
    $ ship = Character(u'Алина Алексеевна', color="#45dec5", what_color="#ffffff", image='ship')
    $ an = Character(u'Настя', color="#d4ad64", what_color="#ffffff", image='an')
    $ tv = Character(u'Диктор', color="#4800ff", what_color="#ffffff")
    $ ma = Character(u'Тетя Маша', color="#82e70f", what_color="#ffffff", image='ma')
    $ doc = Character(u'Врач', color="#278b81", what_color="#ffffff", image='doc')
    $ hero_na = Character(u'Саша и Настя', color="#FFA500", what_color="#ffffff")

    #Музыка и звуки
    $ intro_games = "audio/music/vturilas.mp3"
    $ grust = "audio/music/grust.mp3"
    $ budilnik = "audio/sound/budilnik.mp3"
    $ avtobus = "audio/sound/avtobus.mp3"
    $ avtobus_musik = "audio/music/intro.mp3"
    $ koridor = "audio/sound/koridor.mp3"
    $ steps = "audio/sound/steps.mp3"
    $ rksi = "audio/sound/rksi.mp3"
    $ uved = "audio/sound/iphone.mp3"
    $ ulitsa = "audio/sound/ulitsa.mp3"
    $ rington = "audio/sound/rington.mp3"
    $ smert = "audio/music/smert.mp3"
    $ despair = "audio/music/despair.mp3"
    $ gudki = "audio/sound/gudki.mp3"
    $ sbros = "audio/sound/bb.mp3"
    $ tve = "audio/music/TVE.mp3"
    $ three = "audio/music/three.mp3"
    $ posidelka = "audio/music/posidelka.mp3"
    $ pridu = "audio/music/pridu.mp3"
    $ samurai = "audio/music/pridu.mp3"
    $ dovakin = "audio/music/dovakin.mp3"
    $ den = "audio/music/den.mp3"
    $ nkr = "audio/music/nkr.mp3"
    $ end = "audio/music/end.mp3"
    $ bulk = "audio/sound/voda.mp3"
    
    $ clock_transition_sound = "audio/sound/clock_transition_sound.ogg"
    $ define_assets('images/sprites')
    $ define_assets('images/bg')
    $ define_assets('audio/music')
    image anim blink_down = "images/blink_down.png"
    image anim blink_up = "images/blink_up.png"
    image unblink:
        contains:
            "anim blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "anim blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image blink:
        contains:
            "anim blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "anim blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0


    image blinking:
        contains:
            "anim blink_up"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "anim blink_down"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0
        pause 2.0
        contains:
            "anim blink_up"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "anim blink_down"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)


init python:
    import os
    def get_username_pc():
        if os.name == 'nt':
            for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                username = os.environ.get(name)
        
        elif os.name == 'posix':
            for user in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                username = os.environ.get('USER')
        else:
            username = None
        
        return username