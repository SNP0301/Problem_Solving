#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool is_apocalypse(int num);
int get_num_size(int num);

int main(){
    int N;
    int cnt = 0;
    int num = 665;
    scanf("%d", &N);


    while(1){
        if(is_apocalypse(num) == true) cnt += 1;

        if(cnt == N){
            printf("%d", num);
            break;
        }
        else num += 1;
    }
    

    

    return 0;
}

int get_num_size(int num){
    int size = 1;

    while (num / 10 >= 1){
            size += 1;
            num /= 10;
    }

    return size;
}

bool is_apocalypse(int num){
    int size,i;
    int life;
    int denum = 10;
    int tmp = num;

    if (num < 666) return false;
    else if (num == 666) return true;
    else {
        size = get_num_size(num);
        life = size-2;
        int* arr;
        arr = (int*)malloc(sizeof(int)*size);

        for(i=size-1; i>=0; i--){
            arr[i] = tmp % 10;
            tmp /= 10;
            //printf("[%d] ", arr[i]);
        }
        tmp = num;

        for(i=0; i<life; i++){
            if(arr[i] == 6){
                if (arr[i+1] == 6){
                    if (arr[i+2] == 6) return true;
                }
            }
        }

    }
    return false;
}
