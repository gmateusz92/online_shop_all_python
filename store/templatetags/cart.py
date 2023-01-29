from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False

# Użyliśmy dekoratora rejestru, aby sprawdzić, czy produkt znajduje się w koszyku, czy nie.
#  Najpierw chwytamy wszystkie klucze do wózka. Kluczem tutaj jest identyfikator produktu.
#  A jeśli wartość całkowita tego identyfikatora jest równa identyfikatorowi produktu,
#  oznacza to, że produkt jest w koszyku, w przeciwnym razie nie ma go w koszyku.

#Teraz zastosujmy ten filtr w naszym home.htmlpliku. W tym celu na górze musimy załadować nasz cart.py plik.
#  Więc piszemy. {% load cart %}