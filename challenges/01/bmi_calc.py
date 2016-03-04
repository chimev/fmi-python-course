def body_mass_index(weight, height):
    return round(weight/(height ** 2), 1)


def shape_of(weight, height):
    result = body_mass_index(weight, height)

    if result <= 15:
        return 'тежко недохранване'
    elif 15 < result <= 16:
        return 'средно недохранване'
    elif 16 < result <= 18.5:
        return 'леко недохранване'

    elif 18.5 < result <= 25:
        return 'нормално тегло'
    elif 25 < result <= 30:
        return 'наднормено тегло'

    elif 30 < result <= 35:
        return 'затлъстяване I степен'
    elif 35 < result <= 40:
        return 'затлъстяване II степен'
    elif 40 < result:
        return 'затлъстяване III степен'

    else:
        return None
