class Encryption:
    def encrypted(self, password):
        lett = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = '0123456789'
        syms = '!#$%&()*+'

        splitted = password.split(" | ")
        encrypted_password = ""

        for word in splitted:
            for char in word:
                if char in lett:
                    ind = lett.index(char)
                    encrypted_char = lett[(ind + 2) % len(lett)]
                elif char in nums:
                    indN = nums.index(char)
                    encrypted_char = nums[(indN + 3) % len(nums)]
                elif char in syms:
                    indS = syms.index(char)
                    encrypted_char = syms[(indS + 4) % len(syms)]
                elif char == ' ':
                    encrypted_char = ' '
                else:
                    encrypted_char = char
                encrypted_password += encrypted_char
            encrypted_password += " | "

        encrypted_password = encrypted_password[:-3]

        return encrypted_password
    
    def decrypt(self, encrypted_password):
        lett = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        nums = '0123456789'
        syms = '!#$%&()*+'

        splitted = encrypted_password.split(" | ")
        decrypted_password = ""

        for word in splitted:
            for char in word:
                if char in lett:
                    ind = lett.index(char)
                    decrypted_char = lett[(ind - 2) % len(lett)]
                elif char in nums:
                    indN = nums.index(char)
                    decrypted_char = nums[(indN - 3) % len(nums)]
                elif char in syms:
                    indS = syms.index(char)
                    decrypted_char = syms[(indS - 4) % len(syms)]
                elif char == ' ':
                    decrypted_char = ' '
                else:
                    decrypted_char = char
                decrypted_password += decrypted_char
            decrypted_password += " | "

        decrypted_password = decrypted_password[:-3]

        return decrypted_password
