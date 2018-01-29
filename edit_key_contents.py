import _winreg
#variables to open the desired reg key.
reg_parent = _winreg.HKEY_LOCAL_MACHINE
string_var = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\policies\\system"
new_key = "LocalAccountTokenFilterPolicy"

#variables to substitute
key_name = "key-name"
key_type = _winreg.REG_DWORD #type of key
key_value = 0x00000001 #type in hex, dword requires hex types.

#section to implement the changes to known reg keys
#use OpenKeyEx/SetValueEx if you want to be able to set the key_type to be anything other than purely reg_sz (string), e.g. dword.
x = _winreg.OpenKeyEx(reg_parent, string_var, 0, _winreg.KEY_ALL_ACCESS)
#0 after key_name here has to be passed in.
y = _winreg.SetValueEx(x, key_name,0,key_type,key_value)

#remember to close key
x = _winreg.CloseKey(x)
