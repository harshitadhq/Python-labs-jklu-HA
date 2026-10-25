budget=int(input("Enter budget:"))
season=input("Enter the season[summer/winter]:").strip().lower()
if budget<=0 or season not in['summer','winter']:
    print("Invalid input!")
else:
    if budget<=100:
        destination='Bulgaria'
        if season=='summer':
            place='Camping'
            spent=budget*0.3
        else:
            place='Hotel'
            spent=budget*0.7
    elif budget<=1000:
        destination='Balkans'
        if season=='summer':
            place='Camping'
            spent=budget*0.4
        else:
            place='Hotel'
            spent=budget*0.8
    elif budget>1000:
        destination="Europe"
        place='Hotel'
        spent=budget*0.9
    print(f"somewhere in {destination}.")
    print(f"{place}-{spent:.2f}")
    
    

