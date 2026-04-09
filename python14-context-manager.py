#using context manager we can communicate with files with socket connections like mysql and so on so we dont have to explicit close the conn 

#Manual
file = open("data.txt", "r")
data = file.read()
file.close()


#with context manager
with open("data.txt", "r") as file:
    data = file.read()



#Custom
class FileManager:
    def __enter__(self):
        print("Opening resource")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing resource")



with FileManager():
    print("Using resource")



if __name__ =="__main__":

    with FileManager():
        print("Using resource")


