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


init 1:

    # переменные-флаги
    $ is_go_to_first_seminar = False
    $ is_go_to_sec_seminar = False
    $ svalil = False
    $ zakolka = False
    $ is_stay_home_homie = False
    $ persistent.chnomer = False

    #потом поменять цвета
    $ th = Character(u'Мысли', color="#FFA500", what_color="E2C778")
    $ hero = Character(u'Саша', color="#7ec557", what_color="E2C778")
    
    $ al = Character(u'Алина', color="#55a9c1", what_color="E2C778")
    $ nn = Character(u'Незнакомец', color="#351868", what_color="E2C778")
    $ jeka = Character(u'Женя', color="#41c59d", what_color="E2C778")
    $ cube = Character(u'Кубара', color="#d5c91c", what_color="E2C778")
    $ oleg = Character(u'Олег', color="#06851c", what_color="E2C778")
    $ ship = Character(u'Алина Алексеевна', color="#45dec5", what_color="E2C778")
    $ an = Character(u'Настя', color="#d4ad64", what_color="E2C778")
    $ tv = Character(u'Диктор', color="#4800ff", what_color="E2C778")
    $ ma = Character(u'Мария Васильевна', color="#82e70f", what_color="E2C778")
    $ doc = Character(u'Врач', color="#278b81", what_color="E2C778")
    $ hero_na = Character(u'Саша и Настя', color="#FFA500", what_color="E2C778")


    $ define_assets('images/sprites')
    $ define_assets('audio/music')

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