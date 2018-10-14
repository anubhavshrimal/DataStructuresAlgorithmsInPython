#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a[20],n,i,pass,step,temp;
    printf("total elements\n");
    scanf("%d",&n);
    printf("enter elements\n");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    pass=1;
    while(pass<=n-1)
    {
        step=0;
        while(step<=n-pass)
        {

        if(a[step+1]<a[step])
        {
            temp =a[step];
            a[step]=a[step+1];
            a[step+1]=temp;
        }
        step++;}
        printf("\nsteps  %d is\n",pass);
        for(i=0;i<n;i++)
        {
            printf("%d\t",a[i]);
        }
        pass++;

    }
    return 0;
}
