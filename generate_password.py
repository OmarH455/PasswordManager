import random
class PasswordGenerator:
    def generate_password(self, password_entry):
        password_entry.delete(0, "end")
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '!#$%&()*+'

        while True:
            nr_letters = random.randint(3, 6)
            nr_symbols = random.randint(3, 7)
            nr_numbers = random.randint(3, 4)
            total_characters = nr_letters + nr_symbols + nr_numbers
            if total_characters >= 8:
                break

        password = [random.choice(letters[26:])]

        for _ in range(1, nr_letters):
            password.append(random.choice(letters[0:26]))

        for _ in range(1, nr_symbols):
            password.append(random.choice(symbols))

        for _ in range(1, nr_numbers):
            password.append(random.choice(numbers))

        shuffled_password = password[1:]
        random.shuffle(shuffled_password)
        password = password[0] + ''.join(shuffled_password)
        password_entry.insert(0, password)