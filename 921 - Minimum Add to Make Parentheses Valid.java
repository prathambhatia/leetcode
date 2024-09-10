class Solution {
    public int minAddToMakeValid(String s) {
        //Stack<Character> stack = new Stack<>();
        int open = 0;
        int close = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (c == '(') {
                open++;//stack.push(c);
            } else {
                //if (stack.isEmpty() || stack.peek() == ')') {
                    if(open == 0){
                        close++; //stack.push(c)
                    }
                 else {
                    open--;//stack.pop();
                }
            }
        }

        return (open + close);//stack.size();
    }
}
