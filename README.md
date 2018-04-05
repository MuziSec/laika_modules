# laikaboss modules 

Use at your own risk


explode_rtf.py

Installation:
1. Add explode_rtf.py to modules folder
2. Modify dispatch.yara to include the module:
```     
rule type_is_rtf
{
    meta:
        scan_modules = "EXPLODE_RTF"
        file_type = "rtf"
    condition:
        uint32(0) == 0x74725c7b
}
```


explode_dotnet.py
  Decompiles .NET executables and puts them in folder in output dir.

Dependency:
1. Install Mono
2. Download dnSpy

Installation:
1. Add explode_dotnet.py to modules folder
2. Modify dispatch.yara to include the module:
```
rule type_is_dotnet
{
   meta:
       scan_modules = "EXPLODE_DOTNET"
       file_type = "pe dotnet"

       strings:
               $lib = "mscoree.dll"
               $func = "_CorExeMain"
   condition:
       type_is_mz and $lib and $func
}
```
