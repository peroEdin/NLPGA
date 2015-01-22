#input.txt    
First row  
[V,E,I,D] = [number of variables], [number of equality restrictions], [number of inequality restrictions] [number of domain restrictions]

Next E rows    
Input of equality restrictions    
ex. for E=1 :   
  2x+3y=1      
     
    2 3 1



Next I rows       
Input of inequality restrictions (<=)    
ex. for I=2 :        
  2x+3y <= 1       
  x - y >= 1 (*-1)      
  
    2 3 1        
    -1 1 -1           



Next D rows      
Input of domain restrictions      
ex. for D=1 :      
  -1 <= x <= 1      
  
    -1 1    


#Mutations
- uniform    (tested -> works)
- boundary   (tested -> works)
- nonuniform (test pending for GA simulation)

#Crossovers
- arithmetical
- simple
- heuristic
