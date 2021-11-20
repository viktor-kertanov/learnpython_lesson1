from dataclasses import dataclass

country = {
    "city": "Moscow",
    "temperature": "20",
    "date": "27.05.2019"
}

@dataclass
class Country:
    "Class for countries"
    city: str
    temperature: str
    date: str

#country = Country(city="Moscow", temperature="20", date="27.05.2019")

country_class = Country(**country)

print(type(country_class))

print(country_class.city)
print(country_class.temperature)
print(country_class.date)

print("-"*50)

# print(country["city"])
# country["temperature"] = str(int(country["temperature"])-5)
#
# print(country)
#
# print(country.get("country","Russia"))
#
# country["date"] = "27.05.2019"
# print(len(country))
# print(country)
