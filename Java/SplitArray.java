import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SplitArray {
    public static int[][] divideArray(int[] nums, int k) {
        Arrays.sort(nums); // Sort the input array
        
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentArray = new ArrayList<>();

        // Iterate over the sorted array
        for (int num : nums) {
            // If the current array is empty or the difference between
            // the current number and the last number in the array is <= k,
            // we can add the number to the current array
            if (currentArray.isEmpty() || 
                Math.abs(num - currentArray.get(currentArray.size() - 1)) <= k) {
                currentArray.add(num);
                // If the current array size is 3, we add it to the result
                if (currentArray.size() == 3) {
                    result.add(new ArrayList<>(currentArray));
                    // Clear the current array to start forming a new one
                    currentArray.clear();
                }
            } else {
                // If the condition is not met, it's impossible to form valid arrays,
                // so we return an empty array
                return new int[0][0];
            }
        }

        // If there's still an incomplete array in currentArray,
        // it means it's impossible to satisfy the conditions
        if (!currentArray.isEmpty()) {
            return new int[0][0];
        }

        // Convert the List of Lists to a 2D array
        int[][] nArray = new int[result.size()][3];
        for (int i = 0; i < result.size(); i++) {
            for (int j = 0; j < 3; j++) {
                nArray[i][j] = result.get(i).get(j);
            }
        }

        return nArray;
    }
    public static void print2DArray(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
        public static void main(String[] args) {
        int[] nums = {15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2};
        print2DArray(divideArray(nums,2));
    }
}





