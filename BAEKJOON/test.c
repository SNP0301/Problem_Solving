#include <stdio.h>
#include <stdlib.h>

struct point{
    int x;
    int y;
};

int main(){

    int N, i;
    scanf("%d", &N);

    struct point* pnt = malloc(sizeof(struct point)*N);

    for(i=0; i<N; i++){
        scanf("%d %d", &pnt[i].x, &pnt[i].y);
    }

    

    return 0;
}