#include<iostream>
using namespace std;

void tem_swap(int array[],int i, int j)
{
	int tem=array[i];
	array[i]=array[j];
	array[j]=tem;
}

void insert_sort(int array[], int n)
{
	for(int i=1;i<n;i++)
	{
		for(int j=i;j>0;j--)
			if(array[j]<array[j-1])
				tem_swap(array,j,j-1);
			else
				break;
	}
}


int main()
{
	int num_list[6]={1,2,343,5,35,1};
	cout<<"original list:"<<endl;
	for(int i=0; i<6; i++)
		cout<<num_list[i]<<"  ";
	cout<<endl;
	insert_sort(num_list,6);
	cout<<"sorted list:"<<endl;
	for(int i=0; i<6; i++)
		cout<<num_list[i]<<"  ";
	cout<<endl;
	return 0;
}

