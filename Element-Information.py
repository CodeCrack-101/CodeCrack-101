import periodictable

def Get_Element(symbol):
    try:
        # Get the element from the periodic table
        element = periodictable.elements.symbol(symbol)
        print(f"Element: {element.name}")
        print(f"Element Symbol: {element.symbol}")
        print(f"Atomic Number: {element.number}")
        print(f"Atomic Weight: {element.mass}")
        print(f"Density: {element.density} g/cm³" if element.density else "Density: Not available")
    except KeyError:
        print("Invalid Symbol. Please enter a valid element symbol.")

# Get user input
ele = input("Enter the correct symbol of the element: ").strip()
Get_Element(ele)
