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
