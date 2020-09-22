print('Привет! Я древнерусский конвертеръ единиц изменения!')
print('Я переведу Ваши сантиметры, метры или километры')
print('в одну из единиц измерения Дневней Руси:')
print('пядь, локоть, аршин, сажень, верста и миля!')
print('Для начала введите единицу измерения, которую будем переводить.')
print('Я принимаю варианты только: см, м, км')
input_measurement = str(input())
if input_measurement not in ['см', 'м', 'км']:
    print('Я не играю в нечестные игры. О правилах ты был предупрежден.')
    exit()
else:
    print('Хорошо! Теперь введите число')
    value = float(input())
    # Чтобы было легче конвертировать, переведем исходное число в сантиметры.
    if input_measurement == 'м':
        value = value * 100
    if input_measurement == 'км':
        value = value * 1000 * 100
    print('Теперь нужно выбрать, во что переводить!')
    print('Введите одно из следующих понятий:')
    print('пядь, локоть, аршин, сажень, верста, миля.')
    print('Я выведу число и три знака после запятой.')
    output_measure = str(input())
    if output_measure == 'пядь':
        print('1 пядь это 17.78см')
        print('У вас тут пядей:', float('{:.3f}'.format(value/17.8)))
    elif output_measure == 'локоть':
        print('1 локоть это 53.34см')
        print('У вас тут локтей:', float('{:.3f}'.format(value/53.34)))
    elif output_measure == 'аршин':
        print('1 аршин это 71.12см')
        print('У вас тут аршинов:', float('{:.3f}'.format(value/71.12)))
    elif output_measure == 'сажень':
        print('1 сажень это 213.36см')
        print('У вас тут саженей:', float('{:.3f}'.format(value/213.36)))
    elif output_measure == 'верста':
        print('1 верста это 1066,8м')
        print('У вас тут верст:', float('{:.3f}'.format(value/106680)))
    elif output_measure == 'миля':
        print('1 миля это 7,47км')
        print('У вас тут миль:', float('{:.3f}'.format(value/747000)))
    else:
        print('Я Вас не понял')
        print('Убедитесь, что Вы вводите символы именно так, как я прошу.')
