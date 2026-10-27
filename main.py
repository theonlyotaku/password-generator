import secrets, string

def generate_pwd(length): 
    sr = secrets.SystemRandom()
    chars = (string.ascii_letters + string.digits + "!@#$%^&*")
    pwd = "".join(chars[sr.randint(0,len(chars)-1)] for _ in range(length)) # with "chars" variable
    
    return pwd

length = int(input("\nLength: "))
print(generate_pwd(length))
