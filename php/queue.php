<?php

class Queue {
    public $front;
    public $rear;

    public $queue = array();

    function __construct() {
        $this->front = -1;
        $this->rear = -1;
    }

    function isEmpty() {
        if ($this->front == $this->rear) {
            return true;
        }
        return false;
    }

    function size() {
        // if size is empty, return 0
        $size = $this->rear - $this->front;
        echo "The size of the queue is " . $size . " elements. \n";
    }

    function frontElement() {
        if ($this->isEmpty()) {
            echo "There is no front element - the queue is empty. \n";
        } else {
            $frontElement = $this->queue[$this->front + 1];
            echo "The front element is " . $frontElement . ".\n";
        }
    }

    function rearElement() {
        if ($this->isEmpty()) {
            echo "There is no rear element - the queue is empty. \n";
        } else {
            $rearElement = $this->queue[$this->rear];
            echo "The rear element is " . $rearElement . ".\n";
        }
    }

    function enQueue($element) {
        $this->queue[++$this->rear] = $element;
        echo $element." was added to the queue. \n";
    }

    function deQueue() {
        if ($this->isEmpty()) {
            echo "Cannot dequeue - the queue is empty. \n";
        } else {
            $element = $this->queue[++$this->front];
            echo $element . " was deleted from the queue. \n";
        }
    }
}

$myQueue = new Queue;

if ($myQueue->isEmpty()) {
    echo "The queue is empty. \n";
} else {
    echo "The queue is not empty. \n";
}

$myQueue->enQueue(10);
$myQueue->enQueue(20);
$myQueue->enQueue(30);
$myQueue->enQueue(40);
$myQueue->frontElement();
$myQueue->rearElement();
$myQueue->size();

$myQueue->deQueue();
$myQueue->frontElement();
$myQueue->rearElement();
$myQueue->size();

$myQueue->deQueue();
$myQueue->deQueue();
$myQueue->frontElement();
$myQueue->rearElement();
$myQueue->size();
if ($myQueue->isEmpty()) {
    echo "The queue is empty. \n";
} else {
    echo "The queue is not empty. \n";
}

$myQueue->deQueue();
$myQueue->frontElement();
$myQueue->rearElement();
$myQueue->size();
if ($myQueue->isEmpty()) {
    echo "The queue is empty. \n";
} else {
    echo "The queue is not empty. \n";
}
?>