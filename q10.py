#Write a program that asks the user for their birth year and calculates their age.
def findAge(current_date, current_month, current_year,  
            birth_date, birth_month, birth_year): 
  
    # if birth date is greater than current date 
    # then do not count this month and add 30 to the date so 
    # as to subtract the date and get the remaining days 
      
    month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if (birth_date > current_date): 
        current_month = current_month - 1
        current_date = current_date + month[birth_month-1] 
          
    if (birth_month > current_month):          
        current_year = current_year - 1; 
        current_month = current_month + 12; 
          
    calculated_date = current_date - birth_date; 
    calculated_month = current_month - birth_month; 
    calculated_year = current_year - birth_year; 
      
    print"Present Age"
    print("Years:", calculated_year, "Months:",   
         calculated_month, "Days:", calculated_date) 
      
current_date = 7
current_month = 12
current_year = 2017
          
birth_date = 16
birth_month = 12
birth_year = 2009
  
findAge(current_date, current_month, current_year,  
        birth_date, birth_month, birth_year) 