""" working-with-strings.py
    This Python script shows how you can manipulate strings.

    Author: Andres Hernandez G.
    Email: andres.hernandezg@udem.edu
    Institution: Universidad de Monterrey
    First created: Sun 26 Jan, 2020
"""


# print 'Hello Python!' on the command line
print('Hello Python!')

# similar to previous example
print('Hello' + ' Python!')

# print 'Hello Python" in two separate lines on
# the command line
print('Hello \nPython!')

# similar previous example, but using two 'print'
# instructions
print('Hello')
print('Python!')

# initialise a string-type variable
str_hello = 'Hello'
str_python = ' Python!'
print(str_hello+str_python)

# similar to previous example
print(str_hello)
print(str_python)

# using double quotes with text
print("Don't worry" +' "be" happy')
print('Don\'t worry \"be\" happy')

# indexing a string variable
print('First letter in \'str_hello\':', str_hello[0])
print('Length of string \'str_hello\':', len(str_hello))
len_str_hello = len(str_hello)
print('Last letter in \'str_hello\':', str_hello[len_str_hello-1])
print('Last letter in \'str_hello\':', str_hello[-1])
print('Next-to-last letter in \'str_hello\':', str_hello[-2])
print('First two letter in \'str_hello\':', str_hello[0:2])
print(3*str_hello)
print("""\n\n\tG'day mate!, how's is life in Mexico?
    Here in Hawaii life is not bad; nice beaches 
    and great waves - missing kangaroo burgers though!\n""")



print('Type of variable of \'str_hello\':', type(str_hello))

full_string = str_hello + str_python
print(full_string.split(' '))

full_string_list = full_string.split(' ')
print(full_string_list)
print(full_string_list[0] + ' ' + full_string_list[1])

email_address = 'andres.hernandezg@udem.edu'
username = email_address.split('@')[0]
print('username: ', username)
domain = email_address.split('@')[1]
print('domain: ', domain)

username, domain = email_address.split('@')[0], email_address.split('@')[1]
print('username: ', username)
print('domain: ', domain)

temp = email_address.split('@')
print('username: ', temp[0])
print('domain: ', temp[1])

print('hi there!'.capitalize())
print('UDEM'.islower())
print('UDEM'.lower())
print('5'.isnumeric())
print('A'.isnumeric())
print('5'.isdigit())
print("Adding %d + %d = %d" %(1, 1, 1+1))
var1 = 1
var2 = 2
result = var1 + var2
print('Adding %d + %d = %d' %(var1, var2, result))
var3 = 2.34
result = var1 + var3
print('Adding %d + %f = %d' %(var1, var3, result))
result = var1 + var3
print('Adding %d + %f = %f' %(var1, var3, result))
result = var1 + var3
print('Adding %d + %f = %0.3f' %(var1, var3, result))

print("Train: {a:5f},  Bus: {p:8.5f}".format(p=59.058, a=453.54))





print('UDEM'.__dir__())



