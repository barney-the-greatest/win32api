#script to create registry key. 
import _winreg

#variables to specify contents of the key.
reg_var = _winreg.HKEY_LOCAL_MACHINE
string_var = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\policies\\system"
key_value = "LocalAccountTokenFilterPolicy"
key_type = "_winreg.REG_DWORD"
#open handle to the key, creates the key, gives the values to the key.
x = _winreg.OpenKeyEx(reg_var, string_var, 0, _winreg.KEY_ALL_ACCESS)
y = _winreg.CreateKey(x, key_value, )
y = _winreg.SetValueEx(y, key_value,key_type,1,'1',)

#remember to close key
x = _winreg.CloseKey(x)