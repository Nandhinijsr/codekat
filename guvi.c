#include<stdio.h>
void main()
{
int n;
printf("Enter n");
scanf("%d",&n);
if(n>0)
{
printf("positive");
}
elseif(n<0)
{
printf("negative");
}
else
{
printf("zero");
}
}