import java.util.HashSet;

public class Solution {
  public static boolean hasDuplicate(int[] nums) {
    HashSet<Integer> seen = new HashSet<>();

    for (int num : nums) {
      if (seen.contains(num)) {
        return true;
      }

      seen.add(num);
    }

    return false;
  }

  public static void main(String[] args) {
    int nums1[] = {1,2,3,3};
    int nums2[] = {1,2,5,3};

    System.out.println(hasDuplicate(nums1));
    System.out.println(hasDuplicate(nums2));
  }
}
