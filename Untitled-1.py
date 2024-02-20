from ctypes import *
from ctypes.wintypes import *

MessageBoxA = windll.user32.MessageBoxA
MessageBoxA.argtypes=(HWND, LPCSTR, LPCSTR, UINT)
MessageBoxA.restype=INT

print(MessageBoxA)

lpText = LPCSTR(b"World")
lpCaptopn = LPCSTR(b"Hello")
MB_OK=0x0000000

#MessageBoxA(None, lpText, lpCaptopn, MB_OK)

GetUserNameA=windll.advapi32.GetUserNameA
GetUserNameA.argtypes=(LPSTR, LPDWORD)
GetUserNameA.restype = INT

buffer_size=DWORD(2)
buffer=create_string_buffer(buffer_size.value)

GetUserNameA(buffer, byref(buffer_size))
print(buffer.value)

error = GetLastError()
if error:
    #print(error)
    print(WinError(error))

class RECT(Structure):
    _fields_=[("left", c_long),
              ("top",c_long),
              ("right", c_long),
              ("bottom", c_long)]
rect=RECT()

print(rect.left)

GetWindowRect = windll.user32.GetWindowRect
GetWindowRect.argtypes=(HANDLE, POINTER(RECT))
GetWindowRect.restype=BOOL

hwnd = windll.user32.GetForegroundWindow()
GetWindowRect(hwnd, byref(rect))

print(rect.left)


#undocumented

kernel32=windll.kernel32
SIZE_T =c_size_t
VirtualAlloc = kernel32.VirtualAlloc
#VirtualAlloc.argtypes=(wintypes)