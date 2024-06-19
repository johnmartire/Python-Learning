// Program to Find area
#include <stdio.h>
int main()

{
    double height;
    double width;

    printf("Enter height:");
    scanf("%lf", &height);
    printf("Enter width:");
    scanf("%lf", &width);
    double product = width * height;
    printf("The area is: %f\n", product);

    return 0;
}