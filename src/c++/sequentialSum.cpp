# include <iostream>
# include <cassert>

// write your functions seqSum and extendedSeqSum here
int arr [9] = {0, 1, 1, 3, 5, 11, 21, 43, 85};

int seqSum(int n) {
    if (n == 0) { return 0; }    
    else if (n == 1) { return 1; }
    else {
        int sum = 0;
        for(int i = 0; i <= n ; i++)
            sum += arr[i];
        return sum;
    }
}

int extendedSeqSum(int n) {
    return seqSum(arr[n]);
}

int main()
{
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(3)==5);

    std::cout << "Success!\n";

    return 0;
}