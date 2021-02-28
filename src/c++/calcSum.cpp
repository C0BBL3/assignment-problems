#include <iostream>
#include <cassert>

int calcSum(int m, int n) {
    int sum = 0;
    for (int x = 0; x < m; x++) {
        for (int y = 0; y < m; y++) {
            for(int i = 0; i < n; i++) {
                sum += (x * n + i + 1) * (m * (n - i) - y);
            }
        }
   }
 return sum;
}

int main() {
    std::cout << "Testing...\n";

    assert(calcSum(2, 3)==131);

    std::cout << "Success!";

    return 0;
}