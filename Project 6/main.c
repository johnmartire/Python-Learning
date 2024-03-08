#include <stdio.h>

int main (void) 
{
    
    double height = (2.45);
    double width = (5.35);
    double sum = height + width;
    
    
    double perimeter=2.0*(sum);
    double area = width*height;

    
    printf("The area of a rectangle is: %.2f\n", area);
    printf("The perimeter of a rectangle is: %.2f\n", perimeter);

    
    

return 0;
}