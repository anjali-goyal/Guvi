#include<stdio.h>
int main(){
    int n,arr[100];
    int min=arr[0];
    scanf("%d",&n);
    int i;
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        if(arr[i]<min){
            min=arr[i];
        }
    }
    printf("%d",max);
    return 0;
}
