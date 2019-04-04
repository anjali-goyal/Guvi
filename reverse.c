#include <stdio.h>

int main()
{
    char str[100];
    scanf("%s",str);
    int n=0;
    int i=0;
    while(str[i]!='\0'){
        n++;
        i++;
    }
    for(i=n-1;i>=0;i--){
        printf("%c",str[i]);
    }
    return 0;
}
