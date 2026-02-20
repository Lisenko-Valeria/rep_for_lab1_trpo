CC = gcc
CFLAGS = -Wall -O2 -fPIC  # -fPIC обязателен для разделяемой библиотеки
LIB_NAME = libwrongblas.so
SRCDIR = src
SRCS = $(wildcard $(SRCDIR)/*.c)
OBJS = $(SRCS:.c=.o)

all: $(LIB_NAME)

$(LIB_NAME): $(OBJS)
	$(CC) -shared -o $@ $^ -lm

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(LIB_NAME)

.PHONY: all clean