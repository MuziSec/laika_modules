# Copyright 2017 Chuck DiRaimondi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Note: Before inserting into your laika instance, remember to change the path in outfile (line 33) to your output path and to change the path of dnSpy.Console.exe (line 36) to the correct path on your machine

from laikaboss.objectmodel import ExternalVars, ModuleObject, ScanError
from laikaboss.si_module import SI_MODULE
from laikaboss import config
import os
import subprocess
import md5

class EXPLODE_DOTNET(SI_MODULE):
    def __init__(self):
        self.module_name = "EXPLODE_DOTNET"

    def _run(self, scanObject, result, depth, args):

        moduleResult = []
        success = "Decompiled dotnet results available in dir: \n"
        try:
            outfile = "<insert_output_dir>/%s/decompiled_%s/" % (scanObject.rootUID, scanObject.objectHash)
            filename = "e_decompiled_dotnet_%s" % md5.new(scanObject.filename).hexdigest()
            outname = "decompiled_%s/\n" % scanObject.objectHash
            subprocess.check_output(['mono','<path_to_exe>/dnSpy.Console.exe','--no-resx', '--no-sln', scanObject.filename, '-o', outfile])
            moduleResult.append(ModuleObject(buffer=success + outname,externalVars=ExternalVars(filename=filename)))
        except ScanError:
            raise

        return moduleResult

