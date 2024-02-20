from ctypes import *

print(windll.msvcrt.time(None))
windll.msvcrt.puts(b"print")

mut_str = create_string_buffer(10)
print(mut_str.raw)

mut_str.value =b'AAAA'
print(mut_str.raw)

windll.msvcrt.memset(mut_str, c_char(b'x'), 5)
windll.msvcrt.puts(mut_str)
print(mut_str.raw)

lib=WinDLL("ddlname.dll")
lib.funccall()

lib.func.argtypes(c_char)
lib.func.restype=int