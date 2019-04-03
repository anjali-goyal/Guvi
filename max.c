#include<stdio.h>
int main(){
    int n,arr[100];
    int max=arr[0];
    scanf("%d",&n);
    int i;
    for(i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    for(i=0;i<n;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    printf("%d",max);
    return 0;
}
