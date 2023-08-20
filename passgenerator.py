import random
import string

def parol_generator(uzunluq):
    qaydalar=string.ascii_letters+string.digits+string.punctuation
    parol=[]
    for _ in range(uzunluq):
        random_qaydalar=random.choice(qaydalar)
        parol.append(random_qaydalar)
    parol=''.join(parol)
    return parol

print("""
  _____                                    _     
 |  __ \                                  | |    
 | |__) |_ _ ___ _____      _____  _ __ __| |    
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |    
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |    
 |_|___\__,_|___/___/ \_/\_/ \___/|_|  \__,_|    
  / ____|                         | |            
 | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                            BY: NICAT ABBASOV    
                                                 
""")

uzunluq=int(input("Parolun uzunlugunu daxil edin: "))
parol=parol_generator(uzunluq)
print(f"Parolunuz: {parol}")
