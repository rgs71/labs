def is_leapyear(year):

  # TODO
  
    return True
    
    
 
 if __name__ == '__main__':
    year = int(input("Jahr: "))
    if not is_leapyear(year):
          addition = 'k'
    else:
          addition = ''
    
    print(f"Das Jahr {year} war {addition}ein Schaltjahr")
