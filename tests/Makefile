CC = gcc
CFLAGS = -Wall -O2 -g -I../OpenBLAS
LDFLAGS = -L../OpenBLAS -lopenblas -lm

#LDFLAGS = -L../Wrong_OpenBLAS -lwrongblas -lm

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
	@for test in $(TARGETS); do \
		echo -n "Запуск $$test ... "; \
		./$$test > /dev/null 2>&1 && echo "УСПЕХ" || echo "ПРОВАЛ"; \
	done

.PHONY: all clean run
