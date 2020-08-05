#PF-Prac-3
def create_new_dictionary(prices):
    new_dict=prices.copy()
    for x,y in prices.items():
        if(y<=200):
            new_dict.pop(x)
    return(new_dict)
prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices))