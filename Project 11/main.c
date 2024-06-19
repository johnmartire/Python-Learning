// Pagination
#include <stdio.h>

int main()
{
    int low;
    int up;
    scanf("%d%d", &low, &up);
    for (int i = low; i <= up; i++)
    {
        printf("%d ", i);
    }

    return 0;
}