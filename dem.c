// Online C compiler to run C program online
#include <stdio.h>

int inputArray(int a[], int size){
    for(int i=0;i<size;i++){
        scanf("%d",&a[i]);
    }
}

// int isElement(int a[],int size, int element){
//     for(int i=0;i<size;++){
//         if(a[i]==element){
//             return 1;
//     }
//     return 0;
// }


int main() {

    int n;
   
    printf("enter the number of tickets purchased: ");
    scanf("%d",&n);
    
    printf("enter the ticket number: ");
    int b[n];
    inputArray(b,n);
    for (int i = 0; i < n; i++){
        printf(" %d ", b[i]);
    }
    
    printf("\n enter the winning ticket numbers: ");
    int l[10];
    inputArray(l,10);
    for (int i = 0; i < 10; i++){
        printf(" %d ", l[i]);
    }

   for(int i=0;i<10;i++){
       for(int j=0;j<=n;j++){
           if(l[i]==b[j]){
               printf("\nyou have won %d ",i);
               
           }
       }
       
   }
    
    return 0;
}