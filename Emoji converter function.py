message = input('>>')
def emoji_converter():
	words = message.split(' ')
# words = message.split(' ') will split words into list
	emojies = {
		':)' : '😊', #in dictionaries have to use ':' sign instead of =
		':(' : '😒', 
		':|' : 'NONNESENCE'
	}
	output = ''
	for word in words:
		output = output + emojies.get(word, word) + ' '
	return output
print(emoji_converter()) 