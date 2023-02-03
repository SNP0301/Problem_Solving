#include <stdio.h>
#include <stdlib.h>

int main(){

    int N, M, i, j, check;
    int* sg_arr;
    int* contrast_arr;

    scanf("%d", &N);
    sg_arr = (int*)malloc(sizeof(int)*N);

    for(i=0; i<N; i++){
        scanf("%d",&sg_arr[i]);
    }

    scanf("%d", &M);
    contrast_arr = (int*)malloc(sizeof(int)*M);

    for(i=0; i<M; i++){
        scanf("%d",&contrast_arr[i]);
    }
    
    for(i=0; i<M; i++){
        check = 0;
        for(j=0; j<N; j++){
            if(contrast_arr[i]==sg_arr[j]) check = 1;
        }
        if (check == 0) printf("0 ");
        else printf("1 ");
    }

    return 0;
}