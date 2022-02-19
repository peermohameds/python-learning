def height_imp_to_metric(feet, inch=0):
    return feet * 0.3048 + inch * 0.0254


def weight_lbs_to_kgs(lbs):
    return lbs * 0.45359237


def bmi(weight, height):
    return weight / height ** 2


print(bmi(weight_lbs_to_kgs(145), height_imp_to_metric(5,8)))
print(bmi(70, height_imp_to_metric(5,8)))