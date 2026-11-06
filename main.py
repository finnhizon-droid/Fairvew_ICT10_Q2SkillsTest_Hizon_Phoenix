from pyscript import document
# Dictionary containing elements

nonmetals = {"H": ("Hydrogen", 1, 1.008), "He": ("Helium", 2, 4.002), "F": ("Flourine", 9, 19.00), "Ne": ("Neon", 10, 20.18), "P": ("Phosphorus", 15, 30.97), "C": ("Carbon", 6, 12.01), "N": ("Nitrogen", 7, 14.007), "O": ("Oxygen", 8, 15.999), "S": ("Sulfur", 16, 32.06), "Cl": ("Chlorine", 17, 35.45), "Se": ("Selenium", 34, 78.96), "Br": ("Bromine", 35, 79.90), "I": ("Iodine", 53, 126.90), "Ar": ("Argon", 18, 39.95), "Kr": ("Krypton", 36, 83.80), "Xe": ("Xenon", 54, 131.29), "Rn": ("Radon", 86, 222),}
# ELEMENT: ELEMENT NAME, ATOMIC NUMBER, ATOMIC MASS
# PLANET: PLANET NAME, PLANET ORDER FROM SUN, NUMBER OF MOONS


def search_nonmetal(e):
    #Get the input FROM HTML
    Nonmetal1 = document.getElementById("nonmetal1").value
    #Retrieve information from dictionary
    result = nonmetals.get(Nonmetal1, ("Nonmetal not found", "-", "-"))
    #Display the result in HTML
    document.getElementById("code").innerText = Nonmetal1
    document.getElementById("name").innerText = result[0]
    document.getElementById("number").innerText = result[1]
    document.getElementById("mass").innerText = result[2]
