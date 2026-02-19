import os
import shutil
from dataclasses import dataclass
from typing import List, Tuple, Optional

@dataclass
class function:
    name: str             
    return_type: str          
    arg_types: List[str]         
    arg_names: List[str]        
    is_complex: bool = False       # флаг комплексной функции
    is_return_void: bool = True    # функция возвращает void?
    precision: str = "s"           # s/d/c/z/cs/zd/sc/dz/sds/ds

FUNCTIONS = [
    function("cblas_sdsdot", "float", 
                  ["int", "float", "const float*", "int", "const float*", "int"],
                  ["N", "alpha", "X", "incX", "Y", "incY"],
                  is_return_void=False, precision="sds"),
    function("cblas_dsdot", "double",
                  ["int", "const float*", "int", "const float*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  is_return_void=False, precision="ds"),
    function("cblas_sdot", "float",
                  ["int", "const float*", "int", "const float*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  is_return_void=False, precision="s"),
    function("cblas_ddot", "double",
                  ["int", "const double*", "int", "const double*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  is_return_void=False, precision="d"),
    # Functions having prefixes Z and C only
    function("cblas_cdotu_sub", "void",
                  ["int", "const void*", "int", "const void*", "int", "void*"],
                  ["N", "X", "incX", "Y", "incY", "dotu"],
                  is_complex=True, precision="c"),
    function("cblas_cdotc_sub", "void",
                  ["int", "const void*", "int", "const void*", "int", "void*"],
                  ["N", "X", "incX", "Y", "incY", "dotc"],
                  is_complex=True, precision="c"),
    function("cblas_zdotu_sub", "void",
                  ["int", "const void*", "int", "const void*", "int", "void*"],
                  ["N", "X", "incX", "Y", "incY", "dotu"],
                  is_complex=True, precision="z"),
    function("cblas_zdotc_sub", "void",
                  ["int", "const void*", "int", "const void*", "int", "void*"],
                  ["N", "X", "incX", "Y", "incY", "dotc"],
                  is_complex=True, precision="z"),
    #Functions having prefixes S D SC DZ
    function("cblas_snrm2", "float",
                  ["int", "const float*", "int"],
                  ["N", "X", "incX"],
                  is_return_void=False, precision="s"),
    function("cblas_sasum", "float",
                  ["int", "const float*", "int"],
                  ["N", "X", "incX"],
                  is_return_void=False, precision="s"),
    function("cblas_dnrm2", "double",
                  ["int", "const double*", "int"],
                  ["N", "X", "incX"],
                  is_return_void=False, precision="d"),
    function("cblas_dasum", "double",
                  ["int", "const double*", "int"],
                  ["N", "X", "incX"],
                  is_return_void=False, precision="d"),
    function("cblas_scnrm2", "float",
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  is_complex=True, is_return_void=False, precision="sc"),
    function("cblas_scasum", "float",
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  is_complex=True, is_return_void=False, precision="sc"),
    function("cblas_dznrm2", "double",
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  is_complex=True, is_return_void=False, precision="dz"),
    function("cblas_dzasum", "double",
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  is_complex=True, is_return_void=False, precision="dz"),
    #Functions having standard 4 prefixes (S D C Z)
    function("cblas_isamax", "CBLAS_INDEX",
                  ["int", "const float*", "int"],
                  ["N", "X", "incX"],
                  is_return_void=False, precision="s"),
    function("cblas_idamax", "CBLAS_INDEX",
                  ["int", "const double*", "int"],
                  ["N", "X", "incX"],
                  is_return_void=False, precision="d"),
    function("cblas_icamax", "CBLAS_INDEX",
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  is_complex=True, is_return_void=False, precision="c"),
    function("cblas_izamax", "CBLAS_INDEX",
                  ["int", "const void*", "int"],
                  ["N", "X", "incX"],
                  is_complex=True, is_return_void=False, precision="z"),
    
    # Routines with standard 4 prefixes (s, d, c, z)
    function("cblas_sswap", "void",
                  ["int", "float*", "int", "float*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="s"),
    function("cblas_scopy", "void",
                  ["int", "const float*", "int", "float*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="s"),
    function("cblas_saxpy", "void",
                  ["int", "float", "const float*", "int", "float*", "int"],
                  ["N", "alpha", "X", "incX", "Y", "incY"],
                  precision="s"),
    function("cblas_dswap", "void",
                  ["int", "double*", "int", "double*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="d"),
    function("cblas_dcopy", "void",
                  ["int", "const double*", "int", "double*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  precision="d"),
    function("cblas_daxpy", "void",
                  ["int", "double", "const double*", "int", "double*", "int"],
                  ["N", "alpha", "X", "incX", "Y", "incY"],
                  precision="d"),
    function("cblas_cswap", "void",
                  ["int", "void*", "int", "void*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  is_complex=True, precision="c"),
    function("cblas_ccopy", "void",
                  ["int", "const void*", "int", "void*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  is_complex=True, precision="c"),
    function("cblas_caxpy", "void",
                  ["int", "const void*", "const void*", "int", "void*", "int"],
                  ["N", "alpha", "X", "incX", "Y", "incY"],
                  is_complex=True, precision="c"),
    function("cblas_zswap", "void",
                  ["int", "void*", "int", "void*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  is_complex=True, precision="z"),
    function("cblas_zcopy", "void",
                  ["int", "const void*", "int", "void*", "int"],
                  ["N", "X", "incX", "Y", "incY"],
                  is_complex=True, precision="z"),
    function("cblas_zaxpy", "void",
                  ["int", "const void*", "const void*", "int", "void*", "int"],
                  ["N", "alpha", "X", "incX", "Y", "incY"],
                  is_complex=True, precision="z"),
    
    #Routines with S and D prefix only
    function("cblas_srotg", "void",
                  ["float*", "float*", "float*", "float*"],
                  ["a", "b", "c", "s"],
                  precision="s"),
    function("cblas_srotmg", "void",
                  ["float*", "float*", "float*", "float", "float*"],
                  ["d1", "d2", "b1", "b2", "P"],
                  precision="s"),
    function("cblas_srot", "void",
                  ["int", "float*", "int", "float*", "int", "float", "float"],
                  ["N", "X", "incX", "Y", "incY", "c", "s"],
                  precision="s"),
    function("cblas_srotm", "void",
                  ["int", "float*", "int", "float*", "int", "const float*"],
                  ["N", "X", "incX", "Y", "incY", "P"],
                  precision="s"),
    function("cblas_drotg", "void",
                  ["double*", "double*", "double*", "double*"],
                  ["a", "b", "c", "s"],
                  precision="d"),
    function("cblas_drotmg", "void",
                  ["double*", "double*", "double*", "double", "double*"],
                  ["d1", "d2", "b1", "b2", "P"],
                  precision="d"),
    function("cblas_drot", "void",
                  ["int", "double*", "int", "double*", "int", "double", "double"],
                  ["N", "X", "incX", "Y", "incY", "c", "s"],
                  precision="d"),
    function("cblas_drotm", "void",
                  ["int", "double*", "int", "double*", "int", "const double*"],
                  ["N", "X", "incX", "Y", "incY", "P"],
                  precision="d"),
    #extra 4 
    function("cblas_crotg", "void",
                  ["void*", "void*", "float*", "void*"],
                  ["a", "b", "c", "s"],
                  is_complex=True, precision="c"),
    function("cblas_zrotg", "void",
                  ["void*", "void*", "double*", "void*"],
                  ["a", "b", "c", "s"],
                  is_complex=True, precision="z"),
    function("cblas_csrot", "void",
                ["int", "void*", "int", "void*", "int", "float", "float"],
                ["N", "X", "incX", "Y", "incY", "c", "s"],
                is_complex=True, precision="cs"),

    function("cblas_zdrot", "void",
                ["int", "void*", "int", "void*", "int", "double", "double"],
                ["N", "X", "incX", "Y", "incY", "c", "s"],
                is_complex=True, precision="zd"),
    
    #outines with S D C Z CS and ZD prefixes
    function("cblas_sscal", "void",
                  ["int", "float", "float*", "int"],
                  ["N", "alpha", "X", "incX"],
                  precision="s"),
    function("cblas_dscal", "void",
                  ["int", "double", "double*", "int"],
                  ["N", "alpha", "X", "incX"],
                  precision="d"),
    function("cblas_cscal", "void",
                  ["int", "const void*", "void*", "int"],
                  ["N", "alpha", "X", "incX"],
                  is_complex=True, precision="c"),
    function("cblas_zscal", "void",
                  ["int", "const void*", "void*", "int"],
                  ["N", "alpha", "X", "incX"],
                  is_complex=True, precision="z"),
    function("cblas_csscal", "void",
                  ["int", "float", "void*", "int"],
                  ["N", "alpha", "X", "incX"],
                  is_complex=True, precision="cs"),
    function("cblas_zdscal", "void",
                  ["int", "double", "void*", "int"],
                  ["N", "alpha", "X", "incX"],
                  is_complex=True, precision="zd"),
    
]

TEMPLATE = """\
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

// Тестовые данные для разных случаев
#define TEST_N_VALUES { 0, 5, 3, 1, 7 }
#define TEST_INC_VALUES { 1, 2, -1, 0 }
#define TEST_ALPHA_FLOAT { 0.0f, 1.0f, -2.5f, 0.5f }
#define TEST_ALPHA_DOUBLE { 0.0, 1.0, -2.5, 0.5 }
"""

# Префиксы и соответствующие типы
TYPE_INFO = {
    "s": {"c_type": "float", "c_type_str": "float", "complex": False},
    "d": {"c_type": "double", "c_type_str": "double", "complex": False},
    "c": {"c_type": "float complex", "c_type_str": "float", "complex": True},
    "z": {"c_type": "double complex", "c_type_str": "double", "complex": True},
    "sc": {"c_type": "float complex", "c_type_str": "float", "complex": True},
    "dz": {"c_type": "double complex", "c_type_str": "double", "complex": True},
    "cs": {"c_type": "float complex", "c_type_str": "float", "complex": True},
    "zd": {"c_type": "double complex", "c_type_str": "double", "complex": True},
    "sds": {"c_type": "float", "c_type_str": "float", "complex": False},  # специальный случай
    "ds": {"c_type": "float", "c_type_str": "float", "complex": False},   # специальный случай
}

# ============================================================================
# Генератор тестов
# ============================================================================

def get_base_type_from_precision(precision: str) -> str:
    """Определяет базовый тип для заданной точности"""
    if precision in ["s", "sds"]:
        return "float"
    elif precision in ["d", "ds"]:
        return "double"
    elif precision in ["c", "sc", "cs"]:
        return "float complex"
    elif precision in ["z", "dz", "zd"]:
        return "double complex"
    return "float"

def generate_vector_declaration(func: CBLASFunction) -> str:
    """Генерирует минимальные данные для тестирования - один буфер на всё"""
    if func.precision in ["s", "d", "sds", "ds"]:
        if func.precision in ["s", "sds", "ds"] 
            base_type = "float" 
        else base_type = "double"
        return f"""\

                    #define TEST_BUFFER_SIZE  10
                    {base_type} test_buffer [TEST_BUFFER_SIZE];
                    for (int i = 0; i < TEST_BUFFER_SIZE ; i++) {{
                        test_buffer [i] = ({base_type})(i + 1);
                    }}"""
    else:
        # Комплексные типы
        if func.precision in ["c", "sc", "cs"]:
            base_type = "float complex"

        else:  # "z", "dz", "zd"
            base_type = "double complex"
        
        return f"""\

                    #define TEST_BUFFER_SIZE  10
                    {base_type} test_buffer [TEST_BUFFER_SIZE ];
                    for (int i = 0; i < TEST_BUFFER_SIZE ; i++) {{
                        test_buffer [i] = (i+1) + (i+1)*I;
                    }}"""

def generate_test_cases(func: function) -> str:
    """Генерирует код с тестовыми случаями"""
    lines = []
    
    # Определение базового типа
    base_type = get_base_type_from_precision(func.precision)
    
    # Массивы тестовых значений
    lines.append("    // Массивы тестовых значений")
    
    if "alpha" in func.arg_names:
        if base_type == "float":
            lines.append("    float alpha_values[] = {0.0f, 1.0f, -2.5f, 0.5f, 3.0f};")
            lines.append("    int num_alphas = 5;")
        else:
            lines.append("    double alpha_values[] = {0.0, 1.0, -2.5, 0.5, 3.0};")
            lines.append("    int num_alphas = 5;")
    
    lines.append("    int n_values[] = {0, 1,2,3,5};")
    lines.append("    int inc_values[] = {1, 2};")
    lines.append("    int num_n = 5;")
    lines.append("    int num_inc = 2;")
    
    # Перебор всех комбинаций
    lines.append("\n    // Перебор всех комбинаций параметров")
    lines.append("    for (int i_n = 0; i_n < num_n; i_n++) {")
    lines.append("        int n = n_values[i_n];")
    lines.append("        for (int i_inc = 0; i_inc < num_inc; i_inc++) {")
    lines.append("            int inc = inc_values[i_inc];")
    
    # Вложенные циклы для alpha, если есть
    if "alpha" in func.arg_names and func.name not in ["cblas_caxpy", "cblas_zaxpy"]:
        lines.append("            for (int i_alpha = 0; i_alpha < num_alphas; i_alpha++) {")
        if base_type == "float":
            lines.append("                float alpha = alpha_values[i_alpha];")
        else:
            lines.append("                double alpha = alpha_values[i_alpha];")
    
    # Для комплексных функций с alpha как const void*
    elif "alpha" in func.arg_names and func.is_complex:
        lines.append("            for (int i_alpha = 0; i_alpha < num_alphas; i_alpha++) {")
        if "float" in str(base_type):
            lines.append(f"                {base_type} alpha = alpha_values[i_alpha] + alpha_values[i_alpha]*I;")
        else:
            lines.append(f"                {base_type} alpha = alpha_values[i_alpha] + alpha_values[i_alpha]*I;")
    
    # Вызов функции
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
            if func.name == "cblas_dsdot":
                # dsdot требует float*, а не double*
                args.append(f"(const float*)test_buffer")
            elif "const" in arg_type:
                args.append(f"(const {base_type}*)test_buffer")
            else:
                args.append(f"test_buffer")
                # Для rotg/rotmg функций
        elif arg_name in ["a", "b", "d1", "d2", "b1"]:
            if arg_type.endswith('*'):
                args.append(f"&{arg_name}_val")
            else:
                args.append(f"{arg_name}_val")
        elif arg_name in ["c", "s"]:
            # Специальная обработка для crotg/zrotg
            if func.name in ["cblas_crotg", "cblas_zrotg"]:
                if arg_name == "c":
                    # c - указатель на float (для crotg) или double (для zrotg)
                    args.append(f"&{arg_name}_val")
                else:  # s - указатель на void* (комплексное число)
                    args.append(f"(void*)&{arg_name}_val")
            elif func.name in ["cblas_csrot", "cblas_zdrot"]:
                args.append(f"{arg_name}_val")  # по значению для csrot/zdrot
            else:
                if arg_type.endswith('*'):
                    args.append(f"&{arg_name}_val")
                else:
                    args.append(f"{arg_name}_val")
        elif arg_name == "P":
            args.append("P_param")
        elif arg_name in ["dotu", "dotc"]:
            # Для *_sub функций
            result_var = "result_" + arg_name
            args.append(f"&{result_var}")
        elif arg_name == "b2":
            if base_type == "float":
                args.append("2.0f")
            else:
                args.append("2.0")
        else:
            args.append(arg_name)
    
    call += ", ".join(args) + ");"
    lines.append(call)
    
    # Закрытие циклов
    if "alpha" in func.arg_names:
        lines.append("            }")
    lines.append("        }")
    lines.append("    }")
    
    return "\n".join(lines)

def generate_test_file(func: function) -> str:
    """Генерирует полный код тестового файла для одной функции"""
    content = []
    
    # Заголовок
    content.append(f"""\
/*
 * Тест для функции {func.name}
 * Проверяет успешность вызова с различными параметрами
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include "cblas.h"

int main(int argc, char** argv) {{
    printf("Тестирование {func.name}...\\n");
""")
    
     # Объявление переменных для функций вращения (rot)
    if "rotg" in func.name or "rotmg" in func.name or "rot" in func.name or "rotm" in func.name:
        if func.name.startswith("cblas_s"):  # float версии
            content.append("    float a_val = 1.0f, b_val = 2.0f, c_val = 0.5f, s_val = 0.5f;")
            content.append("    float d1_val = 1.0f, d2_val = 2.0f, b1_val = 3.0f, P_param[5] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f};")
        elif func.name.startswith("cblas_d"):  # double версии
            content.append("    double a_val = 1.0, b_val = 2.0, c_val = 0.5, s_val = 0.5;")
            content.append("    double d1_val = 1.0, d2_val = 2.0, b1_val = 3.0, P_param[5] = {1.0, 2.0, 3.0, 4.0, 5.0};")
        elif func.name == "cblas_csrot":  # complex float с real c,s
            content.append("    float c_val = 0.5f, s_val = 0.5f;")
        elif func.name == "cblas_zdrot":  # complex double с real c,s
            content.append("    double c_val = 0.5, s_val = 0.5;")
        elif func.name == "cblas_crotg":  # complex float rotg
            content.append("    float complex a_val = 1.0f + 1.0f*I, b_val = 2.0f + 2.0f*I;")
            content.append("    float c_val = 0.5f;")
            content.append("    float complex s_val = 0.5f + 0.5f*I;")
        elif func.name == "cblas_zrotg":  # complex double rotg
            content.append("    double complex a_val = 1.0 + 1.0*I, b_val = 2.0 + 2.0*I;")
            content.append("    double c_val = 0.5;")
            content.append("    double complex s_val = 0.5 + 0.5*I;")
    
    # Объявление векторов
    content.append(generate_vector_declaration(func))
    
    # Для функций с возвратом значения через аргумент
    if func.name in ["cblas_cdotu_sub", "cblas_cdotc_sub", "cblas_zdotu_sub", "cblas_zdotc_sub"]:
        base_type = get_base_type_from_precision(func.precision)
        content.append(f"\n    {base_type} result_dotu, result_dotc;")
    
    # Генерация тестовых случаев
    content.append(generate_test_cases(func))
    
    # Завершение
    content.append("""
    printf("Тест пройден успешно!\\n");
    return 0;
}""")
    
    return "\n".join(content)

def generate_makefile():
    """Генерирует Makefile для компиляции всех тестов (для размещения в папке tests)"""
    return """\
CC = gcc
CFLAGS = -Wall -O2 -g -I../OpenBLAS
LDFLAGS = -L../OpenBLAS -lopenblas -lm

# Все тестовые программы (ищем в текущей директории)
SOURCES = $(wildcard test_*.c)
TARGETS = $(SOURCES:.c=)

all: $(TARGETS)

%: %.c
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

clean:
	rm -f $(TARGETS)

run: all
	@echo "Запуск всех тестов..."
	@for test in $(TARGETS); do \\
		echo -n "Запуск $$test ... "; \\
		./$$test > /dev/null 2>&1 && echo "УСПЕХ" || echo "ПРОВАЛ"; \\
	done

.PHONY: all clean run
"""

def generate_run_script():
    """Генерирует скрипт для запуска тестов (для размещения в папке tests)"""
    return """\
#!/bin/bash

echo "Запуск всех тестов CBLAS Level 1"
echo "================================"
echo

FAILED=0
PASSED=0

for test in test_*; do
    # Пропускаем если это не исполняемый файл или это исходный код
    if [ -x "$test" ] && [ ! "${test##*.}" = "c" ] && [ ! "${test##*.}" = "sh" ]; then
        echo -n "Запуск $test ... "
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
echo "Результаты: Пройдено: $PASSED, Провалено: $FAILED"

if [ $FAILED -eq 0 ]; then
    echo "ИТОГО: УСПЕХ"
    exit 0
else
    echo "ИТОГО: ПРОВАЛ"
    exit 1
fi
"""

# ============================================================================
# Основная функция
# ============================================================================

def main():
    """Главная функция генератора"""
    print("Генерация тестов CBLAS Level 1...")
    
    # Создание директории для тестов
    if not os.path.exists("tests"):
        os.makedirs("tests")
        print("  - Создана директория tests/")
    else:
        # Очистка старых тестов
        for file in os.listdir("tests"):
            if file.startswith("test_") and (file.endswith(".c") or not os.path.splitext(file)[1]):
                file_path = os.path.join("tests", file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"  - Удалён старый файл {file}")
    
    # Поиск заголовочного файла
    header_copied = False
    openblas_header = os.path.join("OpenBLAS", "cblas.h")
    if os.path.exists(openblas_header):
        shutil.copy(openblas_header, "tests/cblas.h")
        print("  - cblas.h скопирован из OpenBLAS/ в tests/")
        header_copied = True
    else:
        print("  ! ВНИМАНИЕ: cblas.h не найден! Тесты могут не скомпилироваться.")
        print("    Убедитесь, что файл cblas.h есть в текущей директории.")
    
    # Генерация тестов для каждой функции
    generated = 0
    for func in FUNCTIONS:
        filename = os.path.join("tests", f"test_{func.name}.c")
        with open(filename, "w") as f:
            f.write(generate_test_file(func))
        generated += 1
        if generated <= 5 or generated % 10 == 0:  # Показываем прогресс
            print(f"  - Создан test_{func.name}.c")
    
    # Генерация Makefile в папке tests
    makefile_path = os.path.join("tests", "Makefile")
    with open(makefile_path, "w") as f:
        f.write(generate_makefile())
    print("  - Создан tests/Makefile")
    
    # Генерация скрипта запуска в папке tests
    runscript_path = os.path.join("tests", "run.sh")
    with open(runscript_path, "w") as f:
        f.write(generate_run_script())
    # Делаем скрипт исполняемым
    os.chmod(runscript_path, 0o755)
    print("  - Создан tests/run.sh")
    
    print(f"\nГотово! Создано {generated} тестовых файлов в директории tests/")
    
    if header_copied:
        print("\nДальнейшие действия:")
        print("  cd tests")
        print("  make         # компиляция всех тестов")
        print("  ./run.sh     # запуск тестов")
        print("  или просто: make run  # компиляция и запуск одной командой")
    else:
        print("\nВНИМАНИЕ: Сначала скопируйте cblas.h в директорию tests/")

if __name__ == "__main__":
    main()

#make ./run.sh