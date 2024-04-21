import os

"""
Fuzzy search refers to searching for similar strings in the records instead of the exact same one. This is useful in many scenarios as typo is extremely common thing.

There are various ways to implement fuzzy serch. Among them, Levenstein's distance is one way to approximate the search term.

Levenstein's distance:
    - It provides the minimum changes required between two terms to achieve each other. (i.e. number of insertions, deletions and edits)

Thus, it'd be interesting to see this in action.
"""

# Write a dictionary with countries and their short descriptions
countries = {
    "Afghanistan": "Landlocked country located within South Asia and Central Asia.",
    "Albania": "A country in Southeast Europe on the Adriatic and Ionian Sea within the Mediterranean Sea.",
    "Algeria": "A country in the Maghreb region of North Africa. The capital and most populous city is Algiers.",
    "Andorra": "A sovereign landlocked microstate on the Iberian Peninsula, in the eastern Pyrenees, bordered by France to the north and Spain to the south.",
    "Angola": "A country on the west coast of Southern Africa. It is the second-largest lusophone (Portuguese-speaking) country in both total area and population.",
    "Antigua and Barbuda": "A twin-island country in the Americas, lying between the Caribbean Sea and the Atlantic Ocean.",
    "Argentina": "A country located mostly in the southern half of South America. Argentina is the second-largest country in South America after Brazil.",
    "Armenia": "A country located in the Armenian Highlands of Western Asia. It is a part of the Eurasian Economic Union, the Council of Europe and the Collective Security Treaty Organization.",
    "Australia": "A country comprising the mainland of the Australian continent, the island of Tasmania, and numerous smaller islands. It is the largest country in Oceania and the world's sixth-largest country by total area.",
    "Austria": "A landlocked East Alpine country in the southern part of Central Europe. It is composed of nine federated states, one of which is Vienna, Austria's capital and its largest city.",
    "Azerbaijan": "A country in the South Caucasus region of Eurasia, located at the crossroads of Eastern Europe and Western Asia.",
    "Bahamas": "A country within the Lucayan Archipelago in the West Indies. It takes up 97% of the Lucayan Archipelago's land area and is home to 88% of the archipelago's population.",
    "Bahrain": "An island country in the Persian Gulf. The sovereign state comprises a small archipelago centered around Bahrain Island, situated between the Qatar peninsula and the north eastern coast of Saudi Arabia.",
    "Bangladesh": "A country in South Asia. It is the eighth-most populous country in the world, with a population exceeding 162 million people.",
    "Barbados": "An island country in the Lesser Antilles of the West Indies, in the Caribbean region of North America. It is situated in the western area of the North Atlantic.",
    "Belarus": "A landlocked country in Eastern Europe. It is bordered by Russia to the northeast, Ukraine to the south, Poland to the west, and Lithuania and Latvia to the northwest.",
    "Belgium": "A country in Western Europe. It is bordered by the Netherlands to the north, Germany to the east, Luxembourg to the southeast, France to the southwest, and the North Sea to the northwest.",
    "Belize": "A Caribbean country located on the northeastern coast of Central America. Belize is bordered on the northwest by Mexico, on the east by the Caribbean Sea, and on the south and west by Guatemala.",
    "Benin": "A country in West Africa. It is bordered by Togo to the west, Nigeria to the east, Burkina Faso to the north-west, and Niger to the north-east.",
    "Bhutan": "A landlocked country in the Eastern Himalayas. It is bordered by China to the north and India to the south.",
    "Bolivia": "A landlocked country located in western-central South America. The constitutional capital is Sucre, while the seat of government and executive capital is La Paz.",
    "Bosnia and Herzegovina": "A country in Southeastern Europe, located within the Balkan Peninsula. Sarajevo is the capital and largest city.",
    "Botswana": "A landlocked country in Southern Africa. Formerly the British protectorate of Bechuanaland, Botswana adopted its name after becoming independent within the Commonwealth on 30 September 1966.",
    "Brazil": "The largest country in both South America and Latin America. At 8.5 million square kilometers and with over 211 million people, Brazil is the world's fifth-largest country by area and the sixth most populous.",
    "Brunei": "A country located on the north coast of the island of Borneo in Southeast Asia. Apart from its coastline with the South China Sea, the country is completely surrounded by the Malaysian state of Sarawak.",
    "Bulgaria": "A country in Southeast Europe. It is bordered by Romania to the north, Serbia and North Macedonia to the west, Greece and Turkey to the south, and the Black Sea to the east.",
    "Burkina Faso": "A landlocked country in West Africa. It covers an area of around 274,200 square kilometers and is surrounded by six countries: Mali to the north; Niger to the east; Benin to the southeast; Togo and Ghana to the south; and Ivory Coast to the southwest.",
    "Burundi": "A landlocked country in the Great Rift Valley where the African Great Lakes region and East Africa converge. It is bordered by Rwanda to the north, Tanzania to the east and southeast, and the Democratic Republic of the Congo to the west.",
    "Cabo Verde": "An island country spanning an archipelago of 10 volcanic islands in the central Atlantic Ocean. It forms part of the Macaronesia ecoregion, along with the Azores, Canary Islands, Madeira, and the Savage Isles.",
    "Cambodia": "A country located in the southern portion of the Indochina peninsula in Southeast Asia. It is 181,035 square kilometers in area, bordered by Thailand to the northwest, Laos to the northeast, Vietnam to the east and the Gulf of Thailand to the southwest.",
    "Canada": "A country in the northern part of North America. It's the second-largest country by total area.",
    "Denmark": "A Nordic country in Northern Europe. It is the southernmost of the Scandinavian countries.",
    "Ecuador": "A country in northwestern South America, bordered by Colombia on the north, Peru on the east and south, and the Pacific Ocean on the west.",
    "Fiji": "An island country in Melanesia, part of Oceania in the South Pacific Ocean.",
    "Greece": "A country located in Southeast Europe. Its population is approximately 10.4 million as of 2020.",
    "Honduras": "A country in Central America. It has coastlines on the Caribbean Sea to the north and the Pacific Ocean to the south.",
    "Iceland": "A Nordic island country in the North Atlantic Ocean.",
    "Jamaica": "An island country situated in the Caribbean Sea, spanning 10,990 square kilometers in area.",
    "Kuwait": "A country in Western Asia. It is situated in the northern edge of Eastern Arabia at the tip of the Persian Gulf.",
    "Luxembourg": "A landlocked country in western Europe. It is bordered by Belgium to the west and north, Germany to the east, and France to the south.",
    "Malaysia": "A country in Southeast Asia. The federal constitutional monarchy consists of thirteen states and three federal territories.",
    "Nepal": "A landlocked country in South Asia. It is mainly situated in the Himalayas.",
    "Oman": "An Arab country on the southeastern coast of the Arabian Peninsula in Western Asia.",
    "Portugal": "A southern European country on the Iberian Peninsula, bordering Spain.",
    "Qatar": "A peninsular Arab country whose terrain comprises arid desert and a long Persian Gulf shoreline of beaches and dunes.",
    "Russia": "The largest country in the world by land area, covering more than one-eighth of the Earth's inhabited land area.",
    "Sweden": "A Nordic country in Northern Europe. It borders Norway to the west and north, Finland to the east, and is connected to Denmark in the southwest by a bridge-tunnel across the Öresund Strait.",
    "Turkey": "A transcontinental country located mainly on the Anatolian Peninsula in Western Asia, with a smaller portion on the Balkan Peninsula in Southeastern Europe.",
    "Uganda": "A landlocked country in East Africa. It is bordered to the east by Kenya, to the north by South Sudan, to the west by the Democratic Republic of the Congo, to the south-west by Rwanda, and to the south by Tanzania.",
    "Vietnam": "A country in Southeast Asia and the easternmost country on the Indochinese Peninsula.",
    "United States" : "A superpower with extremely valuable currency and a prosper economy situated in North America. Made up of 50 states depicted by the 50 stars on the flag."
}

