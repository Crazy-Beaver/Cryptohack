from Crypto.Util.number import *
#KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
#KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
#KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
#FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
key1 = bytes_to_long(bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"))
#key2 = bytes_to_long(bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")) ^ key1
#key3 = bytes_to_long(bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")) ^ key2

flag = bytes_to_long(bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")) ^ bytes_to_long(bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")) ^ key1
print(flag)
flag = long2str(flag)
print(flag)
#woohoo