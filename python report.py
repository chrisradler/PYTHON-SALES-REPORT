import csv
from tempfile import tempdir

# The below class will be representing TeamMap
#The Team Map : an integer that uniquely identifying a team and the string name of the team
class TeamMap:
    def __init__(self , teamId ,name):
        self.teamId =int( teamId) 
        self.name = name
#The below class will be representing ProductMaster
#ProductId – an integer uniquely identifying the Product
#Name – a string name of the Product
#Price – a floating point price at which the Product is sold (per unit, not per lot)
#LotSize – an integer representing the number of products sold in a single lot

class ProductMaster:
    def __init__(self, productId, name, price, lotSize):
        self.productId = int(productId)
        self.name = name
        self.price = float(price)
        self.lotSize = int(lotSize)
#The below class will be Sales
# SaleId – an integer uniquely identifying the sale
# ProductId – an integer identifying the Product (matches the ProductId from the Product Master)
# TeamId – an integer identifying the Sales Team (matches the TeamId from the Team Map)
# Quantity – an integer representing how many lots of the product were sold
# Discount – a floating point discount percentage given on the sale (e.g. 2.5% discount as “2.50”)

class Sales:
    def __init__(self, saleId, productId, teamId, quantity, discount):
        self.saleId = int(saleId)
        self.productId = int(productId)
        self.teamId = int(teamId)
        self.quantity = int(quantity)
        self.discount = float(discount)
# The below class will be TeamReport 
# the string name of the sales team and the total gross revenue of their team’s sales.
class TeamReport:
    def __init__(self,teamId,teamName):
        self.teamId = int(teamId)
        self.teamName =teamName
        self.sales =0
# the class below will be the product report
#Name – name of the Product
# GrossRevenue – gross revenue of sales of the Product
# TotalUnits – total number of units sold in the Product
# DiscountCost – total cost of all discounts provided on sales of the Product
class ProductReport:
    def __init__(self,productId,name):
         self.productId = int(productId)
         self.name = name
         self.grossRevenue =0
         self.totalUnits=0
         self.discountCost=0

        
        
# Method Id# 1    
# The readTeamMap(teamMapList) method will load the data from TeamMap.csv which  is a comma-separated text file
#  where each line contains two values: an integer uniquely identifying a team and the string name of the team
# and the first row is just representing the columns names
def readTeamMap(teamMapList):
    # The readTeamMap(teamMapList) read the data from "TeamMap.csv" and as
    # each row besides the very first row is representing an object of TeamMap so it will append 
    # each object in the teamMapList

    with open("TeamMap.csv") as csv_file:
        reader =csv.reader(csv_file,delimiter=',')
        numOfLines =0

        for row in reader:
            if numOfLines == 0:
               # this if just make sure that the first row from TeamMap will not be appended in the list 
               #because row 0 is not the actual data but its just the name of colum
                numOfLines +=1
            else:
                # if the numOfLines is not 0 then it will append teamMap object into teamMapList
                tempData = TeamMap (row[0],row[1])
                teamMapList.append(tempData)

                numOfLines += 1

#Method Id# 2
#The  readProductMaster(productMasterList) will  load The Product Master file
# which  is a comma-separated text file where each line contains information about aunique product. 
def readProductMaster(productMasterList):

    # The readProductMaster(productMasterList) read the data from "ProductMaster.csv" and as
    # each row is representing an object of ProductMaster so it will append 
    # each object in the productMasterList

    with open("ProductMaster.csv") as csv_file:

        f2Reader = csv.reader(csv_file,delimiter=',')
        numOfLines =0
        for row in f2Reader:  
        # this if just make sure that the first row from TeamMap will not be appended in the list 
               #because row 0 is not the actual data but its just the name of colum
            tempData = ProductMaster(row[0],row[1],row[2],row[3])
            productMasterList.append (tempData)
            numOfLines += 1
            
#Method Id# 3
# The readSales(salesList) will read the data from  Sales file is a comma-separated text file 
# where each line contains information about a unique sale. 
def readSales(salesList):

    # The readSales(salesList) read the data from Sales.csv and as
    # each row is representing an object of Sales so it will append 
    # each object in the salesList
    with open("Sales.csv")as csv_file:
        f3Reader = csv.reader(csv_file,delimiter=',')
        for row in f3Reader:
            tempData =Sales(row[0] ,row[1] ,row[2] ,row[3],row[4])
            salesList.append(tempData)

        
