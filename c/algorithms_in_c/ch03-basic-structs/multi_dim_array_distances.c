#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    float x;
    float y;
} point;

typedef struct node *link;
struct node
{
    point p;
    link next;
};

link **grid;
int G;
float d;
int cnt = 0;

void grid_insert(float x, float y)
{

}

link **malloc2d(int r, int c)
{
    int i;
    link **t = malloc(r * sizeof(link *));
    for (i = 0; i < r; i++)
    {
        t[i] = malloc(c * sizeof(link));
    }

    return t;
}

float randFloat()
{
    return 1.0 * rand() / RAND_MAX;
}

int main(int argc, char *argv[])
{
    int i, j, N = atoi(argv[1]);
    d = atof(argv[2]);
    G = 1 / d;
    grid = malloc2d(G + 2, G + 2);
    for (i = 0; i < G+2; i++)
    {
        for (j = 0; j < G+2; j++)
        {
            grid[i][j] = NULL;
        }
    }

    for (i = 0; i < N; i++)
    {
        grid_insert(randFloat(), randFloat());
    }
    printf("\n %d \n", cnt);

    return 0;
}
