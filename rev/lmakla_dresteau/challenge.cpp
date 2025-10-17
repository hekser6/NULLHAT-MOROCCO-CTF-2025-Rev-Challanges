#include <iostream>
#include <string>
#include <cstring>
#include "cryptosystem.hpp"

bool what_she_said(const char* input) {
    const char* secret = OBFUSCATE("makla_Drestau_au_!nadya");
    return strcmp(input, secret) == 0;
}

void reveal_flag() {
    const char* flag = OBFUSCATE("ELITESEC{Pr377Y_80r1N6_451_H4MZ4}");
    std::cout << flag << std::endl;
}

int main() {
    std::cout << "\nwhat she said ? : ";
    std::string input;
    std::getline(std::cin, input);

    if (what_she_said(input.c_str())) {
        reveal_flag();
        return 0;
    } else {
        return 1;
    }
}
