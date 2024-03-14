#include <stdio.h>
int main(void)

{
    int minutes;
    printf ("Enter the amount of minutes:");
    scanf ("%lf", &minutes);
    double days = minutes / (60 * 24);
    int years = days = 365.25;
    double remainingDays = days = (years * 365);

    printf("Converted into years and days: %d years and %.2f days\n", years, remainingDays);

    return 0;
}