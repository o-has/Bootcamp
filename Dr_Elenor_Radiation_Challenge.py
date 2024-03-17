# Dr Elenor's Radiation Exposure Calculator
# Programme that calculates the average (ave) and standard deviation (std) of Radiation Levels across Codecity and allows the user
# to enter new measurements

import math
import statistics
import mycolourset as col


# Define the lists to store locations and radiation readings
locations = ["City Centre", "Industrial Zone", "Residential District", "Rural Outskirts", "Downtown"]
levelsall = [[22, 19, 29, 31, 28],[35, 32, 30, 37, 40],[15, 12, 18, 20, 14],[9, 13, 16, 14, 7], [25, 18, 22, 21, 26]]

# Calculate and display the ave. and std. of radiation levels across the whole of Codecity
print(col.WHITE + "\n=== CODECITY RADIATION LEVELS ===" + col.RESET)

# Adds all readings together
total_levels = sum(sum(sublist) for sublist in levelsall)   

# Returns quantity of readings
total_readings = sum(len(sublist) for sublist in levelsall) 

# Calculates average
big_average = total_levels/total_readings                   
print(f"{col.BLUE}City-wide Average: {col.RESET}{big_average:.2f}", end= " ")

# Places all readings into a single list to make standard deviation calc easier
combined_readings = [item for sublist in levelsall for item in sublist] 

# Calculates standard deviation
big_std = statistics.stdev(combined_readings)                           
print(f"{col.BLUE}City-wide Standard Dev.:{col.RESET} {big_std:.2f}")

# Calculate and display the ave. and std. of radiation levels at each different location
for i in range(len(levelsall)):
    total_levels = sum(levelsall[i])
    print("\n===",locations[i],"===")
    print(f"{col.BLUE}Readings: {col.RESET}{levelsall[i]}")
    avelevels = total_levels/len(levelsall[i])
    stdlevels = statistics.stdev(levelsall[i])
    print(f"{col.BLUE}Average Radiation level: {col.RESET}{avelevels:.2f}", end=" ")
    print(f"{col.BLUE}Standard deviation: {col.RESET}{stdlevels:.2f}")

# Set control variable for upcoming while loops for continuous data entry
Flag_1 = True
Flag_2 = True

# NEW READING INPUT CODE BLOCK

# While loop 1 controlled by Flag_1
while Flag_1 == True:
    try:
        print(col.GREEN +"\n+++ ADD MEASUREMENTS +++" + col.RESET)            
        
        # Request user to select location of reading
        location_ident = input(f"\nLocations:\nCity Centre {col.YELLOW}[1]{col.RESET} \nIndustrial Zone {col.YELLOW}[2]{col.RESET} \nResidential District {col.YELLOW}[3]{col.RESET}\nRural Outskirts {col.YELLOW}[4]{col.RESET}\nDowntown {col.YELLOW}[5]{col.RESET}\n\nType number to select location of reading or type 'done' to finish: ")                
        Flag_2 = True       # Ensures While loop 2 activates
        
        # Condition checks if user wants to stop data entry
        if location_ident.lower() == "done":        
            print(f"{col.GREEN}Thank you. The current Radiation Levels are shown above{col.RESET}")
            break
        # Condition checks that user enters only a number and this is between 0 and 4    
        elif not location_ident.isnumeric() or not int(location_ident) < 6:
            print(f"\n{col.YELLOW}*** Please enter only a numerical value between 1 and 5 ***{col.RESET}")
            continue

    except:
        continue
    
    #While loop 2 controlled by Flag_2
    while Flag_2 == True:
        # Request user to enter radiation level
        levelinput = input("\nEnter new radiation level or 'done' to finish: ")
        
        # Condition checks if user wants to stop data entry
        if levelinput.lower() == "done":
            print(f"{col.GREEN}Thank you. The current Radiation Levels are shown above{col.RESET}")
            Flag_1 = False      # Ensures break out of both loops
            Flag_2 = False      # Ensures break out of both loops
    
        else:       
            # Code block to append new reading to correct location and display updated readings and calculations
            try: 
                levelsall[int(location_ident)-1].append(int(levelinput))  # Attempts to add reading to levelsall, gives ValueError if non-integer entered
                
                print(f"\n{col.BLUE}=== NEW RADIATION LEVELS ==={col.RESET}")
                
                total_levels = sum(sum(sublist) for sublist in levelsall)
                
                total_readings = sum(len(sublist) for sublist in levelsall)
                
                big_average = total_levels/total_readings
                
                print(f"City wide Average:{big_average:.2f}")
                
                combined_readings = [item for sublist in levelsall for item in sublist]
                
                big_std = statistics.stdev(combined_readings)
                
                print(f"City-wide Standard Dev.: {big_std:.2f}")
                
                Flag_2 = False      # Prevents While loop 2 running after a reading has been entered
                Flag_1 = True       # Ensures While loop 1 runs again
                
                # Calculates and displays updated readings and calculations at each different location
                for i in range(len(levelsall)):
                    total_levels = sum(levelsall[i])
                    print("\n===",locations[i],"===")
                    print(f"{col.BLUE}Readings: {col.RESET}{levelsall[i]}")
                    avelevels = total_levels/len(levelsall[i])
                    stdlevels = statistics.stdev(levelsall[i])
                    print(f"{col.BLUE}Average Radiation level: {col.RESET}{avelevels:.2f}")
                    print(f"{col.BLUE}Standard deviation: {col.RESET}{stdlevels:.2f}") 

            except ValueError:
                print(f"\n{col.YELLOW}*** Invalid input, please enter an integer number ***{col.RESET}")
        
                    
            