
def kelvintofah(temperature):
    assert((temperature >= 0), " Colder than absolute zero")
    return (((temperature-273)*1.8)+32)

print(kelvintofah(273))
print(int(kelvintofah(505.78)))
print(kelvintofah(-5))                                                                                                                          