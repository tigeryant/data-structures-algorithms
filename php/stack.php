<?php

class Stack {
    public $top;
    public $stack = array();

    function __construct() {
        $this->top = -1;
    }

    function isEmpty() {
        if ($this->top == -1) {
            echo "The stack is empty. \n";
            return true;
        }
        echo "The stack is not empty. \n";
        return false;
    }

    function size() {
        $size = $this->top + 1;
        echo "The size of the stack is " . $size . " elements. \n";
    }

    function topElement() {
        if ($this->isEmpty()) {
            echo "There is no top element in the stack. \n";
        } else {
            $topElement = $this->stack[$this->top];
            echo "The top element is: " . $topElement . ". \n";
        }
    }

    function push($element) {
        $this->stack[++$this->top] = $element;
        echo $element . " was added to the stack. \n";
    }

    function pop() {
        if ($this->isEmpty()) {
            echo "Nothing to pop - the stack is empty. \n";
        } else {
            $element = $this->stack[$this->top--];
            echo $element . " was removed from the stack. \n";
        }
    }
}

$myStack = new Stack();

$myStack->size();
$myStack->topElement();

$myStack->push(10);
$myStack->push(20);
$myStack->push(30);

$myStack->size();
$myStack->topElement();

$myStack->pop();
$myStack->size();
$myStack->topElement();
?>