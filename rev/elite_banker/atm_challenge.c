#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define PIN_LENGTH 38

void print_banner() {
    printf("\n");
    printf("  ╔═══════════════════════════════════════╗\n");
    printf("  ║                                       ║\n");
    printf("  ║        ELITE BANK ATM SYSTEM          ║\n");
    printf("  ║           Version 3.7.1               ║\n");
    printf("  ║                                       ║\n");
    printf("  ╚═══════════════════════════════════════╝\n");
    printf("\n");
    printf("  [*] Initializing secure transaction module...\n");
    printf("  [*] Loading encryption protocols...\n");
    printf("  [*] Connecting to ELITE banking network...\n");
    printf("\n");
}

int verify_pin(char* pin) {
    if (strlen(pin) != PIN_LENGTH) {
        return 0;
    }
    if (pin[0] * 3 - pin[1] * 2 != 55) return 0;
    if (pin[1] + pin[2] - pin[3] != 65) return 0;
    if (pin[2] * pin[3] - pin[4] * 5 != 5787) return 0;
    if (pin[5] * 2 + pin[6] * 3 - pin[7] != 306) return 0;
    if (pin[7] - pin[8] + pin[9] * 2 != 80) return 0;
    if (pin[8] * pin[9] - pin[10] != 8316) return 0;
    if (pin[10] + pin[11] * 2 - pin[12] != 189) return 0;

    if (pin[11] * 5 - pin[12] * 3 + pin[13] != 383) return 0;
    if (pin[13] + pin[14] - pin[15] * 2 != 54) return 0;
    if (pin[14] * pin[15] - pin[16] * 3 != 4218) return 0;

    if (pin[16] + pin[17] * 4 - pin[18] != 419) return 0;
    if (pin[17] * 2 - pin[18] + pin[19] * 3 != 262) return 0;
    if (pin[19] - pin[20] * 2 + pin[21] != 0) return 0;

    if (pin[20] * 3 + pin[21] - pin[22] * 2 != 6) return 0;
    if (pin[22] + pin[23] * 5 - pin[24] != 492) return 0;
    if (pin[23] * pin[24] - pin[25] * 4 != 3932) return 0;

    if (pin[25] * 2 - pin[26] + pin[27] * 3 != 341) return 0;
    if (pin[26] + pin[27] - pin[28] * 2 != 103) return 0;
    if (pin[28] * 4 - pin[29] * 3 + pin[30] != 108) return 0;

    if (pin[29] * pin[30] - pin[31] * 5 != 2149) return 0;
    if (pin[30] + pin[31] * 2 - pin[32] != 94) return 0;
    if (pin[31] - pin[32] + pin[33] * 4 != 287) return 0;

    if (pin[32] * 3 - pin[33] + pin[34] * 2 != 303) return 0;
    if (pin[33] * pin[34] - pin[35] * 4 != 3552) return 0;
    if (pin[34] + pin[35] * 2 - pin[36] != 88) return 0;

    if (pin[35] - pin[36] + pin[37] * 3 != 367) return 0;
    if (pin[36] * 2 + pin[37] != 237) return 0;

    if (pin[0] + pin[10] + pin[20] + pin[30] != 215) return 0;
    if (pin[5] + pin[15] + pin[25] + pin[35] != 264) return 0;
    if (pin[1] + pin[11] + pin[21] + pin[31] != 290) return 0;

    int sum1 = 0, sum2 = 0;
    for (int i = 0; i < PIN_LENGTH; i += 2) {
        sum1 += pin[i];
    }
    for (int i = 1; i < PIN_LENGTH; i += 2) {
        sum2 += pin[i];
    }
    if (sum1 != 1391) return 0;
    if (sum2 != 1410) return 0;

    for (int i = 0; i < PIN_LENGTH; i++) {
        if (pin[i] < 32 || pin[i] > 126) return 0;
    }

    return 1;
}

int main() {
    char pin[256];

    print_banner();

    printf("  ╔═══════════════════════════════════════╗\n");
    printf("  ║  Please enter your secure PIN code:  ║\n");
    printf("  ╚═══════════════════════════════════════╝\n");
    printf("\n  PIN: ");

    if (fgets(pin, sizeof(pin), stdin) == NULL) {
        printf("\n  [!] Error reading input.\n\n");
        return 1;
    }
    pin[strcspn(pin, "\n")] = 0;

    printf("\n  [*] Verifying PIN against secure database...\n");
    printf("  [*] Running %d security checks...\n", PIN_LENGTH * 3);
    printf("  [*] Performing cryptographic validation...\n\n");

    if (verify_pin(pin)) {
        printf("  ╔═══════════════════════════════════════╗\n");
        printf("  ║                                       ║\n");
        printf("  ║       ✓ ACCESS GRANTED ✓              ║\n");
        printf("  ║                                       ║\n");
        printf("  ║   Welcome, Elite Security Officer!   ║\n");
        printf("  ║                                       ║\n");
        printf("  ║   Your flag: %s\n", pin);
        printf("  ║                                       ║\n");
        printf("  ╚═══════════════════════════════════════╝\n");
        printf("\n  [*] Account balance: $1,337,420.69\n");
        printf("  [*] Transaction history: 42 elite operations\n\n");
    } else {
        printf("  ╔═══════════════════════════════════════╗\n");
        printf("  ║                                       ║\n");
        printf("  ║       ✗ ACCESS DENIED ✗               ║\n");
        printf("  ║                                       ║\n");
        printf("  ║   Invalid PIN code!                   ║\n");
        printf("  ║   Security breach detected.           ║\n");
        printf("  ║                                       ║\n");
        printf("  ╚═══════════════════════════════════════╝\n");
        printf("\n  [!] Notifying security team...\n");
        printf("  [!] Locking ATM terminal...\n\n");
    }

    return 0;
}
