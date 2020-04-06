#include <stdio.h>
#include <stdlib.h>
typedef struct Node node;
struct Node
{
    int stt;
    char id[10];
    char name[25];
    char phonenum[20];
    float grade;
};

void inputdata(FILE *datain, node *arraynew, int max)
{
    int i = 0;
    while(i<max)
    {
        fread(&arraynew[i], sizeof(node), 1, datain);
        i++;
    } 
}
void printout(node *array, int max)
{
    int i = 0;
    while (i < max)
    {
        printf("%-3d%-20s%-30s%-20s%-.2f\n", array[i].stt, array[i].id, array[i].name, array[i].phonenum, array[i].grade);
        i++;
    }
}

int main()
{
    node *studentlist = (node *) malloc(sizeof(node *));
    FILE *fpin = fopen("transcript.dat", "rb");
    int start = 0, end = 0;
    printf("Enter the start point: ");
    scanf("%d", &start);
    getchar();
    printf("Enter the end point: ");
    scanf("%d", &end);
    getchar();
    int max = end - start + 1;
    fseek(fpin, (start-1)*sizeof(node), SEEK_SET);
    inputdata(fpin, studentlist, max);
    printout(studentlist, max);
    fclose(fpin);
    free(studentlist);
    return 0;
}
