# laikaboss modules 

Use at your own risk


explode_rtf.py

Installation:
1. Add explode_rtf.py to modules folder
2. Modify dispatch.yara to include the module:
     
rule type_is_rtf
{
    meta:
        scan_modules = "EXPLODE_RTF"
        file_type = "rtf"
    condition:
        uint32(0) == 0x74725c7b
}

