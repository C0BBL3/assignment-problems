# include <iostream>
# include <cassert>



int seqSum(int n) {
    if (n == 0) { return 0; }    
    else if (n == 1) { return 1; }
    else {
        int terms[n+1];
        terms[0] = 0;
        terms[1] = 1;
        int sum = 1;
        for(int i = 2; i <= n ; i++) {
            terms[i] = terms[i - 1] + 2 * terms[i - 2];
            sum += terms[i];
        }
        return sum;
    }
}

int extendedSeqSum(int n) {
    if (n == 0) { return 0; }    
    else if (n == 1) { return 1; }
    else {
        int terms[n+1];
        terms[0] = 0;
        terms[1] = 1;
        for(int i = 2; i <= n ; i++) {
            terms[i] = terms[i - 1] + 2 * terms[i - 2];
        }
        int valueOfNthTerm = terms[n];
        int extendedTerms[valueOfNthTerm];
        int sum = 0;
        for(int i = 0; i <= valueOfNthTerm ; i++) {
            if (i < n) { 
                extendedTerms[i] = terms[i];
                sum += extendedTerms[i];
            }
            else { 
                extendedTerms[i] = extendedTerms[i - 1] + 2 * extendedTerms[i - 2];
                sum += extendedTerms[i];
            }
        }
        return sum;
    }
}

// write your functions seqSum and extendedSeqSum here
// no

int main()
{
    std::cout << "Testing...\n";

    assert(seqSum(0)==0);
    assert(seqSum(3)==5);
    assert(seqSum(8)==170);

    assert(extendedSeqSum(2)==1);
    assert(extendedSeqSum(3)==5);
    assert(extendedSeqSum(4)==21);

    std::cout << "Success!\n";

    return 0;
}