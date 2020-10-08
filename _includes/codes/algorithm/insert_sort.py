def insert_sort(num_list):
    n=len(num_list)
    for i in range(1,n):
        for j in range(i,0,-1):
            if num_list[j]<num_list[j-1]:
                num_list[j],num_list[j-1]=num_list[j-1],num_list[j]
            else:
                break

def main():
    num_list=[1,3,5,7,6,2,3,1,-1]
    print('original list: ', num_list)
    insert_sort(num_list)
    print('sorted list: ', num_list)

if __name__=='__main__':
    main()