#Method Id# 4        
#The below method will display the data present in the team Map List
def displayTeamMap(teamMapList):


    print("**********************************************************")
    print("*********List of team members is as follow****************")
    print("    Team ID  ,  Names ")
    for value in teamMapList :
        print ( "   ",value.teamId, "    -> ",value.name)


    print("************************************************************")
    #The below method will display the data present in the product master List


#Method Id# 5
#The displayProductMaster(productMasterList) will display all the objects ProductMasters in the list 
def displayProductMaster(productMasterList):
        
    print("**********************************************************")
    print("*********List of Product Master is as follow****************")
    print(" Product id  ,  Names ,      Price ,      Lot Size ")
    for value in productMasterList :
        print ( "   ",value.productId, "  ,",value.name, " ,",value.price, " , ",value.lotSize)


    print("************************************************************")

#Method Id# 6 
#The displaySales(salesList)  will display the data present in the sales List
def displaySales(salesList):
    print("**********************************************************")
    print("*********List of sales is as follow****************")
    print(" SaleId , productId , TeamId , Quantity , Discount ")
    for value in salesList:
        print( "   ", value.saleId, "  , ", value.productId, "  , ", value.teamId, "  , ", value.quantity, "  , ", value.discount)


#Method Id# 7
#The getLotPrice(productMasterList, pId) will accept the productMaster list and product id as pId
# and will return the index of the pId in the productMasterList 
# if there is no product Id match found then it will return -1
def getLotPrice(productMasterList, pId) :

    for value in productMasterList:
         if pId == value.productId:
             return (value.price * value.lotSize)
            
    # if the product with the given id is not present then it will return -1
    return -1 

#Method Id# 8
#The getIndexOfTeam(salesReportList, teamId) will accept the salesReport list and team id as teamId
# and will return the index of the teamId in the salesReportList 
# if non of the available  teamId matchs with this id  then it will return -1
def getIndexOfTeam(salesReportList, teamId):
    for index in range(len(salesReportList)):
        if salesReportList[index].teamId == teamId:
            return index


    # if team id is invalid i'm returning -1
    return -1

#Method Id# 9
#The below method will accept sales List and will sort it with respect  sales
def sortTeamsBySales(salesList):
    for x in range(len(salesList)):
        for y in range(x+1 ,len(salesList)):
            if salesList[x].sales < salesList[y].sales:
                temp = salesList[x] 
                salesList[x] = salesList[y]
                salesList[y] = temp

#Team Id# 10
#The teamReportCalculator(teamMapList, productMasterList, salesList) will accept three list teamMapList ,productMasterList ,salesList
#and will calculate the Report of Teams based on there sales

def teamReportCalculator(teamMapList, productMasterList, salesList):

    # defining a list names as salesReportList that will be used to hold all data for report
    salesReportList =list()
    # just making a toatl sales list for each team 
    for team in teamMapList :
        salesReportList.append(TeamReport(team.teamId,team.name))
    #Traversing the salesList to calculte the team repost
    for sale in salesList :
        
        lotPrice = getLotPrice(productMasterList , sale.productId)

        index = getIndexOfTeam(salesReportList ,sale.teamId)
        if index != -1:
            # calculating the sales sales after discount
            saleBeforeDis = lotPrice * sale.quantity 
            discount  =  saleBeforeDis * (sale.discount / 100)
            salesAfterDis = saleBeforeDis - discount
            #Increasing the sales of a team by adding the sale of x'th transaction
            salesReportList[index].sales = salesReportList[index].sales + ( salesAfterDis )

    return salesReportList




 # team id#  11
 # It will generate TeamReport.txt with reports

    
def TeamSaleReportGenerate(salesReportList):

    writer = open("TeamReport.txt","w")
    writer.write("Team,GrossRevenue\n")
    for x in salesReportList :
        writer.write(x .teamName + ","+ str(x.sales)+"\n")
    writer.close()

# team id # 12
# team 

def getIndexOfProduct( productReportList,productId):
     for index in range(len(productReportList)):
        if productReportList[index].productId == productId:
            return index


     # if team id is invalid i'm returning -1
     return -1


def getLotsSize( productMasterList, productId):
   for index in range(len(productMasterList)):
        if productMasterList[index].productId == productId:
            return productMasterList[index].lotSize


   # if team id is invalid i'm returning -1
   return -1