# Calculate levenstein distance between two strings
def get_levenstein_distance(s1: str, s2: str) -> int:
    """
    Get the Lavenstein's distance between two strings.
    
    Arguments:
    s1 : str : one string
    s2 : str : another string
    """
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) < len(s2):
        return get_levenstein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

# Search for a term in the existing data dictionary
def search(term:str)->dict[str:str]:
    """
    Searches for the provided term into the local data dictionary and returns the closest result. If the difference is significant, returns can't find.

    Arguments:
    term : str : the term to search for

    Returns:
    result : dict[str:str] : the result dictionary with closest term as key and the information as value.
    """
    min = 99999
    result = {}

    for country in countries:
        distance = get_levenstein_distance(term, country)
        if distance  == 0:
            result.clear()
            result[country] = countries[country]
            return result
        
        elif distance < min:
            result.clear()
            min = distance
            result[country] = countries[country]
    
    if min > (0.5)*len(term):
        return {"Sorry":"No search results !!!"}

    return result


# Main driver code
if __name__ == "__main__":
    os.system("clear")
    print("""\n\nHello, welcome to my country information system. This is developed to check fuzzy search. I have a limited knowledge of countries.
          
I will try my best to correct your typos and provide the accurate information.


          """)
    user_choice = input("\tPlease enter a country you want to know about: ")
    information = search(user_choice)
    print(f"\n\n\t{list(information.keys())[0]} : {list(information.values())[0]}\n\n")
