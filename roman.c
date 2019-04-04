#include <stdio.h>
int final(int x,char *rom,int n,int i){
    if(x==0){
        if(rom[i+1]=='V')
            return 4;
        else if(rom[i+1]=='X')
            return 9;
        else
            return n;
    }
    else if(x==5){
            return x+(n-1);
    }
    else if(x==10){
        if(rom[i+1]=='V')
            return 9+final(5,rom,n,1);
        else if(rom[i+1]=='I')
            return 9+final(0,rom,n,1);
        else
            return 10*n;
    }
}
int main()
{
    char roman[10];
    scanf("%s",roman);
    int num;
    int n=0;
    for(int i=0;roman[i]!='\0';i++)
        n++;
    if(roman[0]=='V'){
        num=final(5,roman,n,0);
    }
    else if(roman[0]=='X'){
        num=final(10,roman,n,0);
    }
    else{
       num=final(0,roman,n,0);
    }
    printf("%d",num);
    return 0;
}
