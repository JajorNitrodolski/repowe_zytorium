#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubbleSort(short* arr, unsigned size){
    short temp;
    for(unsigned i=0; i<size; i++){
        for(unsigned j=1; j<size; j++){
            if(arr[j]<arr[j-1]){
                temp=arr[j];
                arr[j]=arr[j-1];
                arr[j-1]=temp;
            }
        }
    }
}
void insertionSort(short* arr, unsigned size){
    short temp, key;
    for(unsigned i=0; i<size; i++){
        for(unsigned j=i; j>0; j--){
            if(arr[j]>=arr[j-1]) continue;
            temp=arr[j];
            arr[j]=arr[j-1];
            arr[j-1]=temp;
        }
    }
}
void mergeSortedArrays(short* arr, unsigned left, unsigned mid, unsigned right){
    unsigned leftSize=mid-left+1, rightSize=right-mid;
    short tempLeftArr[leftSize], tempRightArr[rightSize];
    for(unsigned i=0; i<leftSize; i++) tempLeftArr[i]=arr[left+i];
    for(unsigned i=0; i<rightSize; i++) tempRightArr[i]=arr[mid+1+i];
    for(unsigned i=0, j=0, k=left; k<=right; k++){
        if((i<leftSize)&&(j>=rightSize||tempLeftArr[i]<=tempRightArr[j])){
            arr[k]=tempLeftArr[i];
            i++;
        }
        else{
            arr[k]=tempRightArr[j];
            j++;
        }
    }
}
void mergeSort(short* arr, unsigned left, unsigned right){
    if(left>=right) return;
    unsigned mid=left+(right-left)/2;
    mergeSort(arr,left,mid);
    mergeSort(arr,mid+1,right);
    mergeSortedArrays(arr,left,mid,right);
}

int main(void){
    short array[]={7,18,5,6,9,2,10,16,11};
    //mergeSort(array,0,sizeof(array)/sizeof(short)-1);
    //insertionSort(array,sizeof(array)/sizeof(short));
    //bubbleSort(array,sizeof(array)/sizeof(short));
    for(unsigned i=0; i<sizeof(array)/sizeof(short); i++) printf("%d ",array[i]);
    return 0;
}