input_string = "label"
input_code = 13
array = []
for i in input_string:
    array.append(chr(ord(i)^input_code))
print(array)
# proboha živýho...