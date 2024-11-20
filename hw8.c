#include <stdio.h>
#include <math.h>

double calculateStandardDeviation(double arr[], int size) 
{
    double mean = 0.0, variance = 0.0, stdDev = 0.0;

    for (int i = 0; i < size; i++) 
    {
        mean += arr[i];
    }
    mean /= size;

    for (int i = 0; i < size; i++) 
    {
        variance += pow(arr[i] - mean, 2);
    }
    variance /= size;

    stdDev = sqrt(variance);

    return stdDev;
}

int main() 
{
    double numbers[5];
    int size = 5;

    printf("Enter 5 real numbers: ");
    for (int i = 0; i < size; i++) {
        scanf_s("%lf", &numbers[i]);
    }

    double stdDev = calculateStandardDeviation(numbers, size);
    printf("Standard Deviation = %.3f\n", stdDev);

    return 0;
}
