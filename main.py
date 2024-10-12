import hashlib

rainbow = {}

# tara
# correct = "Sphinx of black quartz, judge my vow!"
# guess = input("what is your passphrase? ")

# correct_hashed = b'\xfa=%\xd6\x08\xa5!#8\x88\xb40\r\xa9N\xdc'
# guess_encoded = guess.encode()
# guess_hashed = hashlib.md5(guess_encoded).digest()

# if guess_hashed == correct_hashed:
#     print("welcome to the club!")
# else:
#     print("go away smh")
# #b'\xfa=%\xd6\x08\xa5!#8\x88\xb40\r\xa9N\xdc'

# for line in open("common-passwords.txt"):
#    password = line
#    password_stripped = password.strip()
#    password_encoded = password_stripped.encode()
#    password_hash = hashlib.md5(password_encoded)
#    password_hash = str(password_hash.digest())
#    rainbow[password_hash] = password
# print(rainbow)

# for line in open("accounts.txt"):
#    line = line.strip()
#    account = line.split(",")
#    name = account[0]
#    password_hash = account[1]
#    if password_hash in rainbow:
#       print(name)
#       print(password_hash)
#       print(rainbow[password_hash])


salt = "salty"
# correct = 'The ship sails at midnight' + salt
# guess = input('guess ')
# guess = guess + salt
# guess_encoded = guess.encode()
# guess_hash = hashlib.md5(guess_encoded).digest()
# correct_encoded = correct.encode()
# correct_hash = b'\xae\xbc\xe9f\xd1%Q\x8a\xf2\xfd\xba\xb2\x922`\xa5'
# if guess_hash == correct_hash:
#     print('yay')
# else:
#     print('nay')

# for number in range(1000, 9999):
#     print(number)

salted_passwords = []
for line in open("salty.txt"):
    line = line.strip()
    account = line.split(",")
    password_hash = account[1]
    salted_passwords.append(password_hash)

    possible_salted = "password" + str(salt)
    possible_encoded = possible_salted.encode()
    possible_hash = hashlib.md5(possible_encoded).digest()
    if possible_hash in salted_passwords:
        print(salt)

