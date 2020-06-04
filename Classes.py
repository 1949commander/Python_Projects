#This program sets up on Parent Class Vehicle:
class Vehicle:
  def __init__(veh_Type, location_Mode, powr_Mode):
    veh_Type.locationmode = location_Mode
    veh_Type.powermode = powr_Mode

  def printVehicle(veh_Type):
    print("Basic vehicle type  operates on", veh_Type.locationmode,"\n"
          "and uses", veh_Type.powermode, " to operate.\n")
#This class uses parent Vehicle as base to child class AirCraft
class AirCraft(Vehicle):
    def __init__(veh_Type, location_Mode, powr_Mode, prop_Type, wing_Type):
       super().__init__(location_Mode, powr_Mode)
       veh_Type.proptype = prop_Type
       veh_Type.wingtype = wing_Type
       
    def printAirC(veh_Type):
       print("This vehicle operates on: \n"
             , veh_Type.locationmode, "and has", veh_Type.powermode, ","
             "\n on this to operate", veh_Type.proptype,","
             "\n uses", veh_Type.wingtype,",\n")
#This class uses parent Vehicle as base for child class Automobile          
class Automobile(Vehicle):
    def __init__(veh_Type, location_Mode, powr_Mode, eng_Type, body_Type):
       super().__init__(location_Mode, powr_Mode)
       veh_Type.engtype = eng_Type
       veh_Type.bodytype = body_Type
       
    def printAuto(veh_Type):
        print("This vehicle operates on:\n"
              , veh_Type.locationmode,"and has" ,veh_Type.powermode,","
              "\n uses a",veh_Type.engtype,","
              "\n the body is a" ,veh_Type.bodytype,".\n")


#Use the Vehicle class to create an object, and then execute the print() method:

x = Vehicle("Land", "Wheels")
x.printVehicle()

y = AirCraft("Air", "Wings", "Gas Turbine", "Swept Wing")
y.printAirC()

z = Automobile("Land", "Wheels", "Gas Engine", "4 Door Sedan")
z.printAuto()
