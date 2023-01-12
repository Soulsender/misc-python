# Will ask for an amount of SSIDs names to create and use a provided string for the name
# useful for tools such as https://github.com/adamff1/WiFi-Spam

spam_string = input("Type in what you want to spam: ")
ssid_num = int(input("How many SSIDs do you want? "))

with open("ssid_list.txt", "w") as file:
    for i in range(ssid_num, 0, -1):
        ssid_string = spam_string + str(i)
        file.write(ssid_string + "\n")

exit()
