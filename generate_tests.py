import os
import shutil
from dataclasses import dataclass
from typing import List

@dataclass
class function:
    name: str                      
    arg_types: List[str]         
    arg_names: List[str]             
    precision: str = "s"          

FUNCTIONS = [
    function("cblas_sdsdot", 
                  ["int", "float", "const float*", "int", "const float*", "int"],
                  ["N", "alpha", "X", "incX", "Y", "incY"],
                  precision="sds"),
    function("cblas_dsdot", 
                  ["int", "const float*", "int", "const float*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="ds"),
    function("cblas_sdot", 
                  ["int", "const float*", "int", "const float*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="s"),
    function("cblas_ddot", 
                  ["int", "const double*", "int", "const double*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="d"),
    # Functions having prefixes Z and C only
    function("cblas_cdotu_sub", 
                  ["int", "const void*", "int", "const void*", "int", "void*"],
                  ["N", "X", "incX", "Y", "incY", "dotu"],
                  precision="c"),
    function("cblas_cdotc_sub", 
                  ["int", "const void*", "int", "const void*", "int", "void*"],
                  ["N", "X", "incX", "Y", "incY", "dotc"],
                  precision="c"),
    function("cblas_zdotu_sub", 
                  ["int", "const void*", "int", "const void*", "int", "void*"],
                  ["N", "X", "incX", "Y", "incY", "dotu"],
                  precision="z"),
    function("cblas_zdotc_sub", 
                  ["int", "const void*", "int", "const void*", "int", "void*"],
                  ["N", "X", "incX", "Y", "incY", "dotc"],
                  precision="z"),
    #Functions having prefixes S D SC DZ
    function("cblas_snrm2", 
                  ["int", "const float*", "int"],
                  ["N", "X", "incX"],
                  precision="s"),
    function("cblas_sasum", 
                  ["int", "const float*", "int"],
                  ["N", "X", "incX"],
                  precision="s"),
    function("cblas_dnrm2", 
                  ["int", "const double*", "int"],
                  ["N", "X", "incX"],
                  precision="d"),
    function("cblas_dasum", 
                  ["int", "const double*", "int"],
                  ["N", "X", "incX"],
                  precision="d"),
    function("cblas_scnrm2", 
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  precision="sc"),
    function("cblas_scasum", 
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  precision="sc"),
    function("cblas_dznrm2", 
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  precision="dz"),
    function("cblas_dzasum", 
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  precision="dz"),
    #Functions having standard 4 prefixes (S D C Z)
    function("cblas_isamax", 
                  ["int", "const float*", "int"],
                  ["N", "X", "incX"],
                  precision="s"),
    function("cblas_idamax", 
                  ["int", "const double*", "int"],
                  ["N", "X", "incX"],
                  precision="d"),
    function("cblas_icamax", 
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  precision="c"),
    function("cblas_izamax", 
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  precision="z"),
    
    # Routines with standard 4 prefixes (s, d, c, z)
    function("cblas_sswap", 
                  ["int", "float*", "int", "float*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="s"),
    function("cblas_scopy", 
                  ["int", "const float*", "int", "float*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="s"),
    function("cblas_saxpy", 
                  ["int", "float", "const float*", "int", "float*", "int"],
                  ["N", "alpha", "X", "incX", "Y", "incY"],
                  precision="s"),
    function("cblas_dswap", 
                  ["int", "double*", "int", "double*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="d"),
    function("cblas_dcopy", 
                  ["int", "const double*", "int", "double*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="d"),
    function("cblas_daxpy", 
                  ["int", "double", "const double*", "int", "double*", "int"],
                  ["N", "alpha", "X", "incX", "Y", "incY"],
                  precision="d"),
    function("cblas_cswap", 
                  ["int", "void*", "int", "void*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="c"),
    function("cblas_ccopy", 
                  ["int", "const void*", "int", "void*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="c"),
    function("cblas_caxpy", 
                  ["int", "const void*", "const void*", "int", "void*", "int"],
                  ["N", "alpha", "X", "incX", "Y", "incY"],
                  precision="c"),
    function("cblas_zswap", 
                  ["int", "void*", "int", "void*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="z"),
    function("cblas_zcopy", 
                  ["int", "const void*", "int", "void*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="z"),
    function("cblas_zaxpy", 
                  ["int", "const void*", "const void*", "int", "void*", "int"],
                  ["N", "alpha", "X", "incX", "Y", "incY"],
                  precision="z"),
    
    #Routines with S and D prefix only
    function("cblas_srotg", 
                  ["float*", "float*", "float*", "float*"],
                  ["a", "b", "c", "s"],
                  precision="s"),
    function("cblas_srotmg", 
                  ["float*", "float*", "float*", "float", "float*"],
                  ["d1", "d2", "b1", "b2", "P"],
                  precision="s"),
    function("cblas_srot", 
                  ["int", "float*", "int", "float*", "int", "float", "float"],
                  ["N", "X", "incX", "Y", "incY", "c", "s"],
                  precision="s"),
    function("cblas_srotm", 
                  ["int", "float*", "int", "float*", "int", "const float*"],
                  ["N", "X", "incX", "Y", "incY", "P"],
                  precision="s"),
    function("cblas_drotg", 
                  ["double*", "double*", "double*", "double*"],
                  ["a", "b", "c", "s"],
                  precision="d"),
    function("cblas_drotmg", 
                  ["double*", "double*", "double*", "double", "double*"],
                  ["d1", "d2", "b1", "b2", "P"],
                  precision="d"),
    function("cblas_drot", 
                  ["int", "double*", "int", "double*", "int", "double", "double"],
                  ["N", "X", "incX", "Y", "incY", "c", "s"],
                  precision="d"),
    function("cblas_drotm", 
                  ["int", "double*", "int", "double*", "int", "const double*"],
                  ["N", "X", "incX", "Y", "incY", "P"],
                  precision="d"),
    #extra 4 
    function("cblas_crotg", 
                  ["void*", "void*", "float*", "void*"],
                  ["a", "b", "c", "s"],
                  precision="c"),
    function("cblas_zrotg", 
                  ["void*", "void*", "double*", "void*"],
                  ["a", "b", "c", "s"],
                  precision="z"),
    function("cblas_csrot", 
                ["int", "void*", "int", "void*", "int", "float", "float"],
                ["N", "X", "incX", "Y", "incY", "c", "s"],
                precision="cs"),

    function("cblas_zdrot", 
                ["int", "void*", "int", "void*", "int", "double", "double"],
                ["N", "X", "incX", "Y", "incY", "c", "s"],
                precision="zd"),
    
    #outines with S D C Z CS and ZD prefixes
    function("cblas_sscal", 
                  ["int", "float", "float*", "int"],
                  ["N", "alpha", "X", "incX"],
                  precision="s"),
    function("cblas_dscal", 
                  ["int", "double", "double*", "int"],
                  ["N", "alpha", "X", "incX"],
                  precision="d"),
    function("cblas_cscal", 
                  ["int", "const void*", "void*", "int"],
                  ["N", "alpha", "X", "incX"],
                  precision="c"),
    function("cblas_zscal", 
                  ["int", "const void*", "void*", "int"],
                  ["N", "alpha", "X", "incX"],
                  precision="z"),
    function("cblas_csscal", 
                  ["int", "float", "void*", "int"],
                  ["N", "alpha", "X", "incX"],
                  precision="cs"),
    function("cblas_zdscal", 
                  ["int", "double", "void*", "int"],
                  ["N", "alpha", "X", "incX"],
                  precision="zd"),
]

def get_base_type_from_precision(precision: str) -> str:
    if precision in ["s", "sds", "ds"]:
        return "float"
    elif precision in ["d"]:
        return "double"
    elif precision in ["c", "sc", "cs"]:
        return "float complex"
    elif precision in ["z", "dz", "zd"]:
        return "double complex"

def generate_test_cases(func: function) -> str:

    lines = []
    
    base_type = get_base_type_from_precision(func.precision)
    if "float" in base_type :
        base_type_f = "f"
    elif "double" in base_type:
        base_type_f = "" 
    base_type_simple = base_type.split()[0]  # float/double

    
    # ПЕРЕМЕННЫЕ
    lines.append("     // Переменные")

    if "rotg" not in func.name and "rotmg" not in func.name:
        lines.append("    int n = 1;")
        lines.append("    int inc = 1;")
    
    # Объявление переменных a, b, c, s, d1, d2, b1, b2, param для функций rot
    if "rotg" in func.name or "rotmg" in func.name or "rot" in func.name or "rotm" in func.name:
        # extra (c z)
        if func.name in  ["cblas_crotg", "cblas_zrotg"] :
            lines.append(f"    {base_type} a_val = 1.0{base_type_f} + 1.0{base_type_f}*I, b_val = 2.0{base_type_f} + 2.0{base_type_f}*I;")
            lines.append(f"    {base_type_simple} c_val = 0.5{base_type_f};")
            lines.append(f"    {base_type} s_val = 0.5{base_type_f} + 0.5{base_type_f}*I;")

        # s d cs zd - не комплекс
        elif "rotg" in func.name:
            lines.append(f"    {base_type} a_val = 1.0{base_type_f}, b_val = 2.0{base_type_f}, c_val = 0.5{base_type_f}, s_val = 0.5{base_type_f};")
        elif "rotmg" in func.name:
            lines.append(f"    {base_type} d1_val = 1.0{base_type_f}, d2_val = 2.0{base_type_f}, b1_val = 1.0{base_type_f}, b2_val = 2.0{base_type_f}, P_param[5];")
        
        elif "rotm" in func.name:
            lines.append(f"    {base_type} P_param[5];") 
        elif "rot" in func.name:
            lines.append(f"    {base_type} c_val = 0.5{base_type_f}, s_val = 0.5{base_type_f};")               

    # Объявление переменных alpha для функций axpy scal
    if "alpha" in func.arg_names:
        alpha_type = func.arg_types[1]
        if "void" in alpha_type:
            # Для комплексных функций с указателем
            lines.append(f"        {base_type} alpha = 2.0{base_type_f} + 2.0{base_type_f}*I;")
        else:
            # Для скалярных функций
            lines.append(f"        {base_type} alpha = 2.0{base_type_f};")
    
    if "X" in func.arg_names or "Y" in func.arg_names:
        if "X" in func.arg_names:
            X_idx = func.arg_names.index("X")
            XY_type = func.arg_types[X_idx]
        else:
            Y_idx = func.arg_names.index("Y")
            XY_type = func.arg_types[Y_idx] 

        if "void" in XY_type:
            # Для комплексных функций 
            lines.append(f"        {base_type} XY = 2.0{base_type_f} + 2.0{base_type_f}*I;")
        else:
            lines.append(f"        {base_type} XY = 2.0{base_type_f};")
    
    #с возвратом значения через аргумент
    if func.name in ["cblas_cdotu_sub", "cblas_zdotu_sub"]:
        lines.append(f"\n    {base_type} dotu;")    
    elif func.name in ["cblas_cdotc_sub", "cblas_zdotc_sub"]:
        lines.append(f"\n    {base_type} dotc;")   

    lines.append("                // Вызов функции")
    call = f"                {func.name}("
    args = []
    
    for arg_name, arg_type in zip(func.arg_names, func.arg_types):
        if arg_name == "N":
            args.append("n")
        elif arg_name == "incX" or arg_name == "incY":
            args.append("inc")
        elif arg_name == "alpha":
            if "void*" in arg_type:
                args.append("&alpha")
            else:
                args.append("alpha")
        elif arg_name in ["X", "Y"]:
            args.append(f"&XY")

                # Для rotg/rotmg функций
        elif arg_name in ["a", "b", "d1", "d2", "b1", "b2", "c", "s"]:
            if arg_type.endswith('*'):
                args.append(f"&{arg_name}_val")
            else:
                args.append(f"{arg_name}_val")

        elif arg_name == "P":
            args.append("P_param")
        elif arg_name in ["dotu", "dotc"]:
            # Для *_sub функций
            args.append(f"&{arg_name}")

        else:
            args.append(arg_name) 
    
    call += ", ".join(args) + ");"
    lines.append(call)

    
    return "\n".join(lines)

def generate_test_file(func: function) -> str:
    content = []
    
    content.append(f"""\

//Тест для функции {func.name}
 

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {{
""")
    
    content.append(generate_test_cases(func))
    
    content.append("""
    return 0;
}""")
    
    return "\n".join(content)

def generate_makefile():
    return """\
CFLAGS = -Wall -I../OpenBLAS
#CFLAGS = -Wall -I../Wrong_OpenBLAS/include  #и удалить cblas bp ntcnjd

LDFLAGS = -L../OpenBLAS -lopenblas -lm
#LDFLAGS = -L../Wrong_OpenBLAS -lwrongblas -lm

C_FILES = $(wildcard test_*.c)
#C_FILES = test_cblas_drot.c test_cblas_dswap.c test_cblas_saxpy.c test_cblas_sdot.c test_cblas_zdotc_sub.c

EXECS = $(C_FILES:.c=)

all: $(EXECS)

%: %.c
	gcc $(CFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f $(EXECS)

"""

def generate_run_script():
    return """\
echo "Запуск всех тестов CBLAS Level 1"
echo

FAILED=0
PASSED=0

for test in test_*; do
#for test in "test_cblas_drot" "test_cblas_dswap" "test_cblas_saxpy" "test_cblas_sdot" "test_cblas_zdotc_sub"; do

    if [ -x "$test" ] && [ ! "${test##*.}" = "c" ] && [ ! "${test##*.}" = "sh" ]; then
        echo -n "ТЕСТ $test   -   "
        ./$test > /dev/null 2>&1
        if [ $? -eq 0 ]; then
            echo "УСПЕХ"
            PASSED=$((PASSED + 1))
        else
            echo "ПРОВАЛ"
            FAILED=$((FAILED + 1))
        fi
    fi
done

echo
echo "Пройдено: $PASSED, Провалено: $FAILED"

"""

def main():

    print("Генерация тестов CBLAS Level 1")
    
    if os.path.exists("tests"):
        shutil.rmtree("tests")
    os.makedirs("tests")

    shutil.copy("OpenBLAS/cblas.h", "tests/cblas.h")

    generated = 0
    for func in FUNCTIONS:
        with open(f"tests/test_{func.name}.c", "w") as f:
            f.write(generate_test_file(func))
        generated += 1
    
    with open("tests/Makefile", "w") as f:
        f.write(generate_makefile())
    with open("tests/run.sh", "w") as f:
        f.write(generate_run_script())

    os.chmod("tests/run.sh", 0o755)
    
    print(f"Создано {generated} тестовых файлов в директории tests/")
    

if __name__ == "__main__":
    main()


#python generate_tests.py
#cd /tests
#make 
#./run.sh