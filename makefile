CC = gcc
CFLAGS = -fPIC -shared
SRC_DIR = ./engine/src
BUILD_DIR = ./engine/lib

# Najdi všechny .c soubory v SRC_DIR a změň příponu na .o pro BUILD_DIR
SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(patsubst $(SRC_DIR)/%.c, $(BUILD_DIR)/%.o, $(SRCS))

# Cíl, který kompiluje všechny .c soubory do .o v adresáři BUILD_DIR
all: $(OBJS)

# Pravidlo pro kompilaci jednotlivých .c souborů do .o
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | $(BUILD_DIR)
	$(CC) $(CFLAGS) -o $@ $<

# Pravidlo pro vytvoření adresáře BUILD_DIR, pokud neexistuje
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

# Pravidlo pro čištění výstupního adresáře
clean:
	rm -f $(BUILD_DIR)/*.o