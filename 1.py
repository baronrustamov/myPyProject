class Laptop:
	name = 'My Laptop'
	processor = 'Intel Core'
	
	@staticmethod
	def start():
		print('Laptop is starting..')
		
	@staticmethod
	def restart(self):
		print('Laptop is restarting')
		
	def details(self):
		print('My laptop name is:', self.name)
		print('It has',self.processor,'processor.')


           
#create object
laptop1 = Laptop()
laptop1.name = 'Dell Alienware'
laptop1.processor = 'Intel Core i7'
laptop1.start()
laptop1.details()

##open file
#f = open("sample.txt", "x")
##close file
#f.close

#text_file = open("sample.txt", "w")
#n = text_file.write('Welcome to python')
#text_file.close()

text_file = open("sample.txt", "wt")
n = text_file.write(laptop1.name)
n = text_file.write(" ")
n = text_file.write(laptop1.processor)
text_file.close()


#read integer from user
n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))

print('The sum of two numbers is:', n1+n2)

if n1<n2:
	print(n1, 'is less than', n2)
else:
	print(n1, 'is not less than', n2)
    
#read multiple strings from user
firstName = input('Enter your first name: ')
lastName = input('Enter your last name: ')

print('Hello',firstName, lastName)