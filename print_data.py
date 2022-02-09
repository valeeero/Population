from models import Population

results = Population.query.all()
asia_pop = 0
eu_pop = 0
america_pop = 0
africa_pop = 0
oceanic_pop = 0
world_pop = 0

i = 0

asia_dict = {}
africa_dict = {}
americas_dict = {}
europe_dict = {}
oceania_dict = {}


class min_max():
    def min_dict(self, dict_country):
        min_value = min(dict_country, key=dict_country.get)
        for k, v in dict_country.items():
            if k == min_value:
                return [min_value, v]

    def max_dict(self, dict_country):
        max_value = max(dict_country, key=dict_country.get)
        for k, v in dict_country.items():
            if k == max_value:
                return [max_value, v]


for el in results:
    if i < len(results):
        test = repr(results[i]).replace(",", "").split("'")[1:-1]
        if test[2] == "Asia":
            asia_pop += int(test[4])
            asia_dict[test[0][4:]] = int(test[4])
        elif test[2] == "Americas":
            america_pop += int(test[4])
            americas_dict[test[0][4:]] = int(test[4])
        elif test[2] == "Africa":
            africa_pop += int(test[4])
            africa_dict[test[0][4:]] = int(test[4])
        elif test[2] == "Europe":
            eu_pop += int(test[4])
            europe_dict[test[0][4:]] = int(test[4])
        elif test[2] == "Oceania":
            oceanic_pop += int(test[4])
            oceania_dict[test[0][4:]] = int(test[4])
        i += 1

print(f'Asia -> {asia_pop}')
print(f'Africa -> {africa_pop}')
print(f'Americas -> {america_pop}')
print(f'Europe -> {eu_pop}')
print(f'Oceania -> {oceanic_pop}')

print("#" * 50, "!The population of the largest country in the region!", "#" * 45)
print("#" * 150)
print("#" * 50, "_" * 22, "ASIA", "_" * 22, "#" * 48)

print(min_max().max_dict(asia_dict)[0])
print(min_max().max_dict(asia_dict)[1])

print("#" * 50, "_" * 21, "AFRICA", "_" * 21, "#" * 50)

print(min_max().max_dict(africa_dict)[0])
print(min_max().max_dict(africa_dict)[1])

print("#" * 50, "_" * 21, "AMERICA", "_" * 20, "#" * 50)

print(min_max().max_dict(americas_dict)[0])
print(min_max().max_dict(americas_dict)[1])

print("#" * 50, "_" * 21, "EUROPE", "_" * 21, "#" * 50)

print(min_max().max_dict(europe_dict)[0])
print(min_max().max_dict(europe_dict)[1])

print("#" * 50, "_" * 21, "OCEANIA", "_" * 20, "#" * 50)

print(min_max().max_dict(oceania_dict)[0])
print(min_max().max_dict(oceania_dict)[1])
print("#" * 150)

print("#" * 50, "!The population of the smallest country in the region!", "#" * 44)
print("#" * 150)
print("#" * 50, "_" * 22, "ASIA", "_" * 22, "#" * 48)

print(min_max().min_dict(asia_dict)[0])
print(min_max().min_dict(asia_dict)[1])
print("#" * 50, "_" * 21, "AFRICA", "_" * 21, "#" * 50)
print(min_max().min_dict(africa_dict)[0])
print(min_max().min_dict(africa_dict)[1])
print("#" * 50, "_" * 21, "AMERICA", "_" * 20, "#" * 50)
print(min_max().min_dict(americas_dict)[0])
print(min_max().min_dict(americas_dict)[1])
print("#" * 50, "_" * 21, "EUROPE", "_" * 21, "#" * 50)
print(min_max().min_dict(europe_dict)[0])
print(min_max().min_dict(europe_dict)[1])
print("#" * 50, "_" * 21, "OCEANIA", "_" * 20, "#" * 50)
print(min_max().min_dict(oceania_dict)[0])
print(min_max().min_dict(oceania_dict)[1])
print("#" * 150)
