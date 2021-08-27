alphabet = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
	'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
	'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input(f"Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input(f"Type your message:\n").lower()
shift = int(input(f"Type the shift number:\n"))


def encrypt(plaintext, shift_amount):
	ciphertext = ""
	for letter in plaintext:
		if letter.isalpha():
			position = alphabet.index(letter)
			new_position = position + shift_amount
			new_letter = alphabet[new_position]
		else:
			new_letter = letter
		ciphertext += new_letter
	print(f'The encoded text is "{ciphertext}"')


def decrypt(ciphertext, shift_amount):
	plain_text = ""
	for letter in ciphertext:
		if letter.isalpha():
			position = alphabet.index(letter)
			new_position = position-shift_amount
			new_letter = alphabet[new_position]
		else:
			new_letter = letter
		plain_text += new_letter
	print(f'The decoded text is "{plain_text}"')


if direction == "encode":
	encrypt(plaintext=text, shift_amount=shift)
else:
	decrypt(ciphertext=text, shift_amount=shift)
