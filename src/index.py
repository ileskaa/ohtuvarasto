from varasto import Varasto


def getterit_ja_setterit(olutta, mehua):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)


def lisaa_tai_ota(varastonimi, tuote, varasto, maara, moodi="lisaa"):
    print(f"{varastonimi}: {varasto}")
    if moodi == "lisaa":
        print(f"{tuote}.lisaa_varastoon({maara})")
        varasto.lisaa_varastoon(maara)
    elif moodi == "ota":
        print(f"{tuote}.ota_varastosta({maara})")
        saatiin = varasto.ota_varastosta(maara)
        print(f"saatiin {saatiin}")
    print(f"{varastonimi}: {varasto}")


def main():
    print("breaking pylint")

    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    getterit_ja_setterit(olutta, mehua)

    virhetilanteet()

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

    lisaa_tai_ota("Olutvarasto", "olutta", olutta, 1000.0)

    lisaa_tai_ota("Mehuvarasto", "mehua", mehua, -666.0)

    lisaa_tai_ota("Olutvarasto", "olutta", olutta, 1000.0, "ota")

    lisaa_tai_ota("Mehuvarasto", "mehua", mehua, -666.0, "ota")


if __name__ == "__main__":
    main()
