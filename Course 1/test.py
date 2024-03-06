# Step 1: Convert each character to ASCII
message = "HELLO"
ascii_bytes = [ord(char) for char in message]

# Step 2: Convert ASCII values to hexadecimal
hex_bytes = [hex(byte) for byte in ascii_bytes]

# Step 3: Concatenate the hexadecimal representations
hex_string = ''.join(byte[2:] for byte in hex_bytes)

# Step 4: Convert the concatenated hexadecimal string to base-10 integer
base_10 = int(hex_string, 16)

print("message:", message)
print("ascii bytes:", ascii_bytes)
print("hex bytes:", hex_bytes)
print("base-16:", hex_string)
print("base-10:", base_10)