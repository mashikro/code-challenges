# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Test Case:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

def defanging_IP_address(address):

    new_address = address.replace('.', '[.]')

    return new_address

print(defanging_IP_address("1.1.1.1"))
        


# this also works:

def defanging_IP_address2(address):

    add = address.split('.')

    return '[.]'.join(add)

print(defanging_IP_address2("1.1.1.1"))
