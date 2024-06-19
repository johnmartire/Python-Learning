// enum program

#include <stdio.h>
#include <stdlib.h>

int main()
{
    enum color
    {
        BLUE,
        RED,
        GREEN,
        PURPLE
    };

    enum color blue = BLUE;
    enum color purple = PURPLE;
    enum color red = RED;

    printf("The value of blue is: %d\n", BLUE);
    printf("The value of purple is: %d\n", PURPLE);
    printf("The value of red is: %d\n", RED);

    return 0;
}