#Code to find ip address and mac address from the given string.
#Coded By : Prerak Mathur (pmathur@scu.edu)
import re
class AddressFinder:
    def __init__(self, string):
        self.string = string
    def findIpAddress(self):

        pattern = re.compile(r'\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\b')
        matches = pattern.finditer(self.string)
        if matches:
            print("Here's the list of ip addresses addresses found")
        else:
            print("No ip address found!")
        for match in matches:
            print(match)

    def findMacAddress(self):

        pattern = re.compile(r'([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])')
        matches = pattern.finditer(self.string)
        if matches:
            print("Here's the list of Mac addresses found")
        else:
            print("No Mac address found!")
        for match in matches:
            print(match)


if __name__ == '__main__':
    #Finding ip and mac addresses in string 1
    print("Executing Test1 ")
    string1 = "abac 10.101.10.2 asa 00:00:5e:00:53:af"
    test1 = AddressFinder(string1)
    test1.findIpAddress()
    test1.findMacAddress()
    print("Test1 Executed \n \n ")


    # Finding ip and mac addresses in string 2
    print("Executing Test2 ")
    string2= "16.481 GMT+0200' 10.13.11.7 Server01:1812 0 0 text=Access GRANT5.525 GMT+0200 0.0.0.0 Server01:1812 0 0 text=Authentication com45.525 GMT+0200 10.13.11.4 Server01:1812 0 0 text=Access GRANT8.485 GMT+0200 0.0.0.0 Server01:1812 0 0 text=Trying to fetch attr16.481 00:00:5e:00:53:af GMT+0200 10.13.11.7 Server01:1812 0 0 text=Access GRANT5.525 GMT+0200 0.0.0.0 Server01:1812 0 0 text=Authentication"
    test2 = AddressFinder(string2)
    test2.findIpAddress()
    test2.findMacAddress()
    print("Test2 Executed \n ")

    print("Thanks!")
