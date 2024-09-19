#include <stdio.h>

int main(void)
{
	double km;
	double mile;
	printf("Please enter kilometers: ");
	scanf_s("%lf", &km);
	mile = (double)km / 1.609;
	printf("%.1fkm is equal to %.1fmiles.", km, mile);

	return 0;
}