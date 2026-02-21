CFLAGS = -Wall -fPIC  # -fPIC - можно размещать в любом месте памяти 
LIB_NAME = libwrongblas.so
SRCS = $(wildcard src/*.c)
OBJS = $(SRCS:.c=.o)

all: $(LIB_NAME)

$(LIB_NAME): $(OBJS)
	gcc -shared -o $@ $^ -lm

%.o: %.c
	gcc $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(LIB_NAME)
