public class Append_Characters_to_String_to_Make_Subsequence {
    public int appendCharacters(String s, String t) {
        int index = 0;
    
        // Iterate over `s` and try to match characters from `t`
        for (int i = 0; i < s.length(); i++) {
            if (index < t.length() && s.charAt(i) == t.charAt(index)) {
                index++;
            }
        }
    
        // The number of characters left in `t` that were not matched
        return t.length() - index;
    }
}
