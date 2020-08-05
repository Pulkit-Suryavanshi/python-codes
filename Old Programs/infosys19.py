'''The year is evenly divisible by 4; If the year can be evenly divided by 100, it is NOT a leap year, unless;
The year is also evenly divisible by 400'''
def find_leap_years(given_year):
    l=[]
    temp=0
    if((d%4== and d%100!=0) or d%400==0):
        for i in range(10):
            l.append(d+temp)
            temp+4
        else:
            temp=d/4
            for i in range(10):
                l.append(d+temp+1)
                temp+=4
                print(l)
    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)