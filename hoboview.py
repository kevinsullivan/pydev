from hobo import HoboCSVReader

with HoboCSVReader("my_hobo_data.csv") as reader:
    print("Reading %s ..." % reader.fname)
    print("Serial Number: %s  Title: %s" % (reader.sn, reader.title))

    for timestamp, temperature, rh, battery in reader:
        print(
            "%s   %03.1f F   %02.1f %%   %.1f V" % (timestamp, temperature, rh, battery)
        )
