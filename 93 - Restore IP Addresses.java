import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        // If the string length is not between 4 and 12, it's impossible to form valid IPs
        if (s.length() < 4 || s.length() > 12) return result;
        
        backtrack(result, s, 0, "", 0);
        return result;
    }

    private void backtrack(List<String> result, String s, int index, String currentIP, int segment) {
        // Base case: if 4 segments are formed and the entire string is used
        if (segment == 4 && index == s.length()) {
            result.add(currentIP);
            return;
        }

        // If 4 segments are formed but the string is not fully used, stop
        if (segment == 4 || index == s.length()) return;

        // Try all possible segment lengths (1, 2, 3)
        for (int length = 1; length <= 3; length++) {
            // If the remaining string is too short or too long for valid IPs, stop
            if (index + length > s.length()) break;

            String part = s.substring(index, index + length);

            // Validate the current segment
            if (isValid(part)) {
                backtrack(result, s, index + length, 
                          currentIP + (segment == 0 ? "" : ".") + part, segment + 1);
            }
        }
    }

    private boolean isValid(String part) {
        // Check if the part is between 0 and 255 and has no leading zeros
        if (part.length() > 1 && part.startsWith("0")) return false;
        int value = Integer.parseInt(part);
        return value >= 0 && value <= 255;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String input = "25525511135";
        List<String> ipAddresses = solution.restoreIpAddresses(input);
        System.out.println("Valid IP addresses: " + ipAddresses);
    }
}
