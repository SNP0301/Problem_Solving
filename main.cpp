#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int>& vec, int left, int mid, int right){
    int i,j,k;
    int fIdx = mid - left + 1;
    int sIdx = right - mid;

    vector<int> leftVc(fIdx), rightVc(sIdx);

    for(i=0; i<fIdx; ++i) leftVc[i] = vec[left+i];
    for(j=0; j<sIdx; ++j) rightVc[j] = vec[mid+1+j];

    i=0;
    j=0;
    k=left;

    while (i < fIdx && j <sIdx){
        if (leftVc[i] <= rightVc[j]){
            vec[k] = leftVc[i];
            ++i;
        }
        else{
            vec[k] = rightVc[j];
            ++j;
        }
        ++k;
    }

    while (i < fIdx){
        vec[k] = leftVc[i];
        ++i;
        ++k;
    }

    while (j < sIdx){
        vec[k] = rightVc[j];
        ++j;
        ++k;
    }
}

void mergeSort(vector<int>& vec, int left, int right){
    if (left <right){ // base case: size가 1인 경우 left == right가 true이므로 재귀 종료.
        int mid = left + (right - left) / 2;

        mergeSort(vec,left,mid);
        mergeSort(vec,mid+1,right);

        merge(vec, left, mid, right);
    }

}