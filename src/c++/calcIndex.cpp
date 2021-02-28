# include <iostream>
# include <cassert>

int calcIndex(int number) 
{
    int sequence[number + 1];
    sequence[0] = 0;
    sequence[1] = 1;

    for (int i = 2; i <= number; i++) {
        sequence[i] = sequence[i-1] + sequence[i-2];
        if (sequence[i] >= number)
            return i;
        
    };
        
    return sizeof sequence / sizeof sequence[0];
}

int main()
{
    std::cout << "Testing...\n";

    assert(calcIndex(8)==6);
    assert(calcIndex(100000)==26);

    std::cout << "Success!";

    return 0;
}