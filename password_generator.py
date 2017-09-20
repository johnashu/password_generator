import random

def passwd(l):
    """
    Generates a Random Password based on an inputted integer
    """
    allowed = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?`¬|{}_+/\.,£€¦=-"
    pass_len = l
    passwd =  "".join(random.sample(allowed, pass_len))
    #print(passwd)
    password = [i + "".join(random.sample(allowed, pass_len)) for i in passwd]
    #print(password)
    password = [i[:-l:l+1] for i in password]
    return "".join(password)

print(len(passwd(25)))
print(passwd(25))