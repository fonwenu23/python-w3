# # global variable
# x = "awesome"

# def myfunc():
# 	print('Python is ' + x)

# myfunc()


# # local variable 
# def myfunc():
# 	x = 'lovely'
# 	print('Python is ' + x)

# myfunc()

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)
