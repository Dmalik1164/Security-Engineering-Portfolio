with open("Scripts/Log Parser/Samples/Auth.log") as file:
     counts = {"error": 0, "Failed password": 0, "Disconnecting": 0}
     for line in file: 
       if "error" in line:
           counts["error"] += 1
           

       if "Failed password" in line:
            counts["Failed password"] += 1
           
        
       if "Disconnecting" in line:
           counts["Disconnecting"] += 1
           
print(counts)
