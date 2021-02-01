#include <iostream>
#include <vector>
#include <string>
#include "constants.h"

double calculateDistanceFallen(int seconds)
{
    // approximate distance fallen after a particular number of seconds
    double distanceFallen = myConstants::gravity * seconds * seconds / 2;
    return distanceFallen;
}

void printStatus(int seconds, double height)
{
    std::cout << "At " << seconds
    << " seconds, the ball is at height "
    << height << " meters\n";
}

int main()
{
    using namespace std;
    cout << "Enter the initial height of the tower in meters: ";
    double initialHeight;
    cin >> initialHeight;

    double heightFallen = 0;
    int seconds = 0;
    while (calculateDistanceFallen(seconds) < 100) {
        printStatus(seconds, initialHeight - calculateDistanceFallen(seconds));
        seconds ++;
    }
    printStatus(5, 0);
    return 0;
}