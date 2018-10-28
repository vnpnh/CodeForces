#include <stdio.h>
#include <string.h>
int main(){

    int n,x = 0;
    char a[4];
    scanf("%d",&n);

    int i;
    for(i = 0;i < n;i++){
        scanf("%s",&a);
        if((strcmp(a,"X++")==0)||strcmp(a,"++X")==0) {
            x+=1;
        }
        else{
            x-=1;
        }
    }
    printf("%d",x);




    return 0;
}
