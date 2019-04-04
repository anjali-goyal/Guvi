import java.util.Scanner;
class Main{
public static void main(String args[]){
Scanner sc=new Scanner(System.in);
int n=sc.nextInt();
int r=0;
int tmp=n;
while(tmp!=0){
int x=tmp%10;
r=r*10+x;
tmp=tmp/10;
}
System.out.println(r);
}
}