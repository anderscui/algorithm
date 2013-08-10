#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "point.h"

float randFloat()
{
    return 1.0 * rand() / RAND_MAX;
}

float distance(Point p1, Point p2)
{
    double delta_x = p1.x - p2.x;
    double delta_y = p1.y - p2.y;
    return sqrt(delta_x * delta_x + delta_y * delta_y);
}

// cmd: app n-points d-distance
int main(int argc, char *argv[])
{
    int n = atoi(argv[1]);
    float d = atof(argv[2]);
    Point *pts = malloc(n * sizeof(Point));

    int i, j;
    for (i = 0; i < n; i++)
    {
        pts[i].x = randFloat();
        pts[i].y = randFloat();
        printf("(%f, %f) \n", pts[i].x, pts[i].y);
    }

    int cnt = 0;
    for (i = 0; i < n; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if(distance(pts[i], pts[j]) < d)
                cnt++;
        }
    }

    printf("%d lines shorter than %f", cnt, d);
    return 0;
}
