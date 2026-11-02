import numpy as np

class DataAnalytics:
    def __init__(self):
        self.data= None
  
    def Create_array(self):

        try:
            print("Select Array for Create(1D,2D,3D): ")
            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")

            choice=int(input("Enter your Choice:- "))

            if choice==1:
                Element=input("Enter a Element for Create a 1D array:- ").split()
                ar=list(map(int,Element))
                self.data=np.array(ar)
                print(f"Element: {self.data}")
                print("Added Successfully!")
                return self.data

            elif choice==2:
                row=int(input("Enter a Row for 2D Array:- "))
                col=int(input("Enter a column for 2D Array:- "))
                ar = input(f"Enter {row * col} elements for the array, separated by spaces:- ").split()
                ar1=list(map(int,ar))
                ar2=np.array(ar1).reshape(row,col)
                self.data=ar2
                return self.data

            elif choice==3:
                dep =int(input("Enter a Depth for 3D:- "))
                row =int(input("Enter a Row for 3D:- "))
                col =int(input("Enter a Column for 3D:- "))
                ar=input(f"Enter {dep*row*col} Element for array, separated by spaces:- ").split()
                ar1=list(map(int,ar))
                ar2=np.array(ar1).reshape(dep,row,col)
                self.data=np.array(ar2)
                return self.data

            else:
                print("Invalid Choice!!")

        except:
            print("Something Went Wrong. Please Enter the Current Number of Element!")

        
    def Indexing_and_slicing_op(self,datas):
        try:
            while True:
                print("Choose a Option")
                print("1. For Indexing")         
                print("2. Slicing")         
                print("3. Back to mene Menu")

                choice=int(input("Enter your Choice:- ")) 
                if choice==1:
                        if datas.ndim==1:
                            index=input("Enter a Index Number of Element:- ") 
                            print(f"Element of Index {index}: {datas[index]}")
                        

            
                        elif datas.ndim==2:
                            row=input("Enter a row Index:- ")
                            col=input("Enter a Column Index:- ")
                            print(f"Row and Column Index ({row},{col}):- {datas[row,col]}")
                        

                        elif datas.ndim==3:
                                dep=input("Enter a Depth index:- ")
                                row=input("Enter a Row index:- ")
                                col=input("Enter a Column index:- ")
                                print(f"Depth,row,column({dep},{row},{col}):- {datas[dep,row,col]}")

                        else:
                                print("Invalid choice!")

                elif choice==2:
                    print("Slicing the array:")
                    if datas.ndim==1:
                            stated=int(input("Enter a start index:- "))
                            end=(input("Enter a start index:- "))
                            print(f"Sliced array: {datas[stated:end]}")

                    elif datas.ndim==2:
                         row_st =int(input("Enter a start row index:- "))
                         row_en =int(input("Enter a end row index:- "))
                         col_st =int(input("Enter a start column index:- "))
                         col_en =int(input("Enter a end column index:- "))
                         print(f"Silcing Array: {datas[row_st:row_en , col_st:col_en]}")

                    elif datas.ndim==3:
                         dep_st=int(input("Enter a start Depth index:- "))
                         dep_en=int(input("Enter a start Depth index:- "))
                         row_st=int(input("Enter a start row index:- "))
                         row_en=int(input("Enter a start row index:- "))
                         col_st=int(input("Enter a start col index:- "))
                         col_en=int(input("Enter a start col index:- "))
                         print(f"Silcing Index: {datas[dep_st:dep_en, row_st:row_en, col_st:col_en]}")
        except:
             print("Something Went Wrong!!")               
                    
    def math_operation(self,datas):
        try:
             while True:
                print("="*15)
                print("Choose a Mathematical Operation ")
                print("="*15)
                print("1. Addition")
                print("2. Subtraction")
                print("3. Multiplication")
                print("4. Division")

                choice=int(input("Enter your choice:- "))

                if choice==1:
                    ar = input(f"Enter {datas.size} elements for the second array, separated by spaces:- ").split()
                    ar1=list(map(int,ar))
                    ar2=np.array(ar1).reshape(datas.shape)
                    ans= datas + ar2
                    print("Result of addition:")
                    print(ans)

                elif choice==2:
                    ar=input(f"Enter {datas.size} Element for second array, separated by space:- ").split()
                    ar1=list(map(int,ar))
                    ar2=np.array(ar1).reshape(datas.shape)
                    ans= datas - ar2
                    print("Result of Subtraction")
                    print(ans)

                elif choice==3:
                    ar=input(f"Enter {datas.size} Element for second array, separated by space:- ").split()
                    ar1=list(map(int,ar))
                    ar2=np.array(ar1).reshape(datas.shape)
                    ans= datas * ar2
                    print("Result of Multiplication")
                    print(ans)

                elif choice==4:
                    ar=input(f"Enter {datas.size} Element for second array, separated by space:- ").split()
                    ar1=list(map(int,ar))
                    ar2=np.array(ar1).reshape(datas.shape)
                    ans= datas / ar2
                    print("Result of Division ")
                    print(ans)

                else:
                    print("Invalid choice!!")

            
        except :
                 print("Invalid input. Please enter a valid choice.")

    def comebine_op(self,datas):
        try:
            print()
            print("choose a option")
            print("1. combine array")
            print("2. split array")

            choice=int(input("Enter your choice"))

            if choice==1:
                ar = input(f"Enter {datas.size} Elements for Another Array: ").split()
                ar1=list(map(int,ar))
                ar2=np.array(ar1).reshape(datas.shapes)
                print("Original Array:")
                print(datas)
                print("Second Array:")
                print(ar2)
                print("comebine array (vertical stack)")
                new=np.vstack((datas,ar2))

            elif choice==2:
                arr=int(input("Enter a value for split:- "))
                ar1=np.array_split(datas,arr)
                print("Original Array")
                print(datas)
                print("Combine Array")
                print(ar1)

            else:
                print("Invalid Choice!!")

        except:
            print("Something Went Wrong!")
            
    def search_arr(self, datas):

        try:
            print("Choose a option.")
            print("1. Search a value")
            print("2. Sort a Array ")
            print("3. Filter a Array")

            choice=int(input("Enter Your Choice:- "))

            if choice==1:
                print("Original Datas")
                print(datas)
                search=int(input("Enter a value to Search:- "))

                if search in datas:
                    print("Value Found at index")
                    ar=np.where(datas==search)
                    print(ar[0])

                else:
                     print("Value Not Found!!")

            elif choice==2:
                print("Original array:")
                print(datas)
                sort_arr=np.sort(datas)
                print("Sort datas")
                print(sort_arr)

            elif choice==3:
                print()
                print("Choose a filter:")
                print("1. Values less than")
                print("2. Values greater than")

                choice=int(input("Enter Your Choice:- "))

                value = int(input("Enter the threshold value:- "))

                if choice==1:
                    print("Original Datas")
                    print(datas)
                    print("Filter a Array")
                    less=datas[datas < value]
                    print(less)

                elif choice==2:
                    print("Original Datas")
                    print(datas)
                    print("Filter a Array")
                    greater=datas[datas > value]
                    print(greater)

                else:
                    print("Invalid Choice!!")

            else:
                    print("Invalid Choice!!")


        except:
            print()
            print("Invalid input. Please enter a valid choice.")    

            
    def Aggregates_operations(self, datas):
    
            try:
      
                print()
                print("Choose an option:")
                print("1. Sum")
                print("2. Mean")
                print("3. Median")
    
                choice = int(input("Enter your choice: "))
    
                if choice == 1:
                    print("Original array:")
                    print(datas)
                    sum_arr = np.sum(datas)
                    print(f"Sum of all elements: {sum_arr}")
    
                elif choice == 2:
                    print("Original array:")
                    print(datas)
                    mean_arr = np.mean(datas)
                    print(f"Mean of all elements: {mean_arr}")
    
                elif choice == 3:
                    print("Original array:")
                    print(datas)
                    median_arr = np.median(datas)
                    print(f"Median of all elements: {median_arr}")
    
                else:
                    print("Invalid choice!")
            except:
                print("Something went wrong!")

    def main_menu(self):
  
        print()
        print("="*25)
        print("Welcome to Numpy Analyzer !")
        print("="*25)
        print("Choose an choice :")
        print("1. Create a Numpy Array ")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays ")
        print("4. Search, Sort or Filter Arrays ")
        print("5. Compute Aggregates and Statistics ")
        print("6. Exit ")

    def start_program(self):
        while True :
            try :

                self.main_menu()

                choice = int(input("Enter Your Choice : "))

                if choice == 1:
                    self.data = obj. Create_array()
                    obj.indexing_operations(self.data)

                elif choice == 2:
                    obj.math_operation(self.data)

                elif choice == 3:
                    obj.comebine_op(self.data)

                elif choice == 4:
                    obj.search_arr(self.data)

                elif choice == 5:
                    obj.Aggregates_operations(self.data) 

                elif choice == 6:   
                    print("Thank You for using Numpy Analyzer! Goodbye!")
                    break

                else:
                    print("Invalid choice! Please try again.")
            except:
                print("Invalid input. Please enter a valid choice.")


obj=DataAnalytics()
obj.start_program()
 
 