type FooBar struct {
	n int
    chanel chan int
}

func NewFooBar(n int) *FooBar {
	return &FooBar{n: n, chanel: make(chan int)}
}

func (fb *FooBar) Foo(printFoo func()) {
	for i := 0; i < fb.n; i++ {
		// printFoo() outputs "foo". Do not change or remove this line.
        printFoo()
        fb.chanel <- i
        <- fb.chanel
	}
}

func (fb *FooBar) Bar(printBar func()) {
	for i := 0; i < fb.n; i++ {
		// printBar() outputs "bar". Do not change or remove this line.
        <- fb.chanel
        printBar()
        fb.chanel <- i
	}
}