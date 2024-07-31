
import java.util.HashMap;

public class Longest_Palindrome {
    public int longestPalindrome(String s) {
        HashMap<Character,Integer> freg = new HashMap<>();
    for(char c: s.toCharArray()){
        freg.put(c,freg.getOrDefault(c, 0)+1); 
        }
        int length = 0;
        boolean oddFound = false;
        
        // Iterate through the frequency map
        for (int count : freg.values()) {
            if (count % 2 == 0) {
                length += count;
            } else {
                length += count - 1; // Add the largest even number less than count
                oddFound = true;     // There is at least one character with an odd count
            }
        }
        
        // If there's any character with an odd count, we can place exactly one in the center of the palindrome
        if (oddFound) {
            length++;
        }
        
        return length;
    }
}
