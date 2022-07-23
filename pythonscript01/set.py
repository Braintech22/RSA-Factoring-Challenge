from typing import Set


countries = set(("nigeria", "Benin", "ghana"))

print (countries)

countries.add("togo")

print(countries)

countries.remove("togo")

print(countries)

countries2 = set(["nigeria", "Benin", "ghana"])

print(countries)

countries2.remove("ghana")

print(countries2)

countries2.pop("nigeria")

print(countries2)