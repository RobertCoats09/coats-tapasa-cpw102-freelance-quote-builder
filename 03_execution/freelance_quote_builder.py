# Defines project calculation 
def laborEstimate(rate, time):
    return (rate * time)

# Defines main functions

def main():
    # Receive user input
    name = input("client's name ")
    workhours = float(input("total work hours "))
    hourlyrate = float(input("hourly rate "))
    directexpenses = float(input("direct expense "))
    # Runs calculation for labor cost and total estimate
    laborCost = laborEstimate(hourlyrate, workhours)
    totalCost = (laborCost + directexpenses)
    # Outputs total project estimate 
    print("PROJECT ESTIMATE")
    print("Client: " + name.strip().title())
    print("Labor Cost: " + "$" + str(laborCost))
    print("Direct Expenses: " + "$" + str(directexpenses))
    print("Total Estimate: " + "$" + str(totalCost))


main()
