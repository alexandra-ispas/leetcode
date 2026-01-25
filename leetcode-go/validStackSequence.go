type stack []int

func (s stack) Push(value int) stack {
    return append(s, value)
}

func (s stack) Length() int{
    return len(s)
}

func (s stack) Peek() int{
    len := s.Length()
    return s[len-1]
}

func (s stack) Pop() stack{
    l := len(s)
    return  s[:l-1]
}

func validateStackSequences(pushed []int, popped []int) bool {
    var i, j int
    s := make(stack, 0)

    for {
        // there is nothing in the stack
        if i < len(pushed) && s.Length() == 0 {
            s = s.Push(pushed[i])
            i++
            continue
        } 
        // first try to pop somthing
        if j < len(popped){
            if s.Length() > 0 && s.Peek() == popped[j] {
                s=s.Pop()
                j++
                continue
            } else {
                if i < len(pushed) {
                    s=s.Push(pushed[i])
                    i++
                    continue
                }  
            }
        }

        // matches
        if i == len(pushed) && j == len(popped){
            return true
        }
        return false
    }
}
