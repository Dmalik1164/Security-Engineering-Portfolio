log_file = open("Sample.log")

for line in log_file: 
   if "ERROR" in line:
       print(line)

   if "WARNING" in line:
     print(line)
        
