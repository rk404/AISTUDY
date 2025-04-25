import random 
def rzut_lewa_moneta():
    ORZEL=0.7 
    prawdopo = random.random()
    if prawdopo<ORZEL: 
        print("Orzeł") 
        print(prawdopo)
    else: 
        print("Reszka")
        print(prawdopo)
rzut_lewa_moneta()