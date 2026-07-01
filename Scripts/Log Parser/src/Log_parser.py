log_file = open("Scripts/Log Parser/Samples/sample.log (v0.1)")

for line in log_file: 
   if "ERROR" in line:
       print(line)

   if "WARNING" in line:
     print(line)
        
