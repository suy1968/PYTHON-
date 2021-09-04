if __name__=='__main_':
    s=[12,3,1,5,6,4,10,9,8,0];
    n=len(s);
    max_end = [-38749432]*(n+1);
    for i in range(n-1,0,-1):
        max_end[i] = max(max_end[i+1],s[i]);
        result = 0;
    for i in range(0,n):
        low =i+1;high=n-1;ans=i;
        while(low<=high):
            mid= int((low+high)/2);
            if(s[i] <=max_end[mid]):
                ans= max(ans,mid);
                low=mid+1;
            else:
                high = mid-1;
        result = max(result,ans-i);
    print(result,end=" ");
