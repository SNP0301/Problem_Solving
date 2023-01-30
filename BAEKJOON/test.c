#include <stdio.h>
#include <stdlib.h>


int main (){
    int N, M, i, j;
    scanf("%d %d", &N, &M);

    char** board;
    board = (char**)malloc(sizeof(char*)*N);
    for(i=0; i<N; i++){
        board[i] = (char*)malloc(sizeof(char)*M);
    }

    for (i=0; i<N; i++){
        for (j=0; j<M; j++){
            scanf("%c", &board[i][j]);
        }
    }

    printf("\n==========\n");
    for (i=0; i<N; i++){
        for (j=0; j<M; j++){
            printf("%c", board[i][j]);
        }
        printf("\n");
    }

    return 0;
}