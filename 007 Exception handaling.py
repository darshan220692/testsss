# f= open("pep.txt", "r")
# print(" Darshan will purchase Toyota Hyrider")


# try:
#     a = 10
#     print(a / 10)
#     print(a/0)
# except Exception as e:
#     print(f'This is my last line if exception occur as: ', e)

#
# try:
#     f = open("Safari.txt", "r")
# except Exception as e:
#     print(e)


# try:
#     f = open("Zanji.txt", "r")
#     f.write("This is my Village")
# except Exception as e:
#     print(e)
#     print("Please enter the correct code")
# finally:
#     print("You are almost there you work hard until it makes sound")#finally block executes in any condition


def say():
    try:
        val =int(input("Please enter an integer"))

    except:
        print(" we are able to handle the distractions ")
        try:
            val=int(input("Please enter an integer"))
        except:
            print("we are able to handle your mistake second time")
    finally:
        print("Finally will be executed anyhow")