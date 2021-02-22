timeOrder = ["acabou de abrir a plataforma", "há {0} minutos", "há {0} horas", "há {0} dias"]

def getTime(time):
    global timeOrder

    diff = (datetime.now() - time).total_seconds()
    index = 0
    
    for i in [60, 60, 24]:
        if diff >= i and index + 1 < len(timeOrder):
            diff = diff/i
            index += 1
        else:
            break

    diff = math.floor(diff)
    message = str(diff) + ' ' + timeOrder[index]
    
    if diff == 1:
        message = message[:-1]

    return message