# method id# 12
# below defined methods will be used to to generate the report with respect to products

def productReportCalculator( productMasterList, salesList):
    
    productReportList = list()

    for product in productMasterList:
           productReportList.append(ProductReport(product.productId, product.name))

    
    for sale in salesList :
        lotPrice = getLotPrice(productMasterList , sale.productId)

        index   = getIndexOfProduct( productReportList,sale.productId)
      

        if index != -1  :
            # the below code will calculate the Gross Revenue
            saleBeforeDis = lotPrice * sale.quantity 
            discount  =  saleBeforeDis * (sale.discount / 100)
            salesAfterDis = saleBeforeDis - discount
            productReportList[index].grossRevenue = productReportList[index].grossRevenue + ( salesAfterDis )

            # code to calculate total Units of a specific product sold
            LotSize = getLotsSize( productMasterList, sale.productId)
            soldUnits   = LotSize * sale.quantity
            productReportList[index].totalUnits = productReportList[index].totalUnits + soldUnits


            # code to calculate total discount

            productReportList[index].discountCost = productReportList[index].discountCost + discount

    return productReportList


#Metods Id # 13
#The sortProductBySales(productReportList) will sort the productReportList  with respect to grossRevenue
def sortProductBySales(productReportList):

    for x in range(len(productReportList)):
        for y in range(x+1 ,len(productReportList)):
            if productReportList[x].grossRevenue < productReportList[y].grossRevenue:
                temp = productReportList[x] 
                productReportList[x] = productReportList[y]
                productReportList[y] = temp

# method id#  14
# It will generate productReport.txt with reports    
def ProductSaleReportGenerate(productReportList):

    writer = open("ProductReport.txt","w")
    writer.write("ProductName,GrossRevenue,TotalUnits,DiscountCost\n")
    for x in productReportList:
          writer.write( x.name+ ","+ str(x.grossRevenue)+","+str(x.totalUnits)+","+str(x.discountCost)+"\n")
    writer.close()


             
#Method Id # 15
#Below I defined the main method and using it as a project controler 
def main():

    teamMapList = list()
    productMasterList =list()
    salesList = list()


    #  calling   readTeamMap to load  data from the teamMap.csv into a list named teamMapList
    readTeamMap(teamMapList)
    displayTeamMap(teamMapList)

    # calling   readProductMaster to load  data from the ProductMaster.csv into a list named  productMasterList
    readProductMaster(productMasterList)
    displayProductMaster(productMasterList)

    
    # calling   readSales to load  data from the Sales.csv into a list named  salesList
    readSales(salesList)
    displaySales(salesList)

    # teamReportCalculator(teamMapList, productMasterList, salesList) will generates the results of sale 
    salesReportList = teamReportCalculator(teamMapList, productMasterList, salesList)

    # sorting the salesReportList 
    sortTeamsBySales(salesReportList)

    # Below i'm just printing the generated Results on console
    print("\n\n\n***********************************************")
    print("-------------Team's Sale Report****************")
    print("***********************************************")
    print("TeamId,TeamName,GrossSales")
    for x in salesReportList :
        print( x.teamId, ",",x .teamName, ",", x.sales)

    print("************************************************\n\n")
    #The  TeamSaleReportGenerate(salesReportList) will store the calculated results into TeamReport.txt
    TeamSaleReportGenerate(salesReportList)

    # Calculating the  Report with respect  to Product
    productReportCalculator(productMasterList, salesList)

    #productReportCalculator( productMasterList, salesList) will generate the results of ProductReport 
    # and will return a list of results
    productReportList  = productReportCalculator( productMasterList, salesList)
    # sorting the results
    sortProductBySales(productReportList)


    # Below i'm just printing the generated Results of Product Report on console
    print("\n\n\n***********************************************")
    print("-------------  Product Report  ****************")
    print("***********************************************")
    print("ProductName,GrossRevenue,TotalUnits,DiscountCost")
     
    for x in productReportList:
        print( x.name, ",", x.grossRevenue,",",x.totalUnits,",",x.discountCost)
    print("************************************************\n\n")
    #ProductSaleReportGenerate(productReportList) will store the productSales result in a txt file
    ProductSaleReportGenerate(productReportList)

    print("_________________________ Note !_____________________")
    print("The following code generates two txt files named as")
    print("TeamReport.txt and ProductReport.txt will results .")
    print("____________________________________________________")






if __name__ == "__main__":
    main()



