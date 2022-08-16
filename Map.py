class Map:
    mapWidth = 81  # tək ədəd olsun
    placeWidth = 22
    upperPlaceWitdh = 31  # tək ədəd olsun
    upHeight = 5
    downHeight = 3
    map = [
        "╔" + "═" * (mapWidth - 2) + "╗",  # 1
        *(["║" + " " * (mapWidth - 2) + "║"] * (upHeight // 2)),
        "║"
        + " " * ((mapWidth - 2 - upperPlaceWitdh) // 2)
        + "═" * upperPlaceWitdh
        + " " * ((mapWidth - 2 - upperPlaceWitdh) // 2)
        + "║",  # 4
        *(["║" + " " * (mapWidth - 2) + "║"] * (upHeight // 2)),
        "╠"
        + "═" * (placeWidth - 1)
        + " " * (mapWidth - placeWidth * 2)
        + "═" * (placeWidth - 1)
        + "╣",  # 5
        *(
            [
                "║"
                + " " * ((mapWidth - 2) // 2)
                + "║"
                + " " * ((mapWidth - 2) // 2)
                + "║"
            ]
            * (downHeight - 1)
        ),  # 7
        "╚"
        + "═" * ((mapWidth - 2) // 2)
        + "╩"
        + "═" * ((mapWidth - 2) // 2)
        + "╝",  # 8
    ]
    foribdden = ["║", "╔", "═", "╗", "╠", "╣", "╚", "╝", "╩"]

    def MapPrint(map, health1, health2):
        for value in map:
            print(value)
        print(f"Player 1 health : {health1}")
        print(f"Player 2 health : {health2}")
