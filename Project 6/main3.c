#include <stdio.h>

int main()
{
    double height;
    double width;
 
    printf("enter height: ");
    scanf("%lf", &height);
    printf("enter width: ");
    scanf("%lf", &width);
    double product = height*width;

    printf("the area is %.2f", product);

    return 0;
}