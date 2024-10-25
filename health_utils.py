def calculate_bmi(height, weight):
    """Calcule l'indice de masse corporelle (IMC) à partir de la taille en mètres et du poids en kilogrammes."""
    return weight / (height ** 2)

def calculate_bmr(height, weight, age, gender):
    """Calcule le taux métabolique de base (BMR) en utilisant l'équation de Harris-Benedict."""
    if gender.lower() == 'male':
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == 'female':
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        return "Invalid gender"

