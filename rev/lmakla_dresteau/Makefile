CXX = g++
CXXFLAGS = -std=c++17 -Wall
TARGET = challenge
SOURCE = challenge.cpp
all: release
release: $(SOURCE) cryptosystem.hpp meta_random.hpp
	$(CXX) $(CXXFLAGS) -O2 -o $(TARGET) $(SOURCE)
	strip $(TARGET)

clean:
	rm -f $(TARGET)

.PHONY: all release
