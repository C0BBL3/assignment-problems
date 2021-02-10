# include <iostream>
# include <cassert>

int fibonacci(int n) {
    if (n==0)
        return 0;
    else if (n==1)
        return 1;
    else
        return fibonacci(n - 1) + fibonacci(n - 2);
}

int kthPartialSum(int n) {
    int sum = 0;
    for (int i = 0; i <= n; i++) 
        sum += fibonacci(i);
    return sum;
}

int metaFibonacciSum(int n) {
    if (n==0)
        return 0;
    else if (n==1)
        return 1;
    else {
        int sum = 0;
        for (int i = 0; i <= n; i++)
            sum += kthPartialSum(fibonacci(i));
        return sum;
    }
}


int main()
{
    std::cout << "Testing...\n";

    assert(metaFibonacciSum(6)==74);

    std::cout << "Success!\n";

    return 0;
}