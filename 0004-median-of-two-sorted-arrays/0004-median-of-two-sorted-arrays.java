class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] nums3=new int[nums1.length+nums2.length];
        int i=0, j=0,k=0;
        
        while(i<nums1.length&&j<nums2.length){
            if(nums1[i]>nums2[j])
                nums3[k++]=nums2[j++];
            else
                nums3[k++]=nums1[i++];
        }
        
        while(i<nums1.length)
            nums3[k++]=nums1[i++];
        
        while(j<nums2.length)
            nums3[k++]=nums2[j++];
                
        return (nums3.length%2==0) ? ((double)(nums3[nums3.length/2]+nums3[(nums3.length/2)-1])/2) : nums3[nums3.length/2]; 
    }
}