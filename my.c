#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int l, int m, int r){
    int i,j,k;
    int n1 = m - l + 1;
    int n2 = r - m;

    int L[n1], R[n2];

    for(i=0; i<n1; i++) L[i] = arr[l + i];
    for(j=0; j<n2; j++) R[j] = arr[m + 1 + j];

    i = 0;
    j = 0;
    k = l;

    while (i < n1 && j < n2){
        if(L[i] <= R[j]){
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1){
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2){
        arr[k] = R[j];
        j++;
        k++;
    }
}
void mergeSort(int arr[], int l, int r){
    if (l <r){
        int m = l + (r-l)/2;
        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);

        merge(arr, l, m, r);
    }
}

typedef struct point{
    int x;
    int y;
} point;

int main(){
    int N,i;
    scanf("%d", &N);

    point* point_arr = malloc(sizeof(point)*N);
    int* x_arr = malloc(sizeof(int)*N);
    int* y_arr = malloc(sizeof(int)*N);

    for(i=0; i<N; i++){
        scanf("%d %d", &point_arr[i].x, &point_arr[i].y);
    }

    for(i=0; i<N; i++){
        x_arr[i] = point_arr[i].x;
    }
    

    free(point_arr);
    free(x_arr);
    free(y_arr);

    return 0;
}