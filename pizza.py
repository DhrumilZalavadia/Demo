def main():
    slicesPerSecond = 350
    slicesPerMinute = 60
    slicesPerHour = 60
    slicePerDay = 24

    slicesPerDay = slicesPerSecond * slicesPerMinute * slicesPerHour * slicePerDay

    print("Total Number of slices per day americans eat is:",slicesPerDay)

if __name__ == "__main__":
    main()
