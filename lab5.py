class Logger:
    def __init__(self, func):
        print('> Класс Logger метод __init__ успешный запуск')
        self.func = func

    def __call__(self):
        print('> Проверка перед запуском', self.func.__name__)
        self.func()
        print('> Проверка безопасного выключения')

@Logger
def site():
    print('Усердная работа сайта')

site()