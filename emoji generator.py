message = input('>>')
words = message.split(' ')
# words = message.split(' ') will split words into list
emojies = {
	':)' : '😊', #in dictionaries have to use ':' sign instead of =
	':(' : '😒'
}
output = ''
for word in words:
	output = output + emojies.get(word, word) + ' '
print (output